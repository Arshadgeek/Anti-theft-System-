import sqlite3
conn = sqlite3.connect("Project.db")
c =conn.cursor()
import pygubu 


#.....................................................................................
from tkinter import*
from tkinter import ttk
from tkinter import messagebox 




win = Tk()



#.....................................................................................
win.title('warning')
win.geometry("400x800+0+0")



#.......................................................................................

def endofday():
    endoftheday = Tk()
    endoftheday.title("this is the final sheet")
    endoftheday.geometry("500x500+900+0")

    L1 = Listbox(endoftheday)
    L1.pack()
   
    c.execute('SELECT serial,amount FROM custemer')
    L1.insert(END,c.fetchall())

    
    

    

#.......................................................................................

def insertdata(E1,E2,E3,E4,E5,E6,E7):
    
    
    c.execute("INSERT INTO custemer (serial,amount,name,address,email,cantact,aadhar) VALUES(?,?,?,?,?,?,?)",(E1,E2,E3,E4,E5,E6,E7))

  

#.......................................................................................
e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()


def sold(A):
    solditem = Tk()
    solditem.geometry("500x400+400+0")
    F1 = Frame(solditem, width = 500,height = 300)
    F1.pack(side= TOP)
    F2 = Frame(solditem, width = 500,height = 100)
    F2.pack(side= BOTTOM)
    solditem.title("Sold sheet for"+ A)
 
    L1 = Label(F1, text ="Serial No:",anchor = E)
    L1.grid(row = 0 ,column = 0)

    E1  = Entry(F1,textvariable = e1)
    E1.grid(row = 0 ,column = 2, sticky = N)

    L2  = Label(F1 , text ="Total Amount:",anchor = E)
    L2.grid(row = 1 ,column = 0)

    E2 = Entry(F1,textvariable = e2)
    E2.grid(row = 1 ,column = 2)
    
    L3 =  Label(F1, text ="Name:",anchor = E)
    L3.grid(row = 4 ,column = 0)

    E3 = Entry(F1,textvariable = e3)
    E3.grid(row = 4 ,column = 2,sticky = N)

    L4 = Label(F1,text = "Address:",anchor = E)
    L4.grid(row = 5 ,column = 0)

    E4 = Entry(F1,textvariable = e4)
    E4.grid(row = 5 ,column = 2)

    L5 = Label(F1, text ="Email:",anchor = E)
    L5.grid(row = 6 ,column = 0)

    E5 = Entry(F1,textvariable = e5)
    E5.grid(row = 6 ,column = 2)

    L6 = Label(F1, text ="Cntact No:",anchor = E)
    L6.grid(row = 7 ,column = 0)
    
    E6 = Entry(F1,textvariable = e6)
    E6.grid(row = 7 ,column = 2)

    L7 = Label(F1, text ="Aadhar Card No:",anchor = E)
    L7.grid(row = 8 ,column = 0)

    E7 = Entry(F1,textvariable = e7)
    E7.grid(row = 8 ,column = 2)

    
    


    b1 = Button (F2,text = "Paid",command= lambda:insertdata(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(), E6.get(), E7.get()))  
    b1.pack(side= TOP)
    b2 = Button (F2,text = "Cancel",command= passvalue(A))
    b2.pack(side= TOP)


C1 = Button(win, text="End of the day",command=lambda:endofday(),anchor = E)
C1.pack(side = BOTTOM)
#.........................................................................................








#.........................................................................................
def passvalue(a):

    if a is not 0:
        print(a)
    else:
        win.destroy()
#..........................................................................................
def messageWindow(A):

    message = A +" has been picked up for a long time"
    Label(win, text=message).pack()
    B1 = Button(win, text='Ignore',command=lambda:passvalue(A),anchor = E)
    B1.pack()
    B2 = Button(win, text='Sold',command=lambda:sold(A),anchor = E)
    B2.pack()
    B3 = Button(win, text='Alerted',command=lambda:passvalue(A),anchor = E)
    B3.pack()
    Scrollbar(win, orient = "vertical")

    exit

B4 = Button(win, text = 'end',command = lambda:passvalue(A),anchor = E)
B4.pack(side = BOTTOM)
#.......................................................................................
B = "ON"
while B is "ON":
 
        A = input("enter the item which has been picked up:")
        messageWindow(A)


