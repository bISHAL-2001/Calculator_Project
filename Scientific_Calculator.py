import math
from tkinter import *
expression = '0'


class Scientific_Calculator:

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
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def square():
        global expression
        try:
            n = float(expression)
            expression = str(math.pow(n, 2))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def cube_root():
        global expression
        try:
            n = float(expression)
            if n < 0:
                expression = str((-1) * (math.pow((n * -1), (1.0 / 3))))
            else:
                expression = str((math.pow(n, (1.0 / 3))))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def cube():
        global expression
        try:
            n = float(expression)
            expression = str(math.pow(n, 3))
            default_text.set(expression)
        except:
            expression = ' '
            default_text.set(expression)
            expression = ''

    @staticmethod
    def plus_minus():
        global expression
        try:
            n = float(expression)
            expression = str(-n)
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def facto():
        global expression
        try:
            n = int(expression)
            expression = str(math.factorial(n))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def inverse():
        global expression
        try:
            n = float(expression)
            expression = str(math.pow(n, -1))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def sin():
        global expression
        try:
            n = float(expression)
            expression = str(math.sin(math.radians(n)))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def cos():
        global expression
        try:
            n = float(expression)
            expression = str(math.cos(math.radians(n)))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def tan():
        global expression
        try:
            n = float(expression)
            if n != 0 and n % 90 == 0:
                expression = 'Math Error'
            else:
                expression = str(math.tan(math.radians(n)))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def sinh():
        global expression
        try:
            n = float(expression)
            expression = str(math.sinh(n))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def cosh():
        global expression
        try:
            n = float(expression)
            expression = str(math.cosh(n))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def tanh():
        global expression
        try:
            n = float(expression)
            expression = str(math.tanh(n))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def log():
        global expression
        try:
            n = float(expression)
            if n == 0:
                expression = 'Math Error'
            else:
                expression = str(math.log(n, 10))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''

    @staticmethod
    def ln():
        global expression
        try:
            n = float(expression)
            if n == 0:
                expression = 'Math Error'
            else:
                expression = str(math.log(n))
            default_text.set(expression)
        except:
            expression = 'Math Error'
            default_text.set(expression)
            expression = ''


