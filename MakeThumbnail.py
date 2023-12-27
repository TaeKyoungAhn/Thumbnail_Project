import os
import datetime
import sys
import re
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, date, timedelta
from PySide6.QtWidgets import QApplication, QWidget


def make_thumb2(var_title , width, height, filepath):
    var_max_w = width #이미지 폭
    var_max_h = height #이미지 높이
    var_anchor = "mm"  # middle, middle
    background_folder = filepath + '\Background'
    
    new_str = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", var_title)
       
    currentTime = datetime.now().strftime("%Y%m%d")
    currentTime = datetime.now().strftime("%Y%m%d")
    output_path = filepath + '\Thumbnail' + '\\' + currentTime + '_' + new_str + '.webp'
    thumbnail_size=(var_max_w, var_max_h)
    
    background_images = [os.path.join(background_folder, f) for f in os.listdir(background_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    if not background_images:
        raise ValueError("No valid background images found in the specified folder.")
     # Choose a random background image
    background_image_path = random.choice(background_images) 
    # Open the background image and resize it to the desired thumbnail size
    background = Image.open(background_image_path)
    background = background.resize(thumbnail_size)
    
    var_title_width_length = 7  # 한 라인의 Max 글자 수
    parametor = textwrap.wrap(var_title, width=var_title_width_length)
   
     # Create a blank image with the same size as the background
    thumbnail = Image.new('RGB', thumbnail_size, (255, 255, 255))
    
     # Paste the background image onto the thumbnail
    thumbnail.paste(background, (0, 0))

    # Create a drawing context to add text to the thumbnail
    draw = ImageDraw.Draw(thumbnail, 'RGBA')
    
    rectangle_size = (thumbnail_size[0] - 60, thumbnail_size[1] - 60)
    x1 = (thumbnail_size[0] - rectangle_size[0]) // 2
    y1 = (thumbnail_size[1] - rectangle_size[1]) // 2
    x2 = x1 + rectangle_size[0]
    y2 = y1 + rectangle_size[1]
    

    # Draw the transparent rectangle in the center
    draw.rectangle([x1, y1, x2, y2], fill=(0,0,0,127))
    draw.rectangle([x1, y1, x2, y2], outline=(255, 255, 255), width=10)
    
    var_pad = 10  # 글 간격   
  
    fontpath = filepath + '\Font'
    font = ImageFont.truetype(fontpath + '\KimNamyun.ttf', size=40)
    font_color = 'rgb(255, 255, 255)'
    
    var_stroke_color = "#FFFFFF"
    
    var_len_line = len(parametor)
    var_x_point = var_max_w / 2 
    var_y_point = var_max_h / 2 
    
    var_textsize_h = draw.textsize(parametor[0], font=font)[1]   
    var_y_point = var_y_point - (((var_textsize_h * var_len_line) + (var_pad * (var_len_line - 1))) / 2) + (var_textsize_h / 2)   
    
    for var_line in parametor: 
        draw.text((var_x_point, var_y_point)
        , var_line
        , font_color
        , font=font
        , stroke_width=0
        , stroke_fill=var_stroke_color
        , align="center"
        , anchor=var_anchor) 
        var_y_point = var_y_point + var_textsize_h + var_pad

    # Save the thumbnail image to the specified output path
    thumbnail.save(output_path)
    return output_path


