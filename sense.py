import sqlite3
conn = sqlite3.connect("Project.db")
c =conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stuff(Serial TEXT,Amount TEXT,Name TEXT,Address TEXT,Email TEXT,Email TEXT,Contact TEXT,Aadhar TEXT)")

#.....................................................................................
from tkinter import*
from tkinter import messagebox 


win = Tk()
solditem = Tk()
solditem.geometry("500x400+400+0")
F1 = Frame(solditem, width = 500,height = 300)
F1.pack(side= TOP)
F2 = Frame(solditem, width = 500,height = 100)
F2.pack(side= BOTTOM)


win.title('warning')
win.geometry("400x800+0+0")




endoftheday = Tk()
endoftheday.title("this is the final sheet")
endoftheday.geometry("500x500+900+0")

#.......................................................................................

def endofday():
    Label(endoftheday,text = "list of all sold items",anchor = E).pack()
#.......................................................................................

def insertdata(E1,E2,E3,E4,E5,E6,E7):
    c.execute("INSERT INTO stuff (Serial,Amount,Name,Address,Email,Email,Contact,Aadhar) VALUES(?,?,?,?,?,?,?)",(E1,E2,E3,E4,E5,E6,E7))
    print("executed")









#.......................................................................................
E1 = StringVar()
E2 = StringVar()
E3 = StringVar()
E4 = StringVar()
E5 = StringVar()
E6 = StringVar()
E7 = StringVar()


def sold(A):
    solditem.title("Sold sheet for"+ A)
 
    Label(F1, text ="Serial NO:",anchor = E).grid(row = 0 ,column = 0)
    Entry(F1, textvariable = E1).grid(row = 0 ,column = 2, sticky = N)
    Label(F1 , text ="Total Amount:",anchor = E).grid(row = 1 ,column = 0)
    Entry(F1,textvariable = E2).grid(row = 1 ,column = 2)
    
    Label(F1, text ="Name:",anchor = E).grid(row = 4 ,column = 0)
    Entry(F1,textvariable = E3).grid(row = 4 ,column = 2,sticky = N)
    Label(F1,text = "Address:",anchor = E).grid(row = 5 ,column = 0)
    Entry(F1,textvariable = E4).grid(row = 5 ,column = 2)
    Label(F1, text ="Email:",anchor = E).grid(row = 6 ,column = 0)
    Entry(F1,textvariable = E5).grid(row = 6 ,column = 2)
    Label(F1, text ="Cntact No:",anchor = E).grid(row = 7 ,column = 0)
    Entry(F1,textvariable = E6).grid(row = 7 ,column = 2)
    Label(F1, text ="Aadhar Card No:",anchor = E).grid(row = 8 ,column = 0)
    Entry(F1,textvariable = E7).grid(row = 8 ,column = 2)


    e1 = E1.get()
    e2 = E2.get()
    e3 = E3.get()
    e4 = E4.get()
    e5 = E5.get()
    e6 = E6.get()
    e7 = E7.get()


    Button (F2,text = "Paid",command= lambda: insertdata(e1,e2,e3,e4,e5,e6,e7)).pack(side= TOP)
    Button (F2,text = "Cancel",command= passvalue(A)).pack(side= TOP)










    

C1 = Button(win, text="End of the day",command=lambda:endofday(),anchor = E)
C1.pack(side = BOTTOM)
    




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


win.mainloop()






