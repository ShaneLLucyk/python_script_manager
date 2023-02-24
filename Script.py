import subprocess
import threading
import tkinter as tk
from tkinter import filedialog
class Script(threading.Thread):
    def __init__(self, file_path, parent):
        super().__init__()
        self.file_path = file_path
        self.app = parent
        self.app.root.table.row = len(self.app.scripts) + 1
        self.row = len(self.app.scripts) + 1

        self.script_label = tk.Label(self.app.root.table, text=self.file_path, bd=1, relief="solid", font="TkDefaultFont 9")
        self.script_label.grid(row=self.row, column=0, padx=10, pady=5, sticky="w")

        self.status_label = tk.Label(self.app.root.table, text="Running", bd=1, relief="solid", font="TkDefaultFont 9")
        self.status_label.grid(row=self.row, column=1, padx=10, pady=5, sticky="w")

    def run(self):
        try:
            print(f'Generating Script Object: {self.file_path}')
            # process = subprocess.Popen(["python", self.file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

            # # proc = subprocess.Popen(["python", self.file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # while True:
            #     output = proc.stdout.readline().decode()
            #     if output == "" and proc.poll() is not None:
            #         break
            #     if output:
            #         self.app.log(output.strip())

            # stderr_output = proc.stderr.read().decode()
            # if stderr_output:
            #     self.app.log(stderr_output.strip())

            # self.status_label.config(text="Finished")
            # self.app.remove_script(self)
        except:
            self.status_label.config(text="Error")
            self.parent.remove_script(self)

    def destroy(self):
        self.script_label.destroy()
        self.status_label.destroy()
