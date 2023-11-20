from tkinter import *
o = Tk()
expression = ''


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
    def oct_to_bin():
        global expression
        try:
            expression = str(bin(int(expression.lower(), 8)))[2:]
            default_text.set(expression)
        except:
            expression = 'Math Error'
            expression = ''

    @staticmethod
    def oct_to_dec():
        global expression
        try:
            expression = str(int(expression.lower(), 8))
            default_text.set(expression)

        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def oct_to_hex():
        global expression
        try:
            expression = str(hex(int(expression.lower(), 8)))[2:]
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''


if __name__ == '__main__':
    o.config(bg='#B2BEB5')
    o.geometry('535x326')
    o.title('Octal → All')
    o.iconphoto(True, PhotoImage(file='binary.png'))
    o.resizable(0, 0)
    default_text = StringVar()
    default_text.set('0')

    Entry(o, justify=RIGHT, state=DISABLED, relief=FLAT, width=19, font=('Times New Roman', 42, 'bold'), textvariable=default_text, xscrollcommand=10).place(x=0, y=0)

    Button(o, text='7', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(7)).place(x=0, y=68)
    Button(o, text='6', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(6)).place(x=75, y=68)
    Button(o, text='5', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(5)).place(x=150, y=68)
    Button(o, text='4', relief=FLAT, bg='#FFFFFF', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(4)).place(x=225, y=68)

    Button(o, text='3', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(3)).place(x=0, y=154)
    Button(o, text='2', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(2)).place(x=75, y=154)
    Button(o, text='1', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(1)).place(x=150, y=154)
    Button(o, text='0', relief=FLAT, bg='#FFFFFF', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(0)).place(x=225, y=154)

    Button(o, text='C', relief=FLAT, bg='#002D62', fg='ORANGE', height=2, width=9, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.clear()).place(x=-5, y=240)
    Button(o, text='←', relief=FLAT, bg='#002D62', fg='ORANGE', height=2, width=9, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.backspace()).place(x=150, y=240)

    Button(o, text='Oct → Bin', relief=FLAT, bg='#AFDBF5', fg='#00008B', height=2, width=14, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.oct_to_bin()).place(x=300, y=68)
    Button(o, text='Oct → Dec', relief=FLAT, bg='#AFDBF5', fg='#00008B', height=2, width=14, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.oct_to_dec()).place(x=300, y=154)
    Button(o, text='Oct → Hex', relief=FLAT, bg='#AFDBF5', fg='#00008B', height=2, width=14, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.oct_to_hex()).place(x=300, y=240)

    o.mainloop()
