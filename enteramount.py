from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(bg="gray")
window.title("Exception Handling")
window.geometry("300x300")
window.resizable(0, 0)

amountlabel = Label(window, text="Please enter funds available:", bg="skyblue")
amountlabel.place(x=20, y=30)
amountfield = Entry(window)
amountfield.place(x=20, y=80)


def checkqualification():
    try:
        money = float(amountfield.get())
        if money < 3000:
            messagebox.showerror("Insufficient funds", "Please deposit more funds for this excursion.")
            amountfield.delete(0, END)
        else:
            messagebox.showinfo("Accepted", "Congratulations. You qualify to go to Malaysia")
            amountfield.delete(0, END)
    except ValueError:
        messagebox.showerror("Invalid input", "Please put in an amount in numbers.")
        amountfield.delete(0, END)


enterbutton = Button(window, text="Enter", bg="royalblue", command=checkqualification)
enterbutton.place(x=20, y=120)


def clearfunc():
    amountfield.delete(0, END)


clearbutton = Button(window, text="Clear", bg="white", command=clearfunc)
clearbutton.place(x=100, y=120)


def exitfunc():
    window.destroy()


exitbutton = Button(window, text="Exit", bg="#a4d1cc", command=exitfunc)
exitbutton.place(x=230, y=120)

window.mainloop()