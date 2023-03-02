import tkinter as tk
from tkinter import filedialog, ttk
from Script import Script


class Application():
    def __init__(self):
        self.scripts = []
        self.script_paths = []
        self.active_log_script = None
        self.create_widgets()
    ### --- Logs Scheduler Not Implemented! IGNORE ME! -- ###
        # self.log_scheduler = BackgroundScheduler(daemon=True)
        # self.log_scheduler.add_job(lambda : self.log_updater(),'interval',seconds=5)
        # self.log_scheduler.start()

    def create_widgets(self):
        """_summary_
        """
        self.root = tk.Tk()
        self.root.title("Python Script Log Viewer")
        self.root.minsize(250, 500)
        self.root.wm_state('iconic')
        self.root.wm_iconbitmap('./assets/images/fire.ico')

        self.tab_controller = ttk.Notebook(self.root)
        self.scripts_view = tk.Frame(self.tab_controller)
        self.logs_view = tk.Frame(self.tab_controller)
        self.generate_scripts_view()
        # self.generate_log_view()

        # Expand Controller to fill all of window
        self.tab_controller.pack(expand=1, fill="both")

    ### --- Log View Disabled. IGNORE ME! -- ###
    # def generate_log_view(self):
    #     #Frame Details for Console Output
    #     self.logs_view.logs_text = tk.Text(self.logs_view)
    #     self.logs_view.logs_text.pack(side='top', padx=10, pady=10)
    #     self.logs_view.logs_text.insert(tk.END, "Please Select a Script & Activate Logging.")
    #     self.logs_view.logs_text.configure(state='disabled')
    #     self.tab_controller.add(self.logs_view, text='Logs')

    def generate_scripts_view(self):
        """_summary_
        """
        # Frame Details for Script Selection & Table
        self.scripts_view.button_select = tk.Button(
            self.scripts_view, text='Select Python Script', command=self.select_script)
        self.scripts_view.button_select.pack(side="bottom", pady=25)
        self.scripts_view.table = tk.Frame(self.scripts_view, bd=2, bg='white')
        self.scripts_view.table.pack(side="top", padx=10, pady=10)
        tk.Label(self.scripts_view.table, text="Script Path", font="TkDefaultFont 9 bold").grid(
            row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.scripts_view.table, text="Status", font="TkDefaultFont 9 bold").grid(
            row=0, column=1, padx=10, pady=5, sticky="w")
        tk.Label(self.scripts_view.table, text="Status", font="TkDefaultFont 9 bold").grid(
            row=0, column=2, padx=10, pady=5, sticky="w")
        tk.Label(self.scripts_view.table, text="Kill Script", font="TkDefaultFont 9 bold").grid(
            row=0, column=3, padx=10, pady=5, sticky="w")
        self.tab_controller.add(self.scripts_view, text='Scripts')

    def select_script(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Python files", "*.py")])
        
        if file_path is None or file_path == '' or file_path in self.script_paths:
            return
        
        print(f"Starting script: {file_path}")
        self.script_paths.append(file_path)
        script = Script(file_path, self)
        self.scripts.append(script)

    def start(self):
        # Run the Tkinter event loop
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()
    app.start()
