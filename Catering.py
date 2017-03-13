#Main file
from tkinter import filedialog
from tkinter import *
import pandas
print("Varsha")

root = Tk()
root.fileName = filedialog.askopenfilename( filetypes = (("All files","*.xlsx"),))

print("err:",root.fileName)


df = pandas.ExcelFile(root.fileName)
df.sheet_names
