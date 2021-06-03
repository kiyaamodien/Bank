import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Authentification")
root.geometry("400x400")
root.config(bg="royalblue")

class AccountAuthentication:
    def __init__(self, master):
        frame1 = Frame(master, width=350, height=350, bg="gray")
        frame1.place(x=30, y=30)

        frame2 = Frame(master, width=350, height=350, bg="gray")
        frame2.place(x=30, y=380)

        self.usernameLabe1 = Label(frame1, text="Please enter username", bg="white")
        self.usernameLabe1.place(x=10, y=50)
        self.username = Entry(frame1, bg="white")
        self.username.place(x=180, y=50)

        self.passwordLabe2 = Label(frame1, text="Please enter password", bg="white")
        self.passwordLabe2.place(x=10, y=80)
        self.password = Entry(frame1, bg="white")
        self.password.place(x=180, y=80)

        def logginbutton():
            users = {"Abdullah": "1234", "Mikayla": "4321", "Jesse": "6666", "Justin": "1111", "Zoe": "4444"}
            user = list(users.keys())
            password = list(users.values())
            found = False
            for x in range(len(users)):
                if self.username.get() == user[x] and self.password.get() == password[x]:
                    found = True
            if found is True:
                        frame2.config(bg="skyblue")
                        self.access.config(bg="red", text="")
                        messagebox.showinfo("status", "Access Granted")
                        root.destroy()
                        import enteramount
            else:
                if self.username.get() not in users:
                    frame2.config(bg="purple")
                    self.access.config(bg="purple")
                    messagebox.showerror("Access Denied", "Unknown User")
                else:
                    frame2.config(bg="purple")
                    self.access.config(bg="purple")
                    messagebox.showerror("Access Denied", "InIncorrect username or password.")

        login = Button(frame1, text="Log in", borderwidth="2", command=logginbutton)
        login.place(x=100, y=170)

        def clearbutton():
            frame2.config(bg="black")
            self.access.config(bg="black", text="")
            self.access.place(x=50, y=40)
            self.username.delete(0, END)
            self.password.delete(0, END)

        clear = Button(frame1, text="Clear", borderwidth="2", command=clearbutton)
        clear.place(x=10, y=170)

        def exitprogram():
            root.destroy()

        exitt = Button(frame1, text="Exit", borderwidth="2", command=exitprogram)
        exitt.place(x=195, y=170)

        self.access = Label(frame2)
        self.access.place(x=50, y=40)


c = AccountAuthentication(root)
root.mainloop()



