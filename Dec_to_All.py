from tkinter import *
from tkinter import messagebox
import random

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
    def dec_to_bin():
        global expression
        try:
            expression = str(bin(int(expression)))[2:]
            expression = expression.upper()
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def dec_to_oct():
        global expression
        try:
            expression = str(oct(int(expression)))[2:]
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def dec_to_hex():
        global expression
        try:
            expression = str(hex(int(expression)))[2:]
            expression = expression.upper()
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

    o.title('Decimal → All')
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

    random_message = ['THANK YOU FOR SUPPORTING US!', "My Attitude in Exam:\nThey gave me questions I don't know,\nI'll give them answers they don't know.", "Winners are those people who never fail\nbut people who don't quit.", "The greatest glory in living lies not in never falling,\nbut in rising every time we fall.", "The way to get started is to quit talking and begin doing.", "Always remember that you are absolutely unique.\nJust like everyone else.", "It is during our darkest moments that we must focus to see the light.", "Studying for 4 hrs...\nNo mom no Dad\nAbout to touch the phone...\nMom and Dad behind me!!!"]

    friendly_button = Button(o, text="☺", relief=RAISED, bd=6, font=("Times New Roman", 25, 'bold'), width=6, height=2, command=lambda: messagebox.showinfo("Thank You!", random.choice(random_message))).place(x=401, y=91)

    dec_to_bin_button = Button(o, bg='#B9D9EB', text='Dec → Bin', relief=GROOVE, font=("Times New Roman", 20, 'bold'), width=32, bd=6, command=lambda: conversion().dec_to_bin()).place(x=10, y=205)
    dec_to_oct_button = Button(o, bg='#B9D9EB', text='Dec → Oct', relief=GROOVE, font=("Times New Roman", 20, 'bold'), width=32, bd=6, command=lambda: conversion().dec_to_oct()).place(x=10, y=265)
    dec_to_hex_button = Button(o, bg='#B9D9EB', text='Dec → Hex', relief=GROOVE, font=("Times New Roman", 20, 'bold'), width=32, bd=6, command=lambda: conversion().dec_to_hex()).place(x=10, y=325)

    clear_button = Button(o, text='C', relief=RAISED, font=("Times New Roman", 21, 'bold'), width=15, bd=1, command=lambda: conversion().clear()).place(x=10, y=395)
    backspace_button = Button(o, text='←', relief=RAISED, font=("Times New Roman", 21, 'bold'), width=15, bd=1, command=lambda: conversion().backspace()).place(x=278, y=395)
    o.mainloop()
