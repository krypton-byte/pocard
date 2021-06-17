from PIL import ImageFont, ImageDraw, Image
def patternResCustom(x, y, res=1280):
    if x==y:
        return [res, res]
    elif x>y:
        return [res,int(y/(x/res))]
    elif x<y:
        return  [int(x/(y/res)),res]
"""img=Image.open("assets/1.png")
draw=ImageDraw.Draw(img)
font=ImageFont.truetype("font/solid.ttf", 20)
draw.text((99,28), "Pikachu Kryptonb", font=font, color=(0,0,0))
desc = ImageFont.truetype("font/desc.ttf", 14)
draw.text((32,316), "Pikach896783u Kryptonb1234567890123456789082627", font=desc, color=(0,0,0))
for i in range(1, 9):
    draw.text((32,316+(21*i)), "Pikach896783u Kryptonb1234567890123456789082627", font=desc, color=(0,0,0))
print(desc.getsize("Pikach896783u Kryptonb1234567890123456789082627"))
img.show()"""
"""img=Image.open("assets/2.jpeg")
dr =Image.new("RGBA",(582, 414), color=(0, 0, 0))
print(img)
draw=ImageDraw.Draw(img)
font=ImageFont.truetype("font/solid.ttf", 30)
print(font.getsize("a1b2c3d4e5f6783hshjGTYCFvgh6g7h8"))
draw.text((96,950), "a1b2c3d4e5f6783hshjGTYCFvgh6g7h8", font=font, color=(0,0,0))
desc = ImageFont.truetype("font/desc.ttf", 30)
print("desk: "+str(desc.getsize("a1b2c3d4e78677575f6783hshjGTYCFvgh6g7h8")))
for i in range(6):
    draw.text((68,630+(36*i)), "a1b2c3d4e78677575f6783hshjGTYCFvgh6g7h8", font=desc, color=(0,0,0))
img.paste(dr, (87, 132))
img.resize(tuple(patternResCustom(*img.size, res=800))).show()"""
img=Image.open("assets/4.png")
dr =Image.new("RGBA",(347, 230), color=(0, 0, 0))
print(img)
draw=ImageDraw.Draw(img)
font=ImageFont.truetype("font/solid.ttf", 17)
print(font.getsize("POKEMON NAGA AIRY"))
draw.text((106,28), "POKEMON NAGA AIRY", font=font, color=(0,0,0))

"""desc = ImageFont.truetype("font/desc.ttf", 15)
print("desk: "+str(desc.getsize("a1b2c3d4e78677575f6783hshjGTYCF0000vgh6g7h8")))
for i in range(10):
    draw.text((30,320+(18*i)), "a1b2c3d4e78677575f6783hshjGTYCFv0000gh6g7h8", font=desc, color=(0,0,0))"""
img.paste(dr, (37, 61))
img.resize(tuple(patternResCustom(*img.size, res=800))).show()
