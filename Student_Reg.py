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
    sheet['B1'] = ""
    sheet['C1'] = ""
    sheet['D1'] = ""
    sheet['E1'] = ""
    sheet['F1'] = ""
    sheet['G1'] = ""
    sheet['H1'] = ""
    sheet['I1'] = ""
    sheet['J1'] = ""
    sheet['K1'] = ""
    sheet['L1'] = ""

root.mainloop()





