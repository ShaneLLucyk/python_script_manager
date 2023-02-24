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

        self.file_path_label = tk.Label(self.app.root.table, text=self.file_path, bd=1, relief="solid", font="TkDefaultFont 9")
        self.file_path_label.grid(row=self.row, column=0, padx=10, pady=5, sticky="w")

        self.status_label = tk.Label(self.app.root.table, text="Running", bd=1, relief="solid", font="TkDefaultFont 9")
        self.status_label.grid(row=self.row, column=1, padx=10, pady=5, sticky="w")


        self.stop_button = tk.Button(self.app.root.table, text="Stop", command=self.stop_script)
        self.stop_button.grid(row=self.row, column=2, padx=10, pady=5, sticky="w")

        self.kill_button = tk.Button(self.app.root.table, text="Kill", command=self.kill_script)
        self.kill_button.grid(row=self.row, column=3, padx=10, pady=5, sticky="w")

        self.is_running = True

    def run(self):
        try:
            print(f'Generating Script Object: {self.file_path}')
            while self.is_running:
                # execute script code
                print('test')
        except:
            self.status_label.config(text="Error")
            self.parent.remove_script(self)

    def stop_script(self):
        self.is_running = False
        self.status_label.config(text='Stopped')

    def kill_script(self):
        self.is_running = False
        self.destroy()

    def destroy(self):
        self.file_path_label.destroy()
        self.status_label.destroy()
        self.stop_button.destroy()
        self.kill_button.destroy()
