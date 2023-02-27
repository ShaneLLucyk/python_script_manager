import subprocess
import threading
import tkinter as tk
import os
from tkinter import filedialog
import sys

from collections import deque

class Script:
    def __new__(cls, file_path, parent):
        self = super().__new__(cls)
        self.file_path = file_path
        self.am_logging = False
        self.parent = parent
        self.parent.scripts_view.table.row = len(self.parent.scripts) + 1
        self.row = len(self.parent.scripts) + 1

        self.file_name = (self.file_path.split('/')[-1]).replace('.py', '')
        self.working_directory = self.file_path.replace((self.file_path.split('/')[-1]), '')

        self.file_path_label = tk.Label(self.parent.scripts_view.table, text=self.file_name, font="TkDefaultFont 9")
        self.file_path_label.grid(row=self.row, column=0, padx=10, pady=5, sticky="w")

        self.status_label = tk.Label(self.parent.scripts_view.table, text="Running", font="TkDefaultFont 9")
        self.status_label.grid(row=self.row, column=1, padx=10, pady=5, sticky="w")

        self.log_button = tk.Button(self.parent.scripts_view.table, text="Open Logs Folder", font="TkDefaultFont 9", command=self.open_logs)
        self.log_button.grid(row=self.row, column=2, padx=10, pady=5, sticky="w")

        self.kill_button = tk.Button(self.parent.scripts_view.table, text="Kill", font="TkDefaultFont 9", command=self.kill_script_button_impl)
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


    def open_logs(self):
        folder_path = self.file_path.replace(self.file_path.split('/')[-1], "")
        if os.path.exists(folder_path + '/' + 'logs'):
            folder_path = folder_path + '/' + 'logs'
        if sys.platform=='win32':
            subprocess.Popen(['start', folder_path], shell= True)
        elif sys.platform =='darwin':
            subprocess.Popen(['open', d])
        else:
            try:
                subprocess.Popen(['xdg-open', d])
            except OSError as e:
                print(f'COULD NOT OPEN LOG FILES DUE TO {e}')

    # def update_text(self):
    #     lines = deque(maxlen=25)
    #     stdout, _ = self.process.communicate()
    #     for line in stdout.decode().splitlines():
    #         lines.append(line.strip())
    #     text_content= '\n'.join(lines)
    #     self.update_log_text(text_content)   

    # def enable_logging(self):
    #     print(f'{self.file_path}\'s log button was clicked.')
    #     #Steps:
    #     # if Parent Active Log Script is not None:
    #         #Turn off Am_Logger on Active Script.
    #         #Enable Button for Active Script
    #     #Disable button for SELF
    #     #Set Active_Parent_Log_Script to self
    #     if self.parent.active_log_script is not None:
    #         print(f'Active Script was not None.')
    #         print(f'Setting {self.parent.active_log_script.file_path} Logging off.')
    #         self.parent.active_log_script.am_logger_script = False
    #         self.parent.active_log_script.log_button['state']='active'
    #     else:
    #         print(f'Active Script was None.')
    #     self.log_button['state']='disabled'
    #     self.am_logging = True
    #     self.parent.active_log_script = self

    # def update_log_text(self, updated_text):
    #     self.parent.logs_view.logs_text.configure(state='normal')    
    #     self.parent.logs_view.logs_text.delete("1.0", tk.END)
    #     self.parent.logs_view.logs_text.insert(tk.END, f'{updated_text}')
    #     self.parent.logs_view.logs_text.configure(state='disabled')

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
        self.log_button.destroy()
        # self.stop_button.destroy()
        self.kill_button.destroy()