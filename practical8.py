# Practical 8

# A
import tkinter as tk
root = tk.Tk()
v1 = "How are you"
m1 = tk.Message(root, text = v1)
m1.pack()
root.mainloop()

# B
import tkinter as tk
def offer():
    v1 = "Nothing is or free, Pay It"
    m1 = tk.Message(root, text = v1)
    m1.pack()
root = tk.Tk()
b1 = tk.Button(root, text = "Click here for offer", command = offer)
b1.pack()
root.mainloop()

# C
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
val = tk.IntVar()
root.title("Python Prcatical")
root.configure(bg = '#FFFAFA')
root.geometry('200x250')

var = tk.IntVar()
frame = tk.LabelFrame(root, text = "Select your stream")
frame.pack(pady = 10, padx = 10)

def reset():
    return var.set(4)

def career():
    choice = var.get()
    if choice == 1:
        disp = "Medical\nTechnical\nMechanical\nResearch"
    elif choice == 2:
        disp = "Language\nPractical\nTheory\nTeaching\nFine Arts"
    elif choice == 3:

        disp = "Accounts\nEconomics\nManagement\nAdministration\nSecretary\nBanking\nInsurance\nR&D"
    else:
        dis = "Invalid"
    return messagebox.showinfo('Available Options', disp)

tk.Radiobutton(frame, text = "Science", variable = var, value = 1, command = career).pack(pady = 8)
tk.Radiobutton(frame, text = "Arts", variable = var, value = 2, command = career).pack(pady = 8)
tk.Radiobutton(frame, text = "Commerce", variable = var, value = 3, command = career).pack(pady = 8)

tk.Button(root, text = "reset", command = reset).pack()
root.mainloop()

# D
import tkinter as tk
root = tk.Tk()
root.title("Checkbox Example")
root.geometry("300x70")
var0 = tk.IntVar()
var1 = tk.IntVar()
tk.Checkbutton(root, text = "Technical", variable = var0).pack()
tk.Checkbutton(root, text = "Mechanical", variable = var1).pack()

root.mainloop()
