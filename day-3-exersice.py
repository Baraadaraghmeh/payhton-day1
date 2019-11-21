#q1
list=[1,2,3,4,5,6,7,8]
for x in list:
    print(x)
#q2.............................................
list=[1,2,3,4,5,6,7,8]
for x in list:
    x+=x
print(x)
#q3..............................................
list=[1,2,3,4,5,6,7,8]
print (max(list))
#q4.............................................
a=[10,20,30,20,10,50,60,40,80,50,40]
print(set(a))
#q5..............................................
list=[]
if len(list)==0:
   print("the list is empty")
#q6..............................................
my_tuple=(1,"Ahmad","Baraa",'a',5,6)
for x in my_tuple:
    print(x)
#q7..............................................
num_set = set([0, 1, 2, 3, 4, 5])
for x in num_set:
    print(x)
#q8..............................................
set1={1,2,3,4,5,6}
set2={1,3,5}
print(set1 & set2)
#q9...............................................
setx=set(["green","blue"])
sety=set(["blue","yellow"])
seta=setx | sety
print (seta)
#output={'blue','yellow','green'}
#q10...............................................
seta=set([5,10,3,15,2,20])
print(len(seta))
   #output=6
#q11...............................................
dic={1:10,2:20}
dic1={3:30,4:40}
dic2={5:50,6:60}
dic4={}
for d in (dic,dic1,dic2):
    dic4.update(d)
print(dic4)
#output:{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#q12.................................................
a="Hello,World!"
print(a[1])
print(a[2:5])
print(a[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("H","j"))
"""Output:
e
llo
orl
12
hello,world!
jello,World!    
"""
    
















  