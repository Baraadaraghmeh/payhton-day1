print("Q1...........................")
from tkinter import *
parent=Tk()

#User=StringVar()

#password=StringVar()

name=Label(parent,text="Name").grid(row=0,column=0)

e1=Entry(parent).grid(row=0,column=1)

password=Label(parent,text="Password").grid(row=1,column=0)

e2=Entry(parent,textvariable=password).grid(row=1,column=1)
def Submit():
    if e1.get=="Orange" and e2.get=="Coding Academy" :
              print("Successful login")
    else :
              print("e-mail or password not correct")
    
submit=Button(parent,text="submit",command=Submit).grid(row=4,column=0)
parent.mainloop()
print("Q2.............................")
q2=Tk(className="Question 2")

def openmsg():
    messagebox.showinfo("Title", "This is a message")
    
def child1():
    c1=Toplevel(q2)
    c1.title("Child 1")
    Label(c1,text="Emp Number").grid(row=0,sticky=E)
    Label(c1,text="Emp Name").grid(row=1,sticky=E)
    x=StringVar()
    y=StringVar()
    Entry(c1,textvariable=x).grid(row=0,column=1)
    Entry(c1,textvariable=y).grid(row=1,column=1)
    Button(c1,text="Exit",command=c1.destroy).grid(row=2)



def child2():
    c2=Toplevel(q2)
    c2.title("Child 2")
    text=scrolledtext.ScrolledText(c2,width=40,height=10)
    text.insert('insert'," The count is 1 \n The count is 2 \n The count is 3 \n The count is 4 \n The count is 5 \n The count is 6 \n The count is 7 \n The count is 8 \n The count is 9 \n The count is 10 \n The count is 11 \n ")
    text.grid()

Button(q2,text="Open Message",command=openmsg).grid(row=0)
Button(q2,text="Open Child window 1",command=child1).grid(row=1)
Button(q2,text="Open Child window 2",command=child2).grid(row=2)
q2.mainloop()

print("Q3.................................")
def getcolor():
    color=askcolor()
    q3.configure(background=color[1])
q3=Tk(className="Question 3")
screen_width= q3.winfo_screenwidth()
screen_height= q3.winfo_screenheight()
q3.geometry(str(int(screen_width/2))+"x"+str(int(screen_height/2))+"+250+100")
Button(q3,text="Select Color",command=getcolor).grid()
q3.mainloop()


    







