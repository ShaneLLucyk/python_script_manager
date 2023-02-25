import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, ttk
from Script import Script
class Application():
    def __init__(self):
        self.scripts = []
        self.script_paths = []
        self.create_widgets()

    def create_widgets(self):
        self.root = tk.Tk()
        self.root.title("Python Script Log Viewer")
        self.root.minsize(250, 500)
        self.root.wm_state('iconic')
        self.root.wm_iconbitmap('./configuration/fire.ico')

        self.root.button_select = tk.Button(self.root, text='Select Python Script', command=self.select_script)
        self.root.button_select.pack(side="bottom", pady=25)
        self.root.table = tk.Frame(self.root, bd=2,bg='white')
        self.root.table.pack(side="top", padx=10, pady=10)
        tk.Label(self.root.table, text="Script Path", font="TkDefaultFont 9 bold").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root.table, text="Status", font="TkDefaultFont 9 bold").grid(row=0, column=1, padx=10, pady=5, sticky="w")
        tk.Label(self.root.table, text="Kill Script", font="TkDefaultFont 9 bold").grid(row=0, column=3, padx=10, pady=5, sticky="w")


    def select_script(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if file_path != None and file_path.endswith('.py') :
            if file_path not in self.script_paths :
                print(f"Starting script: {file_path}")
                self.script_paths.append(file_path)
                script = Script(file_path, self)
                self.scripts.append(script)
                # script.start()
            else:
                print(f'{file_path} is already running')

    # def remove_script(self, script):
    #     print(f"Script finished: {script.file_path}")
    #     self.scripts.remove(script)
    #     script.destroy()

    def start(self):
            # Run the Tkinter event loop
            self.root.mainloop()

if __name__ == "__main__":
        app = Application()
        app.start()

