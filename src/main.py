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
textFont = tkf.Font(family="Arial", size=37)

# An image, to make the buttons square
image = tk.PhotoImage(width=6, height=1)

# text
global text
text = tk.Text(root, width=10, height=1, font=textFont, bg="#444444", fg='#cccccc', border = 0,  state="disabled",)
text.insert(1.0, '          ')
maxTextLength = 10

def addChar(char):
    global text
    print('1')
    #if(text.get(tk.INSERT) != ' '): return None
    print('2')
    text.delete(tk.INSERT)
    print('3')
    text.insert(tk.END, char)
    print('4')
    print(text.get(tk.INSERT, tk.END))
    print("x")

def remove_char():
    global text
    text.delete(tk.END)
    text.insert(tk.INSERT, ' ')
    print(text.get(1.0, tk.END))

def count():
    global text
    text.insert(tk.END, str(eval(text.get(tk.INSERT, tk.END))))
    text.delete(tk.INSERT, '1.10')
    print(text.get(tk.INSERT, tk.END))

def add_1(): addChar('1')
def add_2(): addChar('2')
def add_3(): addChar('3')
def add_4(): addChar('4')
def add_5(): addChar('5')
def add_6(): addChar('6')
def add_7(): addChar('7')
def add_8(): addChar('8')
def add_9(): addChar('9')
def add_0(): addChar('0')
def add_dot(): addChar('.')
def add_addition(): addChar('+')
def add_substraction(): addChar('-')
def add_multiplication(): addChar('*')
def add_division(): addChar('/')


# All the buttons
button_1 = tk.Button(root, image=image, compound='c', text="1", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_1)
button_2 = tk.Button(root, image=image, compound='c', text="2", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_2)
button_3 = tk.Button(root, image=image, compound='c', text="3", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_3)
button_4 = tk.Button(root, image=image, compound='c', text="4", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_4)
button_5 = tk.Button(root, image=image, compound='c', text="5", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_5)
button_6 = tk.Button(root, image=image, compound='c', text="6", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_6)
button_7 = tk.Button(root, image=image, compound='c', text="7", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_7)
button_8 = tk.Button(root, image=image, compound='c', text="8", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_8)
button_9 = tk.Button(root, image=image, compound='c', text="9", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_9)
button_0 = tk.Button(root, image=image, compound='c', text="0", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_0)
button_dot = tk.Button(root, image=image, compound='c', text=".", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_dot)
button_backspace = tk.Button(root, image=image, compound='c', text="←", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=remove_char)
button_equal = tk.Button(root, image=image, compound='c', text="=", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=count)
button_addition = tk.Button(root, image=image, compound='c', text="+", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_addition)
button_substraction = tk.Button(root, image=image, compound='c', text="-", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_substraction)
button_multiplication = tk.Button(root, image=image, compound='c', text="*", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_multiplication)
button_division = tk.Button(root, image=image, compound='c', text="/", width=86, height=86, font=buttonFont, bg="#444444", fg='#dddddd', border=5, command=add_division)

text.grid(column=1, row=1, columnspan=3, pady=11, sticky="e")
button_equal.grid(column=4, row=1)

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
button_backspace.grid(column=3, row=5)
button_addition.grid(column=4, row=5)

# Loop
root.mainloop()