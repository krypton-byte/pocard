<p align="center">
<img src="https://i.ibb.co/5WSxMFD/Stiker-Dekorasi-Latar-Belakang-Tubuh-Laptop-Kartun-Kepribadian-Mode-Stiker-Mainan-Klasik-Pokemon-Pik.webp" width="25%">
</p>

# Pokemon Card
# Install This Library

```bash
#Pypi
$ pip3 install pocard
#Github
$ git clone https://github.com/krypton-byte/pocard
$ cd pocard && python3 setup.py build && python3 setup.py install --user
```
# Use
<p>CommandLine<p>

```bash
krypton-byte@glitch:~/pocard$ python3 -m pocard --title a --desc hai --card-2 --CROP --save anu.jpg --image hasil.webp --help
usage: __main__.py [-h] --title TITLE --desc DESC --image IMAGE --save SAVE (--card-0 | --card-1 | --card-2 | --card-3) (--AUTO | --SCALE | --CROP)

options:
  -h, --help     show this help message and exit
  --title TITLE
  --desc DESC
  --image IMAGE
  --save SAVE

CARD:
  --card-0
  --card-1
  --card-2
  --card-3

METHOD:
  --AUTO
  --SCALE
  --CROP

$ python3 -m pocard --title "hello world" --desc "this is description" --image input.jpg --save output.jpg --card-0 --AUTO
```

<p>Python Interpreter</p>

```python
>>> from pocard import CARDS
>>> CARDS[0].maker("Title", "image_input.png", "Desk", font_color=(0, 0, 0), image_method="auto").show()
>>> CARDS[0].maker("Title", "image_input.png", "Desk", font_color=(0, 0, 0), image_method="auto").save("out.png")
# image_input type: BytesIO, Image.open Object, string(path+filename)
# image_method: scale, auto, crop
```
# Preview
<img src="out.png" width="25%"><img src="out1.png" width="25%"><img src="out2.png" width="25%"><img src="out3.png" width="25%">
# Donasi
<p align="center"><img src="https://svgur.com/i/Vtt.svg">

</p>
<ul><li><a href="https://saweria.co/kryptonbyte">Saweria</a><li><a href="https://wa.me/6283172366463">Whatsapp</a></li><li><a href="https://trakteer.id/krypton-byte-z8vbo">Trakteer</a></li></ul>