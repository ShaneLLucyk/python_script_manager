import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
text.pack()

# Add some text to the Text widget
text.insert(tk.END, "Hello, world!")

# Get the value of the Text widget
text_value = text.get("1.0", tk.END)

print(text_value)

root.mainloop()