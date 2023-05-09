from tkinter import *
from tkinter import messagebox
import mysql.connector

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("Login System")
root.geometry("1250x700+210+100")
root.config(bg=background)
root.resizable(False, False)

# Icon Image

image_icon = PhotoImage(file="/home/anon/PycharmProjects/Login_Sys_Tkinter./Login System SQL/Images/icon.png")
root.iconphoto(False, image_icon)

# Background Image
frame = Frame(root, bg='red')
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="/home/anon/PycharmProjects/Login_Sys_Tkinter./Login System SQL/Images/LOGIN.png")
Label(frame, image=backgroundimage).pack()


# User Entry
def user_enter(e):
    user.delete(0, "end")


def user_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "User ID")


user = Entry(frame, width=18, fg="white", border=0, bg="#375174", font=("Arial Bold", 24))
user.insert(0, "User ID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500, y=315)


# Password Entry

def password_enter(e):
    code.delete(0, "end")


def password_leave(e):
    if code.get() == "":
        code.insert(0, "Password")


code = Entry(frame, width=18, fg="white", border=0, bg="#375174", font=("Arial Bold", 24))
code.insert(0, "Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=500, y=410)

#  Hide And Show Button

button_mode = True


def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye, activebackground="white")
        code.config(show="*")
        button_mode = False

    else:
        eyeButton.config(image=openeye, activebackground="white")
        code.config(show="")
        button_mode = True


openeye = PhotoImage(file="/home/anon/PycharmProjects/Login_Sys_Tkinter./Login System SQL/Images/openeye.png")
closeeye = PhotoImage(file="/home/anon/PycharmProjects/Login_Sys_Tkinter./Login System SQL/Images/close eye.png")

eyeButton = Button(frame, image=openeye, bg="#375174", bd=0, command=hide)
eyeButton.place(x=780, y=410)

# -----------------
loginButton = Button(root, text="LOGIN", bg="#1f5675", fg="white", width=10, height=1, font=("arial", 16, "bold"), bd=0)
loginButton.place(x=570, y=600)

label = Label(root, text="Don't have an account?", fg="white", bg="#00264d", font=("Microsoft YaHei UI Light", 9))
label.place(x=500, y=500)


root.mainloop()
