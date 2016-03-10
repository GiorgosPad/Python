from PIL import Image
import ImageDraw
img = Image.open("myimage.jpg")
picture = img.load()
print img.size
print picture[10,100]
x = size.width()
y = size.height()
k = 0
colors = []*(x*y - 1)
times = []*(x*y - 1)
for i in range(1,x):
    for j in range (1,y):
        if i==1 and j==1:
            colors[k]=picture[i,j]
            k = k+1
        else:
            flag = False
            for z in range(0,k-1):
                if colors[k]==picture[i,z]:
                    flag = True
            if flag == False:
                colors[k]=picture[i,j]
                k=k+1
s = len(colors)
for k in range(0,s):
    for i in range(1,x):
        for j in range(1,y):
            if colors[k]==picture[i,j]:
                times[k]= times[k] + 1
for i in range(s-1,0,-1):
    for j in range(i):
        if times[j]<times[j+1]:
            temp = times[j]
            times[j] = times[j+1]
            times[j+1] = temp
            temp2 = colors[j]
            colors[j]= colors[j+1]
            colors[j+1]=temp2
for i in range[0,4]:
    print colors[i]
import Image
import ImageDraw
im = Image.new("P", (400, 400), 0)
im.putpalette([
    colors[0],
    colors[1],
    colors[2],
    colors[3],
    colors[4]
])
                