if __name__ == '__main__':
    obj = Tk()
    obj.title('Scientific Calculator')
    obj.geometry("492x378")
    obj.resizable(0, 0)

    obj.config(bg='BLACK')

    obj.iconphoto(True, PhotoImage(file="Calcu.png"))

    default_text = StringVar()
    default_text.set('0')

    Entry(obj, relief=GROOVE, bd=6, fg='BLACK', font=('Times New Roman', 35), textvariable=default_text, justify=RIGHT).pack(side=TOP)

    Button(obj, relief=GROOVE, bg='#B2FFFF', text='7', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(7)).place(x=0, y=70)
    Button(obj, relief=GROOVE, bg='#B2FFFF', text='8', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(8)).place(x=58, y=70)
    Button(obj, relief=GROOVE, bg='#B2FFFF', text='9', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(9)).place(x=116, y=70)

    Button(obj, relief=GROOVE, bg='#B2FFFF', text='4', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(4)).place(x=0, y=112)
    Button(obj, relief=GROOVE, bg='#B2FFFF', text='5', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(5)).place(x=58, y=112)
    Button(obj, relief=GROOVE, bg='#B2FFFF', text='6', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(6)).place(x=116, y=112)

    Button(obj, relief=GROOVE, bg='#B2FFFF', text='1', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(1)).place(x=0, y=154)
    Button(obj, relief=GROOVE, bg='#B2FFFF', text='2', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(2)).place(x=58, y=154)
    Button(obj, relief=GROOVE, bg='#B2FFFF', text='3', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(3)).place(x=116, y=154)

    Button(obj, relief=GROOVE, bg='#7DF9FF', text='0', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(0)).place(x=0, y=196)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='00', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press('00')).place(x=58, y=196)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='.', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press('.')).place(x=116, y=196)

    Button(obj, relief=GROOVE, bg='#7DF9FF', text='sin', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().sin()).place(x=174, y=70)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='cos', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().cos()).place(x=232, y=70)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='tan', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().tan()).place(x=290, y=70)

    Button(obj, relief=GROOVE, bg='#7DF9FF', text='sinh', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().sinh()).place(x=174, y=112)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='cosh', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().cosh()).place(x=232, y=112)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='tanh', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().tanh()).place(x=290, y=112)

    Button(obj, relief=GROOVE, bg='#7DF9FF', text='log', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().log()).place(x=174, y=154)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='ln', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().ln()).place(x=232, y=154)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='e', height=1, width=4, font=('Times New Roman', 16, 'bold', 'italic'),  command=lambda: Scientific_Calculator().press(math.e)).place(x=290, y=154)

    Button(obj, relief=GROOVE, bg='#7DF9FF', text='±', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().plus_minus()).place(x=174, y=196)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='!', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().facto()).place(x=232, y=196)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='x\u207B\u00b9', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().inverse()).place(x=290, y=196)

    Button(obj, relief=GROOVE, bg='#7DF9FF', text='x²', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().square()).place(x=0, y=238)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='x\u00b3', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().cube()).place(x=58, y=238)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text="^", height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press('**')).place(x=116, y=238)

    Button(obj, relief=GROOVE, bg='#7DF9FF', text='√', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().square_root()).place(x=174, y=238)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='∛', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().cube_root()).place(x=232, y=238)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='10\u207F', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press('10**')).place(x=290, y=238)

    Button(obj, relief=GROOVE, bg='#7DF9FF', text='π', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(math.pi)).place(x=0, y=280)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='log 2', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(math.log(2, 10))).place(x=58, y=280)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='log 3', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(math.log(3, 10))).place(x=116, y=280)

    Button(obj, relief=GROOVE, bg='#7DF9FF', text='√2', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(math.sqrt(2))).place(x=174, y=280)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='√3', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(math.sqrt(3))).place(x=232, y=280)
    Button(obj, relief=GROOVE, bg='#7DF9FF', text='√5', height=1, width=4, font=('Times New Roman', 16, 'bold'), command=lambda: Scientific_Calculator().press(math.sqrt(5))).place(x=290, y=280)

    Button(obj, relief=GROOVE, text='+ ', height=2, bd=3, bg='#6BCAE2', width=4, font=('Times New Roman', 20, 'bold'), command=lambda: Scientific_Calculator().press('+')).place(x=348, y=70)
    Button(obj, relief=GROOVE, text='-', height=2, bd=3, bg='#6BCAE2', width=4, font=('Times New Roman', 20, 'bold'), command=lambda: Scientific_Calculator().press('-')).place(x=416, y=70)

    Button(obj, relief=GROOVE, text='←', height=1, bd=3, bg='#6BCAE2', width=11, font=('Times New Roman', 15, 'bold'), command=lambda: Scientific_Calculator().backspace()).place(x=348, y=155)
    Button(obj, relief=GROOVE, text='C', height=1, bd=3, bg='#6BCAE2', width=11, font=('Times New Roman', 15, 'bold'), command=lambda: Scientific_Calculator().clear()).place(x=348, y=196)

    Button(obj, relief=GROOVE, text='* ', height=2, bd=3, bg='#6BCAE2', width=4, font=('Times New Roman', 20, 'bold'), command=lambda: Scientific_Calculator().press('*')).place(x=348, y=236)
    Button(obj, relief=GROOVE, text='/', height=2, bd=3, bg='#6BCAE2', width=4, font=('Times New Roman', 20, 'bold'), command=lambda: Scientific_Calculator().press('/')).place(x=416, y=236)

    Button(obj, relief=GROOVE, text='=', height=1, bd=3, bg='#6BCAE2', width=30, font=('Times New Roman', 20, 'bold'), command=lambda: Scientific_Calculator().equal_press()).place(x=0, y=322)

    obj.mainloop()
