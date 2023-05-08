from tkinter import *
from tkinter import messagebox
import mysql.connector


background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"


root = Tk()
root.title("Login System")
root.geometry("1250x700+210+100")
root. config(bg=background)
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
def user_enter():
    user.delete(0, "end")


def user_leave():
    name = user.get()
    if name == "":
        user.insert(0, "User ID")

user = Entry(frame, width=18, fg="white", border=0, bg="#375174", font=("Arial Bold", 24))
user.insert(0, "User ID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500, y=315)






















root.mainloop()

