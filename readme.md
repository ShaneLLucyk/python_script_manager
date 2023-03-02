# Python Script Manager

The basic functionality of this project is to allow a central portal for managing a large number of python scripts at the same time. I build this program because i was sick of having to keep track of the million python scripts i use for automation on my media & home automation server.

## Starting Script:
To start the script, run the `script_manager.py` file. This will open the script window.

![Script Window](/assets/images/script_window.png)

Once the script window is open, you can add a script to manage by selecting its file using the 'Select Python Script Button'. This will open up your default file explorer's window and allow you to select a script.

![Script Selection](/assets/images/script_selection.png)


Once a script is chosen, the system will add an entry to the scripts table. This will have the following:
- The script file name
- A status (running, stopped, error, etc)
- A button to open the logs folder (if one exists, if not it opens the file path)
- A button to kill the scripts process.


![Running Script](/assets/images/running_script.png)

## Dependency List
There are currently no dependencies outside of the standard python library. Nothing to Install. I will add a requirements.txt if any other libraries end up being used.