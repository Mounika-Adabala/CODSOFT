from tkinter import *


first=second=operator=None;
def dig(digit):
    current=result_label['text']
    new=current + str(digit)
    result_label.config(text=new)


def clear():
    result_label.config(text='')

def oper(op):
    global first,operator
    
    first=float(result_label['text'])
    operator=op
    result_label.config(text='')

def res():
    global first,second,operator
    second=float(result_label['text'])

    if operator=='+':
        result_label.config(text=str(first + second))
    elif operator == '-':
        result_label.config(text=str(first - second))
    elif operator == '*':
        result_label.config(text=str(first * second))
    elif operator == '%':
        if second == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first % second)))        
    else:
        if second==0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first / second)))
            
            
    
root=Tk()
root.title('Calculator')
root.geometry('280x440')
root.resizable(False,False)
root.configure(background='black')

result_label=Label(root,text='',bg='white', fg='black')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))


btn7 = Button(root,text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig(7))
btn7.grid(row=1, column=0)
btn7.config(font=('verdana',14))
                    
btn8 = Button(root,text='8', bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig(8))
btn8.grid(row=1, column=1)
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9', bg='#00a65a', bd=1, fg='white', width=5, height=2, command=lambda: dig(9))
btn9.grid(row=1, column=2)
btn9.config(font=('verdana',14))

btn4 = Button(root,text='4', bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig(4))
btn4.grid(row=2, column=0)
btn4.config(font=('verdana',14))

btn5 = Button(root,text='5', bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig(5))
btn5.grid(row=2, column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6', bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig(6))
btn6.grid(row=2, column=2)
btn6.config(font=('verdana',14))

btn1 = Button(root,text='1', bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig(1))
btn1.grid(row=3, column=0)
btn1.config(font=('verdana',14))

btn2 = Button(root,text='2', bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig(2))
btn2.grid(row=3, column=1)
btn2.config(font=('verdana',14))

btn1 = Button(root,text='3',  bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig(3))
btn1.grid(row=3, column=2)
btn1.config(font=('verdana',14))

btn0 = Button(root,text='0', bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig(0))
btn0.grid(row=4, column=1)
btn0.config(font=('verdana',14))

btnp = Button(root,text='+', bg='#00a65a', fg='white', width=5, height=2, command=lambda: oper('+'))
btnp.grid(row=4, column=0)
btnp.config(font=('verdana',14))

btns = Button(root,text='-', bg='#00a65a', fg='white', width=5, height=2, command=lambda: oper('-'))
btns.grid(row=2, column=3)
btns.config(font=('verdana',14))

btnm = Button(root,text='*', bg='#00a65a', fg='white', width=5, height=2, command=lambda: oper('*'))
btnm.grid(row=3, column=3)
btnm.config(font=('verdana',14))

btne = Button(root,text='=', bg='blue', fg='white', width=5, height=2, command=lambda:res())
btne.grid(row=5, column=3)
btne.config(font=('verdana',14))

btnc = Button(root,text='C', bg='orange', fg='white', width=5, height=2, command=lambda: clear())
btnc.grid(row=1, column=3)
btnc.config(font=('verdana',14))

btnd = Button(root,text='/', bg='#00a65a', fg='white', width=5, height=2, command=lambda: oper('/'))
btnd.grid(row=4, column=2)
btnd.config(font=('verdana',14))

btnde = Button(root,text='.', bg='#00a65a', fg='white', width=5, height=2, command=lambda: dig('.'))
btnde.grid(row=5, column=0)
btnde.config(font=('verdana',14))



btnr = Button(root,text='%', bg='#00a65a', fg='white', width=5, height=2, command=lambda:oper('%'))
btnr.grid(row=4, column=3)
btnr.config(font=('verdana',14))
root.mainloop()
