import statistics as st
import random
import math
from PIL import Image,ImageDraw,ImageFilter
x=[1,1.5,4.5,6.75,2.25,5.75,2.25]
print(st.mean(x))    
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.stdev(x))
print(st.variance(x))
print("Q2...................................")
#q2..............................................
print( random.random()) 
print ( random.randrange(10))
print ( random.choice(['Ali','Khalid','Hussam']))
print ( random.sample(range(1000), 10) )
x= [1, 5, 8, 9, 2, 4] 
random.shuffle(x) 
print(x) 
print ( random.randrange(20,30))
print(random.randrange(1000,2111,5))
print(random.uniform(10000,11000))
#q3................................................
print("Q3...................................")
print(math.pi)
print(math.cos(200))
print(math.sin(30))
print(math.tan(180))
n=10.8
print(math.floor(n))
print(math.ceil(n))
#q4....................................................
print("Q4............................................")
x=Image.open("car.JPG")
print(x.format,x.size,x.mode)
x.show()
image_flip=x.transpose(x.FLIP_TOP_BOTTOM)
image_flip.show()
grayscale_image=x.convert('L')
grayscale_image.show()
crop=x.crop((0,0,50,50))
crop.show()
draw=ImageDraw.Draw(x)
draw.line((0,0)+x.size,fill=(255,255,255))
draw.line((0,x.size[1],x.size[0],0),fill=(255,255,255))
draw.text((x.size[0]/2-x.size[0]/2,x.size[1]/2+20),"Baraa",fill=(255,255,0))
x.show()

#.................................................
new=x.filter(ImageFilter.EDGE_ENHANCE)
new.show()
#.................................................
new=x.filter(ImageFilter.FIND_EDGES)
new.show()
#................................................
new=x.filter(ImageFilter.SMOOTH)
new.show()
#................................................
new=x.filter(ImageFilter.SHARPEN)
new.show()
#................................................
alpha=0.5
x2=Image.open("car2.JPG").resize(x.size)
Image.blend(x,x2,alpha).save("New.JPG".format(alpha))
x=Image.open("New.JPG")
x.show()
#.................................................
blurred=x.filter(ImageFilter.BLUR)
#blurred.show()
#.................................................
size=(128,128)
x.thumbnail(size)
x.show()
#.................................................
rot=x.rotate(90)
rot.show()
#.................................................
#im2= x2.resize(x.size)
mask=Image.open("maskie.png")
mask=mask.resize(x.size)
Image.composite(x,x2,mask).save("image_composite_sawsan.jpg")
new=Image.open("image_composite_sawsan.jpg")
new.show()









































