from tkinter import *
from tkinter import messagebox

# Main functions

def btn_press(key, event=None):
    global equation_text
    equation_text += str(key)
    equation_label.set(equation_text)

def equals(event=None):
    global equation_text
    try:
        total = str(eval(equation_text))
    except ZeroDivisionError:
        show_message('ArithmeticError', 'Cannot divide by zero!')
    except SyntaxError:
        show_message('ArithmeticError', 'Invalid format!')
    else:
        equation_text = total
        equation_label.set(total)

def all_clear(event=None):
    global equation_text
    equation_text = ''
    equation_label.set(equation_text)

def backspace(event=None):
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

def show_message(title, msg):
    messagebox.showerror(title, f'{msg:^30}')

# Configure new window
window = Tk()
window.title("Calculator")
window.iconbitmap('icon.ico')
window.resizable(False, False)

equation_text = ''
equation_label = StringVar()

frame = Frame(window, background='black')
frame.pack()

# row 0
label = Label(frame, textvariable=equation_label, font='Helvetica 32 bold', fg='white', bg='black', height=1, width="10", anchor='e')
label.grid(row=0, column=0, columnspan=4, pady=10)

# row 1
btn_ac = Button(frame, text='AC', command=all_clear, bg='black', fg='red', font="Helvetica 15", border=0, height=1, width=6, activebackground='black', activeforeground='white')
btn_ac.grid(row=1, column=0, pady=12)
btn_back = Button(frame, command=backspace, border=0, bg='black', fg="white", text="<", font='Helvetica 15 bold', width=6, activebackground='black', activeforeground='white')
btn_back.grid(row=1, column=3)

# row 2
btn7 = Button(frame, text=7, command=lambda: btn_press(7))
btn7.grid(row=2, column=0)
btn8 = Button(frame, text=8, command=lambda: btn_press(8))
btn8.grid(row=2, column=1)
btn9 = Button(frame, text=9, command=lambda: btn_press(9))
btn9.grid(row=2, column=2)
btn_divide = Button(frame, text='/', command=lambda: btn_press('/'))
btn_divide.grid(row=2, column=3)

# row 3
btn4 = Button(frame, text=4, command=lambda: btn_press(4))
btn4.grid(row=3, column=0)
btn5 = Button(frame, text=5, command=lambda: btn_press(5))
btn5.grid(row=3, column=1)
btn6 = Button(frame, text=6, command=lambda: btn_press(6))
btn6.grid(row=3, column=2)
btn_multiply = Button(frame, text='*', command=lambda: btn_press('*'))
btn_multiply.grid(row=3, column=3)

# row 4
btn1 = Button(frame, text=1, command=lambda: btn_press(1))
btn1.grid(row=4, column=0)
btn2 = Button(frame, text=2, command=lambda: btn_press(2))
btn2.grid(row=4, column=1)
btn3 = Button(frame, text=3, command=lambda: btn_press(3))
btn3.grid(row=4, column=2)
btn_minus = Button(frame, text='-', command=lambda: btn_press('-'))
btn_minus.grid(row=4, column=3)

# row 5
btn0 = Button(frame, text=0, command=lambda: btn_press(0))
btn0.grid(row=5, column=0)
btn_decimal = Button(frame, text='.', command=lambda: btn_press('.'))
btn_decimal.grid(row=5, column=1)
btn_plus = Button(frame, text='+', command=lambda: btn_press('+'))
btn_plus.grid(row=5, column=2)
btn_equal = Button(frame, text='=', command=equals)
btn_equal.grid(row=5, column=3)

# Styling
orange_gr = ['btn_plus', 'btn_minus', 'btn_multiply', 'btn_divide', 'btn_equal']
grey_gr = [f'btn{i}' for i in range(10)] + ['btn_decimal']

for i in orange_gr + grey_gr:
    eval(f'{i}.config(width=4, height=2, font="Helvetiva 22", fg="#ffffff")')
for i in orange_gr:
    eval(f'{i}.config(bg="#f69906")')
for i in grey_gr:
    eval(f'{i}.config(bg="#313131")')

# Key binding
key_func = {'<Return>': 'equals', '<Escape>': 'all_clear', '<BackSpace>': 'backspace'}
for i in '0123456789+-*/.':
    key_func[i] = f'lambda event:btn_press({i!r}, event)'

for key, func in key_func.items():
    eval(f'window.bind("{key}", {func})')

window.mainloop()