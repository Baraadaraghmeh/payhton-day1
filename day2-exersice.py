#q1...............................................
num1=int(input("first number:"))
num2=int(input("second number:"))
if num1>num2:
    print("num1 is max")
else:
    print("num2 is max")
#q2.................................................
n=int(input("enter number:"))
for a in range(11):    
    print(a*n)
#q3.................................................
for x in range(6):
  for y in range (x):
     print ('*',end='')
  print() 
for a in range (5,1,-1):
    for b in range(0,a-1 ):
        print ('*',end='')
    print()    
#q4 ..................................................
letters=['x','y','z','a','b','c']
for i in letters:
    if i=='a':
        continue
    elif i=='c':
        break
    print(i)
"""
output:
x
y
z
b
"""
#q5............................................................. 
for x in range(12,25,3):
    print(x)
    """
    output:
12
15
18
21
24
"""
#q6..............................................................
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
    """
    output:
        1
        2
        3
        """
#q7...............................................................
num=int(input("enter a number"))
sum=0
for a in range(0,num,1):
    sum+=a
print(sum)
#q8................................................................
num=int(input("enter a number:"))
if num%2==0:
    print("even number")
else:
    print("odd number")
#q9..............................................................

            
 
    
    
    
    
    
    
    
    
    
    
#q10..................................................................
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n) 
        break 
    except ValueError: 
        print("No valid integer! Please try again ...")
    print("Great, you successfully entered an integer!")

    
#q11....................................................................
while True:    
    try:
     a=3
     if a<4:
        b=a/(a-3)
     print("value of b=",b)
    except(ZeroDivisionError,NameError):
     print("\nError Occured and Handled")
       """
       output:
          Error Occured and Handled 
           
           """






















        
      
      


















