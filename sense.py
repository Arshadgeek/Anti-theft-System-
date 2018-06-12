
from tkinter import*
from tkinter import messagebox 


window = Tk()
window.geometry("400x400+0+0")
window.title("Project")
Tops = Frame(window,bg="white",width = 800,height=50,relief=RAISED)
Tops.pack(side=TOP)

f1 = Frame(window,width = 400,height=450,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(window,width = 400,height=450,relief=SUNKEN)
f2.pack(side=RIGHT)

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Anti Theft System",fg="dark red",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
#.............................................................................................................
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()

 
def type_():
    if var1.get() is 1:
        messagebox.showwarning("Title", "A has been picked up ")
        
    if var2.get() is 1:
        messagebox.showinfo("Title", "B has been picked up ")
    if var3.get() is 1:
        messagebox.showinfo("Title", "C has been picked up ")
    if var4.get() is 1:
        messagebox.showinfo("Title", "D has been picked up ")
    if var5.get() is 1:
        messagebox.showinfo("Title", "E has been picked up ")
    if var6.get() is 1:
        messagebox.showinfo("Title", "F has been picked up ")
    if var7.get() is 1:
        messagebox.showinfo("Title", "G has been picked up ")
    if var8.get() is 1:
        messagebox.showinfo("Title", "H has been picked up ")
    if var9.get() is 1:
        messagebox.showinfo("Title", "I has been picked up ")



A1 = Radiobutton(f1, font=( 'aria' ,16, ),text="A", variable=var1, value=1,command= type_,anchor = E)
A1.grid(row = 1,column= 1,sticky=W)

A2 = Radiobutton(f1, font=( 'aria' ,16, ),text="B", variable=var2, value=1,command= type_,anchor = E)
A2.grid(row = 1,column= 2,sticky=W)

A3 = Radiobutton(f1, font=( 'aria' ,16, ),text="C", variable=var3, value=1,command= type_,anchor = E)
A3.grid(row = 1,column= 3,sticky=W)

A4 = Radiobutton(f1, font=( 'aria' ,16, ),text="D", variable=var4, value=1,command= type_,anchor = E)
A4.grid(row = 2,column= 1,sticky=W)


A5 = Radiobutton(f1, font=( 'aria' ,16, ),text="E", variable=var5, value=1,command= type_,anchor = E)
A5.grid(row = 2,column= 2,sticky=W)

A6 = Radiobutton(f1, font=( 'aria' ,16, ),text="F", variable=var6, value=1,command= type_,anchor = E)
A6.grid(row = 2,column= 3,sticky=W)

A7 = Radiobutton(f1, font=( 'aria' ,16, ),text="G", variable=var7, value=1,command= type_,anchor = E)
A7.grid(row = 3,column= 1,sticky=W)

A8 = Radiobutton(f1, font=( 'aria' ,16, ),text="H", variable=var8, value=1,command= type_,anchor = E)
A8.grid(row = 3,column= 2,sticky=W)

A9 = Radiobutton(f1, font=( 'aria' ,16, ),text="I", variable=var9, value=1,command= type_,anchor = E)
A9.grid(row = 3,column= 3,sticky=W)
