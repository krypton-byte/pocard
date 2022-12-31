from . import (
    CARDS,
    Image
    )
from . import Resize
from os.path import dirname
import sys
import argparse
args = argparse.ArgumentParser()
args.add_argument("--title", type=str, required=True)
args.add_argument("--desc", type=str, required=True)
args.add_argument("--image", type=argparse.FileType('rb'), required=True)
args.add_argument("--save", type=argparse.FileType('w'), required=True)
img = args.add_argument_group('CARD')
image=img.add_mutually_exclusive_group(required=True)
for i, v in enumerate(CARDS):
    image.add_argument(f'--card-{i}', const=v, dest='card', action='store_const')
method = args.add_argument_group('METHOD')
method_ = method.add_mutually_exclusive_group(required=True)
for k,v in Resize.__members__.items():
    method_.add_argument(f'--{k}', dest='resize', const=v, action='store_const')
parse = args.parse_args()
parse.card.maker(parse.title, Image.open(parse.image), parse.desc, parse.resize).save(parse.save, format='jpeg')