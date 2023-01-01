import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql

def showLastinfo():
    db = mysql.connect(host = "localhost", user = "Prabhat", passwd = "151103")
    cursor = db.cursor()
    cursor.execute("use prabhat")
    insrt = "Insert into skills values('"+fname.get()+"','"+lname.get()+"','"+age.get()+"','"+income.get()+"')"
    cursor.execute(insrt)
    db.commit()


win = tk.Tk()
win.title("Employee Details")
tk.Label(win, text = "First Name").grid(row = 0)
tk.Label(win, text = "Last Name").grid(row = 1)
tk.Label(win, text = "Age").grid(row = 2)
tk.Label(win, text = "Salary").grid(row = 3)

fname = tk.Entry(win).grid(row = 0, column = 1)
lname = tk.Entry(win).grid(row = 1, column = 1)
age = tk.Entry(win).grid(row = 2, column = 1)
income = tk.Entry(win).grid(row = 3, column = 1)


b1 = tk.Button(win, text = "Quit", command = win.destroy).grid(row = 4, column = 0, pady = 4, sticky = 'W')
b2 = tk.Button(win, text = "Insert", command = showLastinfo).grid(row = 4, column =1 , pady = 4, sticky = 'W')

win.mainloop()