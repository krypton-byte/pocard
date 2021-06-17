#!/usr/bin/env python3
"""
AUTHOR: KRYPTON-BYTE
GITHUB: https://github.com/krypton-byte/


"""
from io import BytesIO
from PIL import (
    Image,
    ImageDraw,
    ImageFont
)
from .ExceptionCard import (
    MethodNotFound
)
from .variable import (
    ASSETS_DIR,
    FONT,
    FONT2,
    TEMPLATE
)


class cardmaker:
    def __init__(self, json_) -> None:
        self.json = json_

    def getBorderColor(self):
        """
        AutoBackgroundColor With Max Count Color
        """
        top = [self.image.getpixel((x, 0)) for x in range(self.image.width-1)]
        right = [self.image.getpixel((self.image.width-1, y)) for y in range(self.image.height-1)]
        bottom = [self.image.getpixel((x, self.image.height-1)) for x in range(self.image.width-1)]
        left = [self.image.getpixel((0, y)) for y in range(self.image.height-1)]
        allcolor = [top, right, bottom, left]
        to_return = []
        for post in allcolor:
            max_color = ()
            colors = post
            for pixel in list(set(post)):
                if colors.count(pixel) > colors.count(max_color):
                    max_color = pixel
            to_return.append(tuple(max_color))
        return to_return

    def patternResCustom(self, x, y, res):
        """
        AutoScale
        """
        if x == y:
            return [res, res]
        elif x > y:
            return [res, int(y/(x/res))]
        elif x < y:
            return [int(x/(y/res)), res]

    def smartAutoCropAndscalling(self, target):
        """
        AutoScale&AddLayerWithAutoBackgroundColor
        """
        min_t = min(target)
        background = Image.new("RGB", tuple(target), (0, 0, 0))
        ret = self.patternResCustom(*self.image.size, res=target[0])
        while(min(ret) >= min(target)):
            min_t -= 1
            ret = self.patternResCustom(*self.image.size, res=min_t)
        space_width = int(background.width/2-ret[0]/2)
        space_height = int(background.height/2-ret[1]/2)
        colorgenerator = self.getBorderColor()
        for x in range(background.height):
            for i in range(space_width):
                background.putpixel((i, x), colorgenerator[3])  # Left
            for y in range(background.width-space_width-1, background.width):
                background.putpixel((y, x), colorgenerator[1])  # Right
        for i in range(background.width):
            for x in range(space_height):
                background.putpixel((i, x), colorgenerator[0])  # Rop
            for y in range(background.height-space_height-1, background.height):
                background.putpixel((i, y), colorgenerator[2])  # Bottom
        background.paste(self.image.resize(tuple(ret)), (
            int(target[0]/2-ret[0]/2), int(target[1]/2-ret[1]/2)
            ))
        return background

    def textmaker(
            self,
            imgDraw,
            img_size,
            cordinate,
            max_size,
            text,
            font,
            color,
            center,
            space_line=1,
            max_line=1):
        """
        Card maker
        """
        data = ""
        plt = []
        for i in text:
            if font.getsize(data)[0] < max_size:
                data += i
            else:
                plt.append(data)
                data = i
        else:
            plt.append(data)
        slicer = plt[:max_line]
        x, y = cordinate
        for i in enumerate(slicer):
            if center:
                imgDraw.text(
                    (img_size[0]/2-font.getsize(i[1])[0]/2, y+(space_line*i[0])),
                    i[1],
                    font=font,
                    fill=color
                )
            else:
                imgDraw.text((x, y+(space_line*i[0])), i[1], font=font, fill=color)

    def maker(
            self,
            title,
            image,
            desc,
            image_method,
            font_color=(0, 0, 0)):
        self.img = Image.open(
            f'{ASSETS_DIR}/{self.json["filename"]}'
        ).convert("RGB")
        self.image = Image.open(image) if isinstance(image, str) or isinstance(image, BytesIO) else image
        if image_method == "auto":
            image = self.smartAutoCropAndscalling(tuple(self.json["config"]["image"]["size"]))
            # image.resize(tuple(self.json["config"]["image"]["size"]))
        elif image_method == "scale":
            image = self.image.resize(tuple(self.json["config"]["image"]["size"]))
        elif image_method == "crop":
            x_target, y_target = self.json["config"]["image"]["size"]
            self.image = self.image.resize(self.patternResCustom(*[min(self.image.size)]*2, res=max(self.json["config"]["image"]["size"])))
            x_original, y_original = self.image.size
            x = (x_original/2)
            y = (y_original/2)
            left = x-(x_target/2)
            right = x+(x_target/2)
            bottom = y+(y_target/2)
            top = y-(y_target/2)
            image = self.image.crop((left, top, right, bottom))
        else:
            raise MethodNotFound("Method Is Invalid")
        self.img.paste(image, tuple(self.json["config"]["image"]["cordinate"]))
        self.textmaker(ImageDraw.Draw(self.img), self.img.size, self.json["config"]["title"]["cordinate"], self.json["config"]["title"]["max_size"], title, ImageFont.truetype(FONT, self.json["config"]["title"]["fontsize"]), color=font_color, center=self.json["config"]["title"]["center"])  # title
        self.textmaker(ImageDraw.Draw(self.img), self.img.size, self.json["config"]["desc"]["cordinate"], self.json["config"]["desc"]["max_size"], desc, ImageFont.truetype(FONT2, self.json["config"]["desc"]["fontsize"]), space_line=self.json["config"]["desc"]["space_line"], max_line=self.json["config"]["desc"]["max_line"], color=font_color, center=self.json["config"]["desc"]["center"])  # desc
        return self.img


CARDS = [cardmaker(i) for i in TEMPLATE]
