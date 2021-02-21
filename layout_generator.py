#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
from keycodes import KEYCODES
import json

KEY_WIDTH = 50
NUM_COLS = 12
NUM_ROWS = 5
KEYBOARD_GUTTER = 10
TITLE_GUTTER = 30
IMAGE_PADDING = 10
KEY_GUTTER = 5
TTF_FONT_PATH = '/usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf'
FONT_SIZE = 10

keyboard_width = KEY_WIDTH * NUM_COLS + (NUM_COLS - 1) * KEY_GUTTER
keyboard_height = KEY_WIDTH * NUM_ROWS + (NUM_ROWS - 1) * KEY_GUTTER

with open('keymap.json', 'r') as f:
    keyboard = json.loads(f.read())

layer_count = len(keyboard['layers'])
image_width = keyboard_width + IMAGE_PADDING * 2
image_height = keyboard_height * layer_count + (layer_count - 1) * KEYBOARD_GUTTER + (layer_count - 1) * KEY_GUTTER + IMAGE_PADDING * 2 + layer_count * TITLE_GUTTER

layout_image = Image.new('RGB', (image_width, image_height), color = 'white')
key_image = Image.open('key.png')
draw = ImageDraw.Draw(layout_image)
font = ImageFont.truetype(TTF_FONT_PATH, FONT_SIZE)

def draw_key(x, y, keycode):
    text = KEYCODES[keycode]
    try:
        text = KEYCODES[keycode]
    except KeyError:
        text = keycode

    layout_image.paste(key_image, (x, y))

    text_width, text_height = draw.textsize(text)
    text_x = x + KEY_WIDTH / 2 - text_width / 2
    text_y = y + KEY_WIDTH / 2 - text_height / 2

    draw.text((text_x, text_y), text, fill=(0,0,0,128), font=font, align='center')

x = IMAGE_PADDING
y = IMAGE_PADDING

for layer_idx in range(0, len(keyboard['layers'])):
    text = 'Layer %d' % layer_idx
    layer = keyboard['layers'][layer_idx]

    text_width, text_height = draw.textsize(text)
    text_x = image_width / 2 - text_width / 2

    draw.text((text_x, y), text, fill=(0,0,0,128), font=font, align='center')

    y += TITLE_GUTTER

    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            text = layer.pop(0)
            draw_key(x, y, text)
            x += KEY_WIDTH + KEY_GUTTER
        x = IMAGE_PADDING
        y += KEY_WIDTH + KEY_GUTTER
    y += KEYBOARD_GUTTER

layout_image.save('layout.png')
