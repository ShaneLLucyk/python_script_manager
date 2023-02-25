import subprocess
import threading
import tkinter as tk
from tkinter import filedialog
class Script(threading.Thread):
    def __init__(self, file_path, parent):
        super().__init__()
        self.file_path = file_path
        # parent = parent
        parent.root.table.row = len(parent.scripts) + 1
        self.row = len(parent.scripts) + 1

        file_name = (self.file_path.split('/')[-1]).replace('.py', '')
        self.file_path_label = tk.Label(parent.root.table, text=file_name, font="TkDefaultFont 9")
        self.file_path_label.grid(row=self.row, column=0, padx=10, pady=5, sticky="w")

        self.status_label = tk.Label(parent.root.table, text="Running", font="TkDefaultFont 9")
        self.status_label.grid(row=self.row, column=1, padx=10, pady=5, sticky="w")


        self.stop_button = tk.Button(parent.root.table, text="Stop", font="TkDefaultFont 9", command=self.stop_script)
        self.stop_button.grid(row=self.row, column=2, padx=10, pady=5, sticky="w")

        self.kill_button = tk.Button(parent.root.table, text="Kill", font="TkDefaultFont 9", command=self.kill_script)
        self.kill_button.grid(row=self.row, column=3, padx=10, pady=5, sticky="w")

        self.is_running = True

    def run(self):
        try:
            print(f'Generating Script Object: {self.file_path}')
            # while self.is_running:
            #     # execute script code
            #     print('test')

            self.working_directory = self.file_path.replace((self.file_path.split('/')[-1]), '')
            # self.process = subprocess.Popen(["python", self.file_path], cwd=self.working_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            # # # proc = subprocess.Popen(["python", self.file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # while True:
            #     if self.process.poll() is not None:
            #         self.kill_script()

            # stderr_output = proc.stderr.read().decode()
            # if stderr_output:
            #     parent.log(stderr_output.strip())

            # self.status_label.config(text="Finished")
            # parent.remove_script(self)
        except Exception as e:
            print(f'{e}')
            self.status_label.config(text="Error")
            self.stop_script(self)

    def stop_script(self):
        self.is_running = False
        # self.process.terminate()
        self.status_label.config(text='Stopped')

    def kill_script(self):
        self.destroy()

    def destroy(self):
        self.file_path_label.destroy()
        self.status_label.destroy()
        self.stop_button.destroy()
        self.kill_button.destroy()
