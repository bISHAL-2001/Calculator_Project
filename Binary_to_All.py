from tkinter import *

o = Tk()
expression = ' '


class conversion:
    def __init__(self):
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
    def bin_to_oct():
        global expression
        try:
            expression = str(oct(int(expression, 2)))[2:]
            expression = expression.upper()
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def bin_to_dec():
        global expression
        try:
            expression = str(int(expression, 2))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def bin_to_hex():
        global expression
        try:
            expression = str(hex(int(expression, 2)))[2:]
            expression = expression.upper()
        except:
            expression = 'Math Error'
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


if __name__ == '__main__':

    o.title('Binary → All')
    o.iconphoto(True, PhotoImage(file='binary.png'))
    o.geometry('550x440')
    o.config(bg='#6CB4EE')
    o.resizable(0, 0)

    default_text = StringVar()
    default_text.set('0')
    Entry(o, state=DISABLED, bd=12, textvariable=default_text, justify='right', font=('Times New Roman', 31, 'bold'), width=24).place(x=10, y=10)

    b0 = Button(o, text='0', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), height=1, width=15, command=lambda: conversion().press('0')).place(x=10, y=90)
    b1 = Button(o, text='1', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), height=1, width=15, command=lambda: conversion().press('1')).place(x=274, y=90)

    bin_to_dec_button = Button(o, bg='#B9D9EB', text='Bin → Oct', relief=GROOVE, font=("Times New Roman", 20, 'bold'), height=1, width=32, bd=6, command=lambda: conversion().bin_to_oct()).place(x=10, y=170)
    bin_to_hex_button = Button(o, bg='#B9D9EB', text='Bin → Dec', relief=GROOVE, font=("Times New Roman", 20, 'bold'), height=1, width=32, bd=6, command=lambda: conversion().bin_to_dec()).place(x=10, y=230)
    bin_to_oct_button = Button(o, bg='#B9D9EB', text='Bin → Hex', relief=GROOVE, font=("Times New Roman", 20, 'bold'), height=1, width=32, bd=6, command=lambda: conversion().bin_to_hex()).place(x=10, y=290)

    clear_button = Button(o, text='C', relief=RAISED, font=("Times New Roman", 21, 'bold'), height=1, width=15, bd=1, command=lambda: conversion().clear()).place(x=10, y=370)
    backspace_button = Button(o, text='←', relief=RAISED, font=("Times New Roman", 21, 'bold'), height=1, width=15, bd=1, command=lambda: conversion().backspace()).place(x=274, y=370)
    o.mainloop()
