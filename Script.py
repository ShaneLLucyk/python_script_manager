import subprocess
import threading
import tkinter as tk
from tkinter import filedialog

class Script:
    def __new__(cls, file_path, parent):
        self = super().__new__(cls)
        self.file_path = file_path
        self.parent = parent
        self.parent.root.table.row = len(self.parent.scripts) + 1
        self.row = len(self.parent.scripts) + 1

        self.file_name = (self.file_path.split('/')[-1]).replace('.py', '')
        self.working_directory = self.file_path.replace((self.file_path.split('/')[-1]), '')

        self.file_path_label = tk.Label(self.parent.root.table, text=self.file_name, font="TkDefaultFont 9")
        self.file_path_label.grid(row=self.row, column=0, padx=10, pady=5, sticky="w")

        self.status_label = tk.Label(self.parent.root.table, text="Running", font="TkDefaultFont 9")
        self.status_label.grid(row=self.row, column=1, padx=10, pady=5, sticky="w")

        # self.stop_button = tk.Button(self.parent.root.table, text="Stop", font="TkDefaultFont 9", command=self.stop_script)
        # self.stop_button.grid(row=self.row, column=2, padx=10, pady=5, sticky="w")

        self.kill_button = tk.Button(self.parent.root.table, text="Kill", font="TkDefaultFont 9", command=self.kill_script_button_impl)
        self.kill_button.grid(row=self.row, column=3, padx=10, pady=5, sticky="w")

        self.is_running = True

        threading.Thread(target=self.run).start()

        return self

    def run(self):
        try:
            print(f'Generating Script Object: {self.file_path}')
            self.process = subprocess.Popen(["python", self.file_path], cwd=self.working_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            print(f'PID for subprocess: {self.process.pid}')
            stat = ""
            while True:
                if self.process.poll() is not None:
                    if(self.is_running is not False):
                        stat = 'err'
                        break
            if stat == 'err': 
                self.script_death()

        except Exception as e:
            print(f'{e}')
            self.status_label.config(text="Error")
            print(f'in exceptions')
            # self.stop_script(self)

    # def stop_script(self):
    #     self.is_running = False
    #     self.status_label.config(text='Stopped')
    #     self.process.kill()


    def kill_script_button_impl(self):
        self.is_running = False
        self.process.terminate()
        self.parent.script_paths.remove(self.file_path)
        self.destroy()

    def script_death(self):
        print(f'Script Terminated Outside of manual KILL operation.')
        self.process.terminate()
        self.parent.script_paths.remove(self.file_path)
        self.destroy()

    def destroy(self):
        self.file_path_label.destroy()
        self.status_label.destroy()
        # self.stop_button.destroy()
        self.kill_button.destroy()