import tkinter as tk

# Creating the window and configuring it
root = tk.Tk()
root.title("Windows calculator")
root.resizable(0,0)
root.geometry('377x610') # golden ratio

button1 = tk.Button(root, text="1", width=100, height=20)
#button1.grid(column=1, row=2)