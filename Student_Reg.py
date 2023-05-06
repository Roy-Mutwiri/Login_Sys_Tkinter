from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)

file = pathlib.Path("Student_data.xlsx")
if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active
    sheet['A1'] = "Registration No."
    sheet['B1'] = "Name"
    sheet['C1'] = "Class"
    sheet['D1'] = "Gender"
    sheet['E1'] = "DOB"
    sheet['F1'] = "Date Of Registration"
    sheet['G1'] = "Religion"
    sheet['H1'] = "Skill"
    sheet['I1'] = "Father Name"
    sheet['J1'] = "Mother Name"
    sheet['K1'] = "Father's Occupation"
    sheet['L1'] = "Mother's Occupation"

    file.save("Student_data.xlsx")

# Top Frames
Label(root, text="Email:mutwiriroy63@gmail.com", width=10, height=3, bg="#f0687c", anchor='e').pack(side=TOP, fill=X)
Label(root, text="STUDENT REGISTRATION", width=10, height=2, bg="#c36464", fg="white", font="arial 20 bold").pack(
    side=TOP, fill=X)

# Search Box To Update
Search = StringVar()
Entry(root, textvariable=Search, width=15, bd=2, font="arial 20").place(x=820, y=70)
imageicon3 = PhotoImage(file="/home/anon/PycharmProjects/Login_Sys_Tkinter./Images-20230505T155526Z-001"
                             "/Images/search.png")
Srch = Button(root, text="Search", compound=LEFT, image=imageicon3, width=123, bg='#68ddfa', font="arial 13 bold")
Srch.place(x=1060, y=66)

imageicon4 = PhotoImage(file="/home/anon/PycharmProjects/Login_Sys_Tkinter./Images-20230505T155526Z-001"
                             "/Images/Layer 4.png")
Update_button = Button(root, image=imageicon4, bg="#c36464")
Update_button.place(x=110, y=64)

# Registration And Date
Label(root, text="Registration No: ", font="arial 13", fg=framebg, bg=background).place(x=30, y=150)
Label(root, text="Date: ", font="arial 13", fg=framebg, bg=background).place(x=500, y=150)

Registration = StringVar()
Date = StringVar()

reg_entry = Entry(root, textvariable=Registration, width=15, font="arial 10")
reg_entry.place(x=160, y=150)

# registration_no()

today = date.today()
d1 = today.strftime("%d/%m/%Y")






root.mainloop()

# -------
