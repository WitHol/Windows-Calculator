import tkinter as tk
import tkinter.font as tkf

# Creating the window and configuring it
root = tk.Tk()
root.title("Windows calculator")
root.resizable(0,0)
root.geometry('400x500')
root.config(bg="#444444")

# Making it so t hat when the window is closed, the program ends
def closeWindow():
    root.destroy()
    exit(code=1)
root.protocol("WM_DELETE_WINDOW", closeWindow)

# Fonts
buttonFont = tkf.Font(family="Arial", size=50)
textFont = tkf.Font(family="Arial", size=50)

# An image, to make the buttons square
image = tk.PhotoImage(width=6, height=1)


#
text = tk.Text(root, width=10, height=1, font=textFont, bg="#444444", fg='#cccccc', border = 0)

# All the buttons
button_1 = tk.Button(root, image=image, compound='c', text="1", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_2 = tk.Button(root, image=image, compound='c', text="2", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_3 = tk.Button(root, image=image, compound='c', text="3", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_4 = tk.Button(root, image=image, compound='c', text="4", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_5 = tk.Button(root, image=image, compound='c', text="5", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_6 = tk.Button(root, image=image, compound='c', text="6", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_7 = tk.Button(root, image=image, compound='c', text="7", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_8 = tk.Button(root, image=image, compound='c', text="8", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_9 = tk.Button(root, image=image, compound='c', text="9", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_0 = tk.Button(root, image=image, compound='c', text="0", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_dot = tk.Button(root, image=image, compound='c', text=".", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_equal = tk.Button(root, image=image, compound='c', text="=", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_addition = tk.Button(root, image=image, compound='c', text="+", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_substraction = tk.Button(root, image=image, compound='c', text="-", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_multiplication = tk.Button(root, image=image, compound='c', text="×", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)
button_division = tk.Button(root, image=image, compound='c', text="÷", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5)

text.grid(column=1, row=1, columnspan=4, pady=11, sticky="e")

button_1.grid(column=1, row=2)
button_2.grid(column=2, row=2)
button_3.grid(column=3, row=2)
button_division.grid(column=4, row=2)

button_4.grid(column=1, row=3)
button_5.grid(column=2, row=3)
button_6.grid(column=3, row=3)
button_multiplication.grid(column=4, row = 3)

button_7.grid(column=1, row=4)
button_8.grid(column=2, row=4)
button_9.grid(column=3, row=4)
button_substraction.grid(column=4, row=4)

button_dot.grid(column=1, row=5)
button_0.grid(column=2, row=5)
button_equal.grid(column=3, row=5)
button_addition.grid(column=4, row=5)

root.mainloop()