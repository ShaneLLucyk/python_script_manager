import subprocess
import threading
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.scripts = []
        self.create_widgets()

    def create_widgets(self):
        self.button_select = tk.Button(self)
        self.button_select["text"] = "Select Python Script"
        self.button_select["command"] = self.select_script
        self.button_select.pack(side="top")

        self.table = tk.Frame(self)
        self.table.pack(side="top", pady=10)

        tk.Label(self.table, text="Script Path").grid(row=0, column=0)
        tk.Label(self.table, text="Status").grid(row=0, column=1)

    def select_script(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if file_path:
            self.log(f"Starting script: {file_path}")
            script = Script(file_path, self)
            self.scripts.append(script)
            script.start()

    def remove_script(self, script):
        self.log(f"Script finished: {script.file_path}")
        self.scripts.remove(script)
        script.destroy()

    def log(self, msg):
        print(msg)

class Script(threading.Thread):
    def __init__(self, file_path, app):
        super().__init__()
        self.file_path = file_path
        self.app = app

        self.row = len(self.app.scripts) + 1

        self.script_label = tk.Label(self.app.table, text=self.file_path)
        self.script_label.grid(row=self.row, column=0)

        self.status_label = tk.Label(self.app.table, text="Running")
        self.status_label.grid(row=self.row, column=1)

    def run(self):
        try:
            process = subprocess.Popen(["python", self.file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

            # proc = subprocess.Popen(["python", self.file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            while True:
                output = proc.stdout.readline().decode()
                if output == "" and proc.poll() is not None:
                    break
                if output:
                    self.app.log(output.strip())

            stderr_output = proc.stderr.read().decode()
            if stderr_output:
                self.app.log(stderr_output.strip())

            self.status_label.config(text="Finished")
            self.app.remove_script(self)
        except:
            self.status_label.config(text="Error")
            self.app.remove_script(self)

    def destroy(self):
        self.script_label.destroy()
        self.status_label.destroy()
