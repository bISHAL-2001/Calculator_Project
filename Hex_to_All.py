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
    def hex_to_bin():
        global expression
        try:
            expression = str(bin(int(expression.lower(), 16)))[2:]
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def hex_to_oct():
        global expression
        try:
            expression = str(oct(int(expression.lower(), 16)))[2:]
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def hex_to_dec():
        global expression
        try:
            expression = str(int(expression.lower(), 16))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

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

    o.title('Hexadecimal → All')
    o.iconphoto(True, PhotoImage(file='binary.png'))
    o.geometry('550x460')
    o.config(bg='#6CB4EE')
    o.resizable(0, 0)

    default_text = StringVar()
    default_text.set('0')
    Entry(o, state=DISABLED, bd=12, textvariable=default_text, justify='right', font=('Times New Roman', 31, 'bold'), width=24).place(x=10, y=10)

    b0 = Button(o, text='0', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('0')).place(x=10, y=90)
    b1 = Button(o, text='1', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('1')).place(x=88, y=90)
    b2 = Button(o, text='2', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('2')).place(x=166, y=90)
    b3 = Button(o, text='3', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('3')).place(x=244, y=90)
    b4 = Button(o, text='4', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('4')).place(x=322, y=90)
    b5 = Button(o, text='5', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('5')).place(x=10, y=145)
    b6 = Button(o, text='6', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('6')).place(x=88, y=145)
    b7 = Button(o, text='7', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('7')).place(x=166, y=145)
    b8 = Button(o, text='8', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('8')).place(x=244, y=145)
    b9 = Button(o, text='9', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4, command=lambda: conversion().press('9')).place(x=322, y=145)

    bA = Button(o, text='a', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=3,
                command=lambda: conversion().press('a')).place(x=401, y=90)
    bB = Button(o, text='b', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4,
                command=lambda: conversion().press('b')).place(x=462, y=90)
    bC = Button(o, text='c', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=3,
                command=lambda: conversion().press('c')).place(x=401, y=145)
    bD = Button(o, text='d', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=4,
                command=lambda: conversion().press('d')).place(x=462, y=145)
    bE = Button(o, text='e', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=15,
                command=lambda: conversion().press('e')).place(x=10, y=200)
    bF = Button(o, text='f', relief=GROOVE, bd=2, font=("Times New Roman", 22, 'bold'), width=15,
                command=lambda: conversion().press('f')).place(x=275, y=200)

    dec_to_bin_button = Button(o, bg='#B9D9EB', text='Hex → Bin', relief=GROOVE, font=("Times New Roman", 22, 'bold'), width=15, bd=2, command=lambda: conversion().hex_to_bin()).place(x=10, y=275)
    dec_to_oct_button = Button(o, bg='#B9D9EB', text='Hex → Oct', relief=GROOVE, font=("Times New Roman", 22, 'bold'), width=15, bd=2, command=lambda: conversion().hex_to_oct()).place(x=10, y=335)
    dec_to_hex_button = Button(o, bg='#B9D9EB', text='Hex → Dec', relief=GROOVE, font=("Times New Roman", 22, 'bold'), width=15, bd=2, command=lambda: conversion().hex_to_dec()).place(x=10, y=395)

    clear_button = Button(o, text='C', bg='#A4DDED', relief=GROOVE, font=("Times New Roman", 21, 'bold'), width=15, height=2, bd=2, command=lambda: conversion().clear()).place(x=275, y=275)
    backspace_button = Button(o, text='←', bg='#A4DDED', relief=GROOVE, font=("Times New Roman", 21, 'bold'), width=15, height=2, bd=2, command=lambda: conversion().backspace()).place(x=275, y=363)
    o.mainloop()
