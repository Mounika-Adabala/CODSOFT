from tkinter import *
import string
import random

root = Tk()
root.geometry("400x300")
root.title("Password Generator")

passstr = StringVar()
pwdlen = IntVar()


def getpass():
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for x in range(pwdlen.get()):
        password += random.choice(pass1)
        passstr.set(password)

Label(root, text='Password Generator', font="Calibri 18 bold").pack()

Label(root, text="Enter Length: ", font="cursive 14").pack(pady=9)

Entry(root, textvariable=pwdlen,width=30, font="cursive 14").pack(pady=2)

Button(root, text="Generate password", command=lambda: getpass()).pack(pady=15)

Entry(root, textvariable=passstr,width=30, font="cursive 14").pack(pady=2)

root.mainloop()
