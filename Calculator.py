import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox


if __name__ == '__main__':
    o = Tk()
    menu = Menu(o)

    new = Menu(menu, tearoff=0)
    menu.add_cascade(label='File', menu=new)


    def new_window():
        os.system('Calculator.exe')


    new.add_command(label='New', command=new_window)
    about = Menu(menu, tearoff=0)
    menu.add_cascade(label='About', menu=about)
    about.add_command(label='Version 1.0', command=None)


    def ExitApplication():
        msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if msg_box == 'yes':
            o.destroy()
        else:
            tk.messagebox.showinfo('Return', 'Return to the application window')


    exit_click = Menu(menu, tearoff=0)
    menu.add_cascade(label='More', menu=exit_click)
    exit_click.add_command(label='Exit', command=ExitApplication)

    o.config(menu=menu)

    o.title("Calculator Options")
    o.iconphoto(True, PhotoImage(file="calculator.png"))
    o.geometry("500x521")
    o.config(relief=SUNKEN, bg="#ADD8E6")


    def click_basic():
        os.system('Basic_Calculator.exe')


    def click_scientific():
        os.system('Scientific_Calculator.exe')


    def click_binary_to_all():
        os.system('Binary_to_All.exe')

    def click_octal_to_all():
        os.system('Oct_to_All.exe')

    def click_decimal_to_all():
        os.system('Dec_to_All.exe')

    def click_hex_to_all():
        os.system('Hex_to_All.exe')

    def click_bitwise():
        os.system('Bitwise_Operations.exe')

    def button():
        Button(o, bg="#BCD4E6", fg="black", relief="groove", text="Basic", font=("Times New Roman", 16, "bold"),
               command=click_basic).pack(fill="both", expand=True)
        Button(o, bg="#89CFF0", fg="black", relief="groove", text="Scientific", font=("Times New Roman", 16, "bold"),
               command=click_scientific).pack(fill='both', expand=True)

        Button(o, bg="#BCD4E6", fg="black", relief="groove", text="Bin → Oct, Dec, Hex", font=("Times New Roman", 16, "bold"),
               command=click_binary_to_all).pack(fill='both', expand=True)

        Button(o, bg="#89CFF0", fg="black", relief="groove", text="Oct → Bin, Dec, Hex", font=("Times New Roman", 16, "bold"),
               command=click_octal_to_all).pack(fill='both', expand=True)

        Button(o, bg="#BCD4E6", fg="black", relief="groove", text="Dec → Bin, Oct, Hex",
               font=("Times New Roman", 16, "bold"), command=click_decimal_to_all).pack(fill='both', expand=True)

        Button(o, bg="#89CFF0", fg="black", relief="groove", text="Hex → Bin, Oct, Dec",
               font=("Times New Roman", 16, "bold"), command=click_hex_to_all).pack(fill='both', expand=True)

        Button(o, bg="#BCD4E6", fg="black", relief="groove", text="Bitwise Operations",
               font=("Times New Roman", 16, "bold"), command=click_bitwise).pack(fill='both', expand=True)


    button()
    o.mainloop()
