from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, root, title, icon_path):
        self.root = root
        self.root.title(title)
        self.root.iconbitmap(icon_path)
        self.root.resizable = (False, False)

        self.equation_text = ''
        self.equation_label = StringVar()

        frame = Frame(root, background='black')
        frame.pack()

        # row 0
        self.label = Label(frame, textvariable=self.equation_label, font='Helvetica 32 bold', fg='white', bg='black', height=1, width="10", anchor='e')
        self.label.grid(row=0, column=0, columnspan=4, pady=10)

        # row 1
        self.btn_ac = Button(frame, text='AC', command=self.all_clear, bg='black', fg='red', font="Helvetica 15", border=0, height=1, width=6, activebackground='black', activeforeground='white')
        self.btn_ac.grid(row=1, column=0, pady=12)
        self.btn_back = Button(frame, command=self.backspace, border=0, bg='black', fg="white", text="<", font='Helvetica 15 bold', width=6, activebackground='black', activeforeground='white')
        self.btn_back.grid(row=1, column=3)

        # row 2
        self.btn7 = Button(frame, text=7, command=lambda: self.btn_press(7))
        self.btn7.grid(row=2, column=0)
        self.btn8 = Button(frame, text=8, command=lambda: self.btn_press(8))
        self.btn8.grid(row=2, column=1)
        self.btn9 = Button(frame, text=9, command=lambda: self.btn_press(9))
        self.btn9.grid(row=2, column=2)
        self.btn_divide = Button(frame, text='/', command=lambda: self.btn_press('/'))
        self.btn_divide.grid(row=2, column=3)

        # row 3
        self.btn4 = Button(frame, text=4, command=lambda: self.btn_press(4))
        self.btn4.grid(row=3, column=0)
        self.btn5 = Button(frame, text=5, command=lambda: self.btn_press(5))
        self.btn5.grid(row=3, column=1)
        self.btn6 = Button(frame, text=6, command=lambda: self.btn_press(6))
        self.btn6.grid(row=3, column=2)
        self.btn_multiply = Button(frame, text='*', command=lambda: self.btn_press('*'))
        self.btn_multiply.grid(row=3, column=3)

        # row 4
        self.btn1 = Button(frame, text=1, command=lambda: self.btn_press(1))
        self.btn1.grid(row=4, column=0)
        self.btn2 = Button(frame, text=2, command=lambda: self.btn_press(2))
        self.btn2.grid(row=4, column=1)
        self.btn3 = Button(frame, text=3, command=lambda: self.btn_press(3))
        self.btn3.grid(row=4, column=2)
        self.btn_minus = Button(frame, text='-', command=lambda: self.btn_press('-'))
        self.btn_minus.grid(row=4, column=3)

        # row 5
        self.btn0 = Button(frame, text=0, command=lambda: self.btn_press(0))
        self.btn0.grid(row=5, column=0)
        self.btn_decimal = Button(frame, text='.', command=lambda: self.btn_press('.'))
        self.btn_decimal.grid(row=5, column=1)
        self.btn_plus = Button(frame, text='+', command=lambda: self.btn_press('+'))
        self.btn_plus.grid(row=5, column=2)
        self.btn_equal = Button(frame, text='=', command=self.equals)
        self.btn_equal.grid(row=5, column=3)

        self.style_buttons()
        self.key_bind()
        self.root.mainloop()
    
    def btn_press(self, key, event=None):
        self.equation_text += str(key)
        self.equation_label.set(self.equation_text)

    def equals(self, event=None):
        try:
            total = str(eval(self.equation_text))
        except ZeroDivisionError:
            self.show_message('ArithmeticError', 'Cannot divide by zero!')
        except SyntaxError:
            self.show_message('ArithmeticError', 'Invalid format!')
        else:
            self.equation_text = total
            self.equation_label.set(total)

    def all_clear(self, event=None):
        self.equation_text = ''
        self.equation_label.set(self.equation_text)

    def backspace(self, event=None):
        self.equation_text = self.equation_text[:-1]
        self.equation_label.set(self.equation_text)

    def show_message(self, title, msg):
        messagebox.showerror(title, f'{msg:^30}')

    def key_bind(self):
        key_func = {'<Return>': 'self.equals', '<Escape>': 'self.all_clear', '<BackSpace>': 'self.backspace', '1': "lambda event: self.btn_press('1', event)"}
        for i in '0123456789+-*/.':
            key_func[i] = f'lambda event, self=self: self.btn_press({i!r}, event)'

        for key, func in key_func.items():
            eval(f'root.bind("{key}", {func})')

    def style_buttons(self):
        orange_gr = ['btn_plus', 'btn_minus', 'btn_multiply', 'btn_divide', 'btn_equal']
        grey_gr = [f'btn{i}' for i in range(10)] + ['btn_decimal']

        for i in orange_gr + grey_gr:
            eval(f'self.{i}.config(width=4, height=2, font="Helvetiva 22", fg="#ffffff")')
        for i in orange_gr:
            eval(f'self.{i}.config(bg="#f69906")')
        for i in grey_gr:
            eval(f'self.{i}.config(bg="#313131")')

if __name__ == '__main__':
    calculator = App(root := Tk(), 'Calculator', 'icon.ico')