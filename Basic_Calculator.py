import math
from tkinter import *

obj = Tk()
expression = ''


class Calculator:

    def __int__(self):
        self.q = 0

    @staticmethod
    def press(num):
        # point out the global expression variable
        global expression
        # concatenation of string
        expression = expression + str(num)
        # update the expression by using set method
        default_text.set(expression)

    @staticmethod
    def clear():
        global expression
        expression = ''
        default_text.set(expression)

    @staticmethod
    def backspace():
        global expression
        expression = expression[:(len(expression) - 1)]
        default_text.set(expression)

    @staticmethod
    def equal_press():
        global expression
        for i in range(len(expression) - 1):
            if expression[0] == '0':
                if expression[i] == '0' and expression[i + 1] != '0':
                    expression = expression[i + 1:]
            else:
                break
        try:
            total = str(eval(expression))
            expression = total
            default_text.set(expression)

        except:
            default_text.set("✖‿✖")
            expression = ''

    @staticmethod
    def square_root():
        global expression
        try:
            n = float(expression)
            if n < 0:
                expression = 'Math Error'
            else:
                expression = str(math.sqrt(float(expression)))
        except:
            expression = ' '
        default_text.set(expression)

    @staticmethod
    def square():
        global expression
        try:
            n = float(expression)
            expression = str(math.pow(n, 2))
        except:
            expression = ' '
        default_text.set(expression)

    @staticmethod
    def cube_root():
        global expression
        try:
            n = float(expression)
            if n < 0:
                expression = str((-1) * (math.pow((n * -1), (1.0 / 3))))
            else:
                expression = str((math.pow(n, (1.0 / 3))))
        except:
            expression = ' '
        default_text.set(expression)

    @staticmethod
    def cube():
        global expression
        try:
            n = float(expression)
            expression = str(math.pow(n, 3))
        except:
            expression = ' '
        default_text.set(expression)


if __name__ == "__main__":
    obj.geometry("565x365")
    obj.config(bg="#C6E6FB")
    obj.resizable(0, 0)
    obj.title("Calculator")

    default_text = StringVar()
    default_text.set('0')
    Entry(obj, state=DISABLED, bg='White', fg='black', font=('Times New Roman', 31), textvariable=default_text,
          justify='right', xscrollcommand=20,
          bd=8, relief=SUNKEN, width=24).place(x=21, y=15)
    icon = PhotoImage(file="Calcu.png")
    obj.iconphoto(True, icon)

    button1 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='1', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(1)).place(x=23, y=90)
    button2 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='2', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(2)).place(x=99, y=90)
    button3 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='3', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(3)).place(x=175., y=90)
    button4 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='4', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(4)).place(x=251, y=90)
    button5 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='5', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(5)).place(x=327, y=90)

    add_button = Button(obj, relief=GROOVE, bg="#6BCAE2", font=("Times New Roman", 16, 'bold'), text='+', height=4,
                        width=5, command=lambda: Calculator().press('+')).place(x=403, y=90)
    sub_button = Button(obj, relief=GROOVE, bg="#6BCAE2", font=("Times New Roman", 16, 'bold'), text='-', height=4,
                        width=5, command=lambda: Calculator().press('-')).place(x=474, y=90)

    button6 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='6', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(6)).place(x=23, y=141)
    button7 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='7', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(7)).place(x=99, y=141)
    button8 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='8', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(8)).place(x=175, y=141)
    button9 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='9', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(9)).place(x=251, y=141)
    button0 = Button(obj, relief=GROOVE, bg="#AFEEEE", fg="black", text='0', height=2, width=6,
                     font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().press(0)).place(x=327, y=141)

    button00 = Button(obj, relief=GROOVE, bg="#AFDBF5", fg="black", text='00', height=1, width=6,
                      font=("Times New Roman Bold", 14, 'bold'), command=lambda: Calculator().press('00')).place(x=23,
                                                                                                                 y=195)
    dot_button = Button(obj, relief=GROOVE, bg="#AFDBF5", fg="black", text='.', height=1, width=6,
                        font=("Times New Roman Bold", 14, 'bold'), command=lambda: Calculator().press('.')).place(x=99,
                                                                                                                  y=195)

    first_bracket_open_button = Button(obj, relief=GROOVE, bg="#AFDBF5", fg="black", text='(', height=1, width=6,
                                       font=("Times New Roman", 14, 'bold'),
                                       command=lambda: Calculator.press("(")).place(x=175, y=195)
    second_bracket_close_button = Button(obj, relief=GROOVE, bg="#AFDBF5", fg="black", text=')', height=1, width=6,
                                         font=("Times New Roman", 14, 'bold'),
                                         command=lambda: Calculator.press(")")).place(x=251, y=195)

    pi = math.pi
    pi_button = Button(obj, relief=GROOVE, bg="#AFDBF5", fg="black", text='π', height=1, width=6,
                       font=("Times New Roman", 14, 'bold'), command=lambda: Calculator.press(pi)).place(x=327, y=195)

    backspace_button = Button(obj, relief=GROOVE, bg="#AFDBF5", fg="black", text='⌂ DEL', height=1, width=5,
                              font=("Times New Roman Bold", 16, 'bold'), command=lambda: Calculator.backspace()).place(
        x=403, y=194)
    clear_button = Button(obj, relief=GROOVE, bg="#AFDBF5", fg="black", text='C', height=1, width=5,
                          font=("Times New Roman", 16, 'bold'), command=lambda: Calculator().clear()).place(x=474,
                                                                                                            y=194)

    to_the_power_button = Button(obj, relief=GROOVE, bg="#AFD8F5", fg="black", text='^', height=2, width=6,
                                 font=("Times New Roman", 14, 'bold bold bold'),
                                 command=lambda: Calculator.press('**')).place(x=23, y=236)
    square_button = Button(obj, relief=GROOVE, bg="#AFD8F5", fg="black", text='x\u00b2', height=2, width=6,
                           font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().square()).place(x=99,
                                                                                                              y=236)
    cube_button = Button(obj, relief=GROOVE, bg="#AFD8F5", fg="black", text='x\u00b3', height=2, width=6,
                         font=("Times New Roman", 14, 'bold'), command=lambda: Calculator().cube()).place(x=175, y=236)
    sqrt_button = Button(obj, relief=GROOVE, bg="#AFD8F5", fg="black", text='√', height=2, width=6,
                         font=("Times New Roman", 14, 'bold bold'), command=lambda: Calculator().square_root()).place(
        x=251, y=236)
    cubert_button = Button(obj, relief=GROOVE, bg="#AFD8F5", fg="black", text='∛', height=2, width=6,
                           font=("Times New Roman", 14, 'bold'), command=lambda: Calculator.cube_root()).place(x=327,
                                                                                                               y=236)

    equal_button = Button(obj, relief=GROOVE, bg="#6BCAE2", fg="black", text='=', height=3, width=53,
                          font=("Times New Roman", 10, 'bold'), command=lambda: Calculator().equal_press()).place(x=23,
                                                                                                                  y=294)

    mul_button = Button(obj, relief=GROOVE, bg="#6BCAE2", text='*', font=("Times New Roman", 16, 'bold'), height=4,
                        width=5, command=lambda: Calculator().press('*')).place(x=403, y=236)
    div_button = Button(obj, relief=GROOVE, bg="#6BCAE2", text='/', font=("Times New Roman", 16, 'bold'), height=4,
                        width=5, command=lambda: Calculator().press('/')).place(x=474, y=236)
    obj.mainloop()
