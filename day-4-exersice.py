o=lambda x=1,y=2,z=3:x+y+z
print(o())
print(o(10))
print(o(10,20))
"""output:
    6
    15
    33
"""
#q2.......................................................
from functools import reduce 
x= reduce(lambda a,b: a*b,[1,2,3,4]) 
print(x)
        
#q3........................................................
x=(lambda x,y:x*y)(3,5)
print(x)      
#q4........................................................
negative_numbers=list(filter(lambda x:x<0,range(-5,5)))
print("Negative",negative_numbers)
#q5........................................................
x=lambda a,b,c:a+b+c
print(x(5,6,2))
"""output: 13

"""
#q6.........................................................
x=("Joy","Monica","Ross")
y=("Chandler","Pheobe")
z=("David","Rachel","Courtney")
result=list(zip(x,y,z))
print(result)
"""Output:
    [('Joy', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]
    """
#q7..........................................................
coin=("Bitcoin","Ether","Ripple","Litcoin")
code=("BTC","ETH","XRP","LTC")  
d=dict(zip(coin,code))
print(d)
"""
Output:
    {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litcoin': 'LTC'}
"""
#q8....................................................................
def fun(variables):
    letters=["a","e","i","o","u"]
    if (variables in letters):
        return True
    else:
        return False
sequence=['g','j','e','j','k','o','p','r']   
filterd=list(filter(fun,sequence))
print(filterd)
"""Output:
    ['e','o']
    """
#q9......................................................................
x=list(map(int,input("Enter a multiple value").split()))   
print("List of student:",x)
#q10....................................................................
def newfunc(a):
    return a*a
x=list(map(newfunc,(1,2,3,4,5)))
print(x)
"""
output:
    [1, 4, 9, 16, 25]
    """
#q11..................................................................
def func (a,b):
    return a+b
a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)
"""output:
    [3,6,8]
    """
#q12...................................................................
c=map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3,4)))
print(list(c))
"""
output:
    [6,8]
    """
#q13....................................................................
c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
print(list(c))
"""
output:[4, 6, 8]
"""
#q14.......................................................................
from functools import reduce 
x= reduce(lambda a,b: a if a<b else b,[1,2,3,4,5,-1,0]) 
print(x)
#q15....................................................................
num=[1,2,3]
letters=['a','b','c']
result=list(zip(num,letters))
print(result)































    















    


















