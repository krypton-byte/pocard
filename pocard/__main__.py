from . import (
    CARDS,
    Image
    )
from os.path import dirname
import sys
args = sys.argv[1:]
def helper():
    cmd=dirname(__file__).split("/")[-1]
    print(f"{cmd} index:[0-{len(CARDS)-1}] \"title\" \"desc\" \"image_path\" \"output_path\", \"method:[scale, auto, crop]\"")
def execute():
    if args.__len__() == 6:
        try:
            CARDS[int(args[0])].maker(args[1], args[3], args[2], image_method=args[5]).save(args[4])
        except Exception as e:
            print(e)
    else:
        index_card()
def index_card():
    helper()
    print("Index\tSize")
    for i in enumerate(CARDS):
        img=Image.open(dirname(__file__)+"/assets/"+i[1].json["filename"])
        print(f"  {i[0]}\t"+" x ".join(str(x) for x in img.size))
if __name__ == "__main__":
    execute()