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
    def not_operation():
        global expression
        try:
            n = int(expression)
            expression = str(~n)
            default_text.set(expression)
        except:
            default_text.set("✖‿✖")
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


if __name__ == '__main__':
    o.config(bg='#B2BEB5')
    o.geometry('536x425')
    o.title('Bitwise Calculator')
    o.iconphoto(True, PhotoImage(file='binary.png'))
    o.resizable(0, 0)
    default_text = StringVar()
    default_text.set('0')

    Entry(o, justify=RIGHT, state=DISABLED, relief=FLAT, width=19, font=('Times New Roman', 42, 'bold'), textvariable=default_text, xscrollcommand=10).place(x=0, y=0)

    Button(o, text='7', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(7)).place(x=0, y=68)
    Button(o, text='8', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(8)).place(x=75, y=68)
    Button(o, text='9', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(9)).place(x=150, y=68)

    Button(o, text='4', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(4)).place(x=0, y=154)
    Button(o, text='5', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(5)).place(x=75, y=154)
    Button(o, text='6', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(6)).place(x=150, y=154)

    Button(o, text='1', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(1)).place(x=0, y=240)
    Button(o, text='2', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(2)).place(x=75, y=240)
    Button(o, text='3', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=4, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press(3)).place(x=150, y=240)

    Button(o, text='0', relief=FLAT, bg='WHITE', fg='#002D62', height=2, width=12, font=('Times New Roman', 23, 'bold'), command=lambda: conversion.press(0)).place(x=-2, y=326)

    Button(o, text='&', relief=FLAT, bg='#E1EBEE', fg='#00008B', height=2, width=5, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press('&')).place(x=225, y=68)
    Button(o, text='|', relief=FLAT, bg='#E1EBEE', fg='#00008B', height=2, width=5, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press('|')).place(x=316, y=68)
    Button(o, text='<<', relief=FLAT, bg='#E1EBEE', fg='#00008B', height=2, width=5, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press('<<')).place(x=225, y=154)
    Button(o, text='>>', relief=FLAT, bg='#E1EBEE', fg='#00008B', height=2, width=5, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press('>>')).place(x=316, y=154)

    Button(o, text='~', relief=FLAT, bg='#E1EBEE', fg='#00008B', height=2, width=8, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.not_operation()).place(x=407, y=68)
    Button(o, text='^', relief=FLAT, bg='#E1EBEE', fg='#00008B', height=2, width=8, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.press('^')).place(x=407, y=154)

    Button(o, text='C', relief=FLAT, bg='#B9D9EB', fg='#002244', height=2, width=5, font=('Times New Roman', 20, 'bold'), command=lambda: conversion.clear()).place(x=225, y=240)
    Button(o, text='← backspace', relief=FLAT, bg='#B9D9EB', fg='#002244', height=2, width=14, font=('Times New Roman', 20), command=lambda: conversion.backspace()).place(x=316, y=240)

    Button(o, text='=', relief=FLAT, bg='#002D62', fg='ORANGE', height=2, width=17, font=('Times New Roman', 23, 'bold'), command=lambda: conversion.equal_press()).place(x=225, y=326)

    o.mainloop()
