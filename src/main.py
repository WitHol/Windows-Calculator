import tkinter as tk
import tkinter.font as tkf

# Creating the window and configuring it
root = tk.Tk()
root.title("Windows calculator")
root.resizable(0,0)
root.geometry('400x500')

# Making it so t hat when the window is closed, the program ends
def closeWindow():
    root.destroy()
    exit(code=1)
root.protocol("WM_DELETE_WINDOW", closeWindow)

font = tkf.Font(family="Arial", size=14)

# All the buttons
buttonc = tk.Button(root, text="c", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button1 = tk.Button(root, text="1", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button2 = tk.Button(root, text="2", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button3 = tk.Button(root, text="3", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button4 = tk.Button(root, text="4", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button5 = tk.Button(root, text="5", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button6 = tk.Button(root, text="6", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button7 = tk.Button(root, text="7", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button8 = tk.Button(root, text="8", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button9 = tk.Button(root, text="9", width=2, height=2, font=font, bg='#333333', fg='#dddddd')
button0 = tk.Button(root, text="0", width=2, height=2, font=font, bg='#333333', fg='#dddddd')

buttonc.grid(column=1, row=1, sticky='NSEW', rowspan=3)
button1.grid(column=1, row=2, sticky='NSEW')
button2.grid(column=2, row=2, sticky='NSEW')
button3.grid(column=3, row=2, sticky='NSEW')
button4.grid(column=1, row=3, sticky='NSEW')
button5.grid(column=2, row=3, sticky='NSEW')
button6.grid(column=3, row=3, sticky='NSEW')
button7.grid(column=1, row=4, sticky='NSEW')
button8.grid(column=2, row=4, sticky='NSEW')
button9.grid(column=3, row=4, sticky='NSEW')
button0.grid(column=2, row=5, sticky='NSEW')

root.mainloop()