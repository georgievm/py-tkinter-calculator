import tkinter as tk
from tkinter import messagebox as mb

# Custom Button class
class LargeButton(tk.Button):
    def __init__(self, master, color='grey', **kwargs):
        kwargs['width'] = 4
        kwargs['height'] = 2
        kwargs['font'] = "Helvetiva 22"
        kwargs['fg'] = 'white'
        kwargs['bg'] = "#f69906" if color == 'orange' else '#313131'
        super().__init__(master, **kwargs)

class Calculator:
    def __init__(self, master, title, icon_path):
        self.master = master
        master.title(title)
        master.iconbitmap(icon_path)
        master.resizable = (False, False)

        self.equation_text = ''
        self.equation_label = tk.StringVar()

        # Create widgets
        self.frame = tk.Frame(master, background='black')
        self.label = tk.Label(self.frame, textvariable=self.equation_label, font='Helvetica 32 bold', fg='white', bg='black', height=1, width="10", anchor='e')

        self.btn_ac = tk.Button(self.frame, text='AC', command=self.all_clear, bg='black', fg='red', font="Helvetica 15", border=0, height=1, width=6, activebackground='black', activeforeground='white')
        self.btn_back = tk.Button(self.frame, command=self.backspace, border=0, bg='black', fg="white", text="<", font='Helvetica 15 bold', width=6, activebackground='black', activeforeground='white')

        for i in range(10):
            exec(f'self.btn{i} = LargeButton(self.frame, text={i}, command=lambda self=self: self.btn_press({i}))')
        
        self.btn_decimal = LargeButton(self.frame, text='.', command=lambda: self.btn_press('.'))
        self.btn_plus = LargeButton(self.frame, text='+', command=lambda: self.btn_press('+'), color='orange')
        self.btn_minus = LargeButton(self.frame, text='-', command=lambda: self.btn_press('-'), color='orange')
        self.btn_multiply = LargeButton(self.frame, text='*', command=lambda: self.btn_press('*'), color='orange')
        self.btn_divide = LargeButton(self.frame, text='/', command=lambda: self.btn_press('/'), color='orange')
        self.btn_equal = LargeButton(self.frame, text='=', command=self.equals, color='orange')

        # Set Layout
        self.frame.pack()
        self.label.grid(row=0, column=0, columnspan=4, pady=10)
        # row 1
        self.btn_ac.grid(row=1, column=0, pady=12)
        self.btn_back.grid(row=1, column=3)
        # row 2
        self.btn7.grid(row=2, column=0)
        self.btn8.grid(row=2, column=1)
        self.btn9.grid(row=2, column=2)
        self.btn_divide.grid(row=2, column=3)
        # row 3
        self.btn4.grid(row=3, column=0)
        self.btn5.grid(row=3, column=1)
        self.btn6.grid(row=3, column=2)
        self.btn_multiply.grid(row=3, column=3)
        # row 4
        self.btn1.grid(row=4, column=0)
        self.btn2.grid(row=4, column=1)
        self.btn3.grid(row=4, column=2)
        self.btn_minus.grid(row=4, column=3)
        # row 5
        self.btn0.grid(row=5, column=0)
        self.btn_decimal.grid(row=5, column=1)
        self.btn_plus.grid(row=5, column=2)
        self.btn_equal.grid(row=5, column=3)

        # Key binding
        key_func = {
            '<Return>': 'self.equals',
            '<Escape>': 'self.all_clear',
            '<BackSpace>': 'self.backspace',
            '1': "lambda event: self.btn_press('1', event)"
        }
        for i in '0123456789+-*/.':
            key_func[i] = f'lambda event, self=self: self.btn_press({i!r}, event)'

        for key, func in key_func.items():
            eval(f'master.bind("{key}", {func})')
    
    def btn_press(self, key, event=None):
        self.equation_text += str(key)
        self.equation_label.set(self.equation_text)

    def equals(self, event=None):
        if self.equation_text:
            try:
                total = str(eval(self.equation_text))
            except ZeroDivisionError:
                mb.showerror('Error', f'{"Cannot divide by zero!":^30}')
            except SyntaxError:
                mb.showerror('Error', f'{"Invalid format!":^30}')
            else:
                self.equation_text = total
                self.equation_label.set(total)

    def all_clear(self, event=None):
        self.equation_text = ''
        self.equation_label.set(self.equation_text)

    def backspace(self, event=None):
        self.equation_text = self.equation_text[:-1]
        self.equation_label.set(self.equation_text)

def main():
    root = tk.Tk()
    calculator = Calculator(root, 'Calculator', 'icon.ico')
    root.mainloop()

if __name__ == '__main__':
    main()