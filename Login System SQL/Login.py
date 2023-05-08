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



root.mainloop()

