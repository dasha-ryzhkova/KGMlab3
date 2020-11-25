from PIL import Image, ImageDraw
import math

print("Input path to file:")
f = input()
print("Input path to save picture:")
p = input()
# f = "C:\\Users\\VivoBook\\Desktop\\KGMlab2\\DS5.txt"
# p = "C:\\Users\\VivoBook\\Desktop\\KGMlab2\\test.png"

#n = 5
#angle = 10*(n+1)*pi/180 = 10*6*pi/180
#angle = pi/3


file = open(f, "r")
line = file.readlines()
dot = []
new_cord = []
ox = 480
oy = 480
angle = math.pi/3

for i in line:
    cord_x, cord_y = i.split(" ")
    dot.append(int(cord_x))
    dot.append(int(cord_y))
    qx = ox + math.cos(angle) * (int(cord_x) - ox) - math.sin(angle) * (int(cord_y) - oy)
    qy = oy + math.sin(angle) * (int(cord_x) - ox) + math.cos(angle) * (int(cord_y) - oy)
    new_cord.append(qx)
    new_cord.append(qy)
file.close()


image = Image.new("RGBA", (960, 960), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)
draw.point(dot, fill="black")
draw.point(new_cord, fill="blue")
image.save(p, "PNG")
image.show()




