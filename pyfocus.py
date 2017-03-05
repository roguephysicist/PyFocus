#!/usr/bin/env python3
"""
PyFocus.py

Usage:
python pyfocus.py <dngfile>
"""

import sys
import io
import exiftool
from rawkit.raw import Raw
from PIL import Image, ImageDraw

from PentaxK50 import *

def create_img_object(file, scale):
    """ extracts the jpg preview from RAW file, places in buffer, then as pillow image """
    with Raw(filename=file) as raw:
        img = Image.open(io.BytesIO(raw.thumbnail_to_buffer())).convert('RGBA')
    resize_dims = list(map(int, (i * scale for i in img.size)))
    img = img.resize(resize_dims)
    return img

def get_active_points(file):
    """ gets the active AF points from the RAW file EXIF information """
    with exiftool.ExifTool() as exif:
        afpoints = exif.get_tag('MakerNotes:AFPointsInFocus', file)
    points = names[afpoints].split(', ')
    return points

def draw_overlay(array, color):
    """ creates a transparent image and draws the AF points at their assigned spots """
    over = Image.new('RGBA', WORKSIZE, (0, 0, 0, 0))
    for key in array:
        draw_rectangle(over, key, color)
    return over

def draw_rectangle(overlay, key, color):
    """ draws a rectangle at each designated AF spot """
    draw = ImageDraw.Draw(overlay)
    for pttype in locations[key][2]:
        ptcent = [WORKSIZE[0]*locations[key][0], WORKSIZE[1]*locations[key][1]]
        ptsize = [WORKSIZE[0]*interface[pttype][0]*0.5, WORKSIZE[1]*interface[pttype][1]*0.5]
        coord1 = [ptcent[0]-ptsize[0], ptcent[1]-ptsize[1]]
        coord2 = [ptcent[0]+ptsize[0], ptcent[1]+ptsize[1]]
        if interface[pttype][2] == 'color':
            draw.rectangle([coord1[0], coord1[1], coord2[0], coord2[1]], fill=color)
        elif interface[pttype][2] == 'transparent':
            draw.rectangle([coord1[0], coord1[1], coord2[0], coord2[1]], fill=(0, 0, 0, 0))
    del draw


FILE = sys.argv[1]
OUT = FILE.split('.')[0] + '_afpoints.jpg'
SCALE = 0.25

IMG = create_img_object(FILE, SCALE) # returns a pillow image object, resized by some scale
WORKSIZE = IMG.size
ACTIVE_POINTS = get_active_points(FILE) # returns a list with the active AF point names

INACTIVE = draw_overlay(locations, (0, 0, 0, 128)) # overlay with inactive points
ACTIVE = draw_overlay(ACTIVE_POINTS, 'red') #  overlay with active points

OVERLAY = Image.alpha_composite(INACTIVE, ACTIVE) # composites both active and inactive overlays
FINAL = Image.alpha_composite(IMG, OVERLAY) # composites the final overlay with the image
FINAL.save(OUT) # saves to file
