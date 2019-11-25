class Employee:
    def __init__(self,number,name,address,salary,job):
        self.number=number
        self.__name=name
        self.__address=address
        self.__salary=salary
        self.__job=job
    def getname(self):
        return self.__name
    
    def getaddress(self):
        return self.__address
    
    def setaddress(self,address):
        self.__address=address
        
        
    def getsalary(self):
        return self.__salary
    
    def getjob(self):
        return self.__job
    
    def __del__(self):
        print(self.getname(),"has been deleted")


        

    def employee_info(self):
        print("Employee Information:")
        print('Employee Number:',self.number)
        print('Name: ',self.getname())
        print('Address: ',self.getaddress())
        print('Salary: ',self.getsalary())
        print('Job Title: ',self.getjob())  
        
    def employee_info2(self):
        print("Employee info:",self.number,self.getname(),self.getaddress(),self.getsalary(),self.getjob())
                        
E1=Employee(1,'Mohammad khalid','Amman-Jordan',500,'Consultant')
E2=Employee(2,'Hala Rana','Aqaba-Jordan',750,'Manager')
E1.employee_info()
E2.employee_info2()
E1.setaddress('Usa')
print(E1.getaddress())

del E1
del E2




