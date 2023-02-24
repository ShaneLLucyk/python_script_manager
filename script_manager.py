import tkinter as tk
from tkinter import filedialog, ttk
import subprocess
import threading
import os
import signal

class LogThread(threading.Thread):
    def __init__(self, process, text_widget):
        threading.Thread.__init__(self)
        self.process = process
        self.text_widget = text_widget
        self.stopped = False

    def stop(self):
        # Set the stopped flag to true
        self.stopped = True

        # Terminate the process
        self.process.terminate()

    def run(self):
        while not self.stopped:
            line = self.process.stdout.readline().decode()
            if not line:
                break
            self.text_widget.insert("end", line)

            # Scroll to the end of the text box
            self.text_widget.see("end")

        while not self.stopped:
            line = self.process.stderr.readline().decode()
            if not line:
                break
            self.text_widget.insert("end", line)

            # Scroll to the end of the text box
            self.text_widget.see("end")

class LogViewer:
        def __init__(self):
                # Create the Tkinter window
                self.root = tk.Tk()
                self.root.title("Python Script Log Viewer")
                self.root.wm_state('iconic')
                self.root.wm_iconbitmap('./configuration/fire.ico')
                # Create the menu bar
                self.menu_bar = tk.Menu(self.root)

                # Create the File menu
                self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
                self.file_menu.add_command(label="Minimize", command=self.root.wm_iconify)
                self.file_menu.add_separator()
                self.file_menu.add_command(label="Close", command=self.root.destroy)
                self.menu_bar.add_cascade(label="File", menu=self.file_menu)

                # Add the menu bar to the window
                self.root.config(menu=self.menu_bar)

                # Create a button to open the file dialog and select a Python script
                self.open_button = tk.Button(self.root, text="Select Python Script", command=self.open_file)
                self.open_button.pack(pady=10)

                # Create a label to display the PID of the selected Python script
                self.pid_label = tk.Label(self.root, text="")
                self.pid_label.pack(pady=10)

                # Create a text box to display the logs of the selected script
                self.log_text = tk.Text(self.root, wrap="word", width=80, height=20)
                self.log_text.pack(fill="both", expand=True)

                # # Create a button to stop the selected Python script
                # self.stop_button = tk.Button(self.root, text="Stop Script", command=self.stop_script, state="disabled")
                # self.stop_button.pack(pady=10)

        def open_file(self):
                file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
                if file_path:
                        self.run_script(file_path)

        def run_script(self, file_path):
                # Disable the "Select Python Script" button
                self.open_button.config(state="disabled")

                # Create a button to stop the selected Python script
                # stop_button = tk.Button(tab, text="Stop Script", command=lambda: self.stop_script(process, log_thread, stop_button, tab), state="disabled")


                # self.stop_button = tk.Button(text="Stop Script", command=lambda: self.stop_script(process, log_thread), state="disabled")
                # self.stop_button.pack(pady=10)

                # Create a subprocess to run the selected Python script
                process = subprocess.Popen(["python", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
                print(f'{process.pid}')
                # Start a thread to read the logs of the subprocess and display them in the text box
                log_thread = LogThread(process, self.log_text)
                log_thread.start()

                self.stop_button = tk.Button(text="Stop Script", command=lambda: self.stop_script(process, log_thread), state="normal")
                self.stop_button.pack(pady=10)

                # Update the PID label with the PID of the subprocess
                # pid_label.config(text="Process ID: {}".format(process.pid))
                self.pid_label.config(text="Process ID: {}".format(process.pid))

                # Enable the "Stop Script" button
                # stop_button.config(state="normal")
                self.stop_button.config(state="normal")

        # def stop_script(self, process, log_thread, stop_button, tab):
        def stop_script(self, process, log_thread):

                # Send a signal to the subprocess to terminate it
                
                # process.terminate()
                print(process.pid)
                os.kill(process.pid, signal.SIGINT)

                # # Wait for the subprocess to terminate and get its return code
                # return_code = process.wait()

                # # Join the log thread to wait for it to finish
                # log_thread.join()

                # Disable the "Stop Script" button
                # stop_button.config(state="disabled")
                self.stop_button.config(state="disabled")

                # Enable the "Select Python Script" button
                self.open_button.config(state="normal")

                # Display the return code of the subprocess in the log text box
                log_thread.log("Script exited with return code {}\n".format(return_code))

                # # Close the current tab
                # self.tab_bar.forget(tab)
                


        def start(self):
                # Run the Tkinter event loop
                self.root.mainloop()

if __name__ == "__main__":
        log_viewer = LogViewer()
        log_viewer.start()
