from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Number=IntVar()
Nationality = StringVar()
Date=StringVar()
Gender= StringVar()
Address=StringVar()
Department=StringVar()
Salary=IntVar()


def database():
   name1=Fullname.get()
   number=Number.get()
   nationality=Nationality.get()
   date=Date.get()
   gender=Gender.get()
   address=Address.get()
   department=Department.get()
   salary=Salary.get()
   

   conn = sqlite3.connect('OrgDB.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Employees (Fullname TEXT,Number INT,Nationality TEXT,Date TEXT, Gender TEXT,Address TEXT,Department TEXT , Salary INT)')
   cursor.execute('INSERT INTO Employees (FullName,Number,Nationality,Date,Gender,Address,Department,Salary) VALUES(?,?,?,?,?,?,?,?)',(name1,number,nationality,date,gender,address,department,salary))
   for row in cursor.execute('SELECT * FROM Employees ORDER BY Salary'):
       print(row)
   conn.commit()
   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)


#...............
label_2 = Label(root, text="Number",width=20,font=("bold", 10))
label_2.place(x=70,y=160)

entry_2 = Entry(root,textvar=Number)
entry_2.place(x=240,y=160)



label_3 = Label(root, text="Nationality",width=20,font=("bold", 10))
label_3.place(x=68,y=190)

entry_3 = Entry(root,textvar=Nationality)
entry_3.place(x=240,y=190)

label_4 = Label(root, text="Gender",width=20,font=("bold", 10))
label_4.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=Gender, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=Gender, value=2).place(x=290,y=230)

label_5 = Label(root, text="Date of Birth",width=20,font=("bold", 10))
label_5.place(x=70,y=280)

entry_5 = Entry(root,textvar=Date)
entry_5.place(x=240,y=280)
#.........................
label_6 = Label(root, text="Address",width=20,font=("bold", 10))
label_6.place(x=75,y=310)

entry_6 = Entry(root,textvar=Address)
entry_6.place(x=240,y=310)




label_7 = Label(root, text="Department",width=20,font=("bold", 10))
label_7.place(x=80,y=340)

entry_7 = Entry(root,textvar=Department)
entry_7.place(x=240,y=340)



label_8 = Label(root, text="Salary",width=20,font=("bold", 10))
label_8.place(x=80,y=370)

entry_8 = Entry(root,textvar=Salary)
entry_8.place(x=240,y=370)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=400)

root.mainloop()
