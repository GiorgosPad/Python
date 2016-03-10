from PIL import Image, ImageDraw
tablex = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tabley = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tabler = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
im = Image.new("RGB", (1024, 1024), "white")
for i in range (1,20):
    x = random.randrange(500,524)
    y = random.randrange(500,524)
    r = random.randrange(10,501)
    tablex[i] = x
    tabley[i] = y
    tabler[i] = r
    draw = ImageDraw.Draw(im)
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,0), outline ='red')
    im.show()
d = 0
for i in range(0,18):
    for j in range(i+1,19):
        if math.sqrt((tablex[i]-tablex[j])^2 + (tabley[i] - tabley[j])^2)<tabler[i] + tabler[j] and math.sqrt((tablex[i]-tablex[j])^2 + (tabley[i] - tabley[j])^2)>math.abs(tabler[i] - tabler[j]):
            d = d + 2
print d
        
        
