import os
import datetime
import sys
import re
import random
import textwrap

from typing import Optional
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, date, timedelta
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog, QLineEdit
from mainWinodw import Ui_MainWindow

filePath = "C:\\ThumbnailMaker"
settingsPath= "C:\\ThumbnailMaker\\Settings"

def setSettings():
    global settingsPath
    if not os.path.exists(settingsPath):
        os.makedirs(settingsPath)
    if not os.path.exists(settingsPath + "\\settings.ini"):
        f = open(settingsPath + "\\settings.ini", 'w')
        f.write("font=Arial.ttf\n")
        f.write("font_size=50\n")
        f.write("width=1280\n")
        f.write("height=720\n")
        f.write("background_folder=C:\\ThumbnailMaker\\Background\n")
        f.write("output_folder=C:\\ThumbnailMaker\\Output\n")
        f.close()
    f = open(settingsPath + "\\settings.ini", 'r')
    font = f.readline().split("=")[1].strip()
    font_size = int(f.readline().split("=")[1].strip())
    width = int(f.readline().split("=")[1].strip())
    height = int(f.readline().split("=")[1].strip())
    background_folder = f.readline().split("=")[1].strip()
    output_folder = f.readline().split("=")[1].strip()
    f.close()
    return font, font_size, width, height, background_folder, output_folder



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        setSettings()
        #self.saveFolderPath.clicked.connect(self.saveFilePath) # 저장 경로 버튼
        self.makeThumbnail.clicked.connect(self.make_thumb2)
        
        
        
    def make_thumb2(self):
        var_max_w = self.widthCombo.currentText() #이미지 폭
        maxW = int(var_max_w)
        var_max_h = self.heightCombo.currentText() #이미지 높이
        maxH = int(var_max_h)
        var_anchor = "mm"  # middle, middle
        fontSize = self.sizeFontSpin.value()  #폰트 크기
        background_folder = filePath + '\Background' #배경사진 폴더

        new_str = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", filePath)

        currentTime = datetime.now().strftime("%Y%m%d")
        currentTime = datetime.now().strftime("%Y%m%d")
        output_path = filePath + '\Thumbnail' + '\\' + currentTime + '_' + new_str + '.webp'
        thumbnail_size=(maxW, maxH)

        background_images = [os.path.join(background_folder, f) for f in os.listdir(background_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        if not background_images:
            raise ValueError("No valid background images found in the specified folder.")
         # Choose a random background image
        background_image_path = random.choice(background_images) 
        # Open the background image and resize it to the desired thumbnail size
        background = Image.open(background_image_path)
        background = background.resize(thumbnail_size)

        var_title_width_length = 7  # 한 라인의 Max 글자 수
        parametor = textwrap.wrap(self.titleInput.text(), width=var_title_width_length)
    
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
    
        
        font = ImageFont.truetype(self.fontComboBox.currentFont(), size=fontSize)
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
        pixmap = QPixmap(output_path)
        self.imagePanel.setPixmap(pixmap)

    #배경사진 고르기

    
    
    #사진 저장 위치 고르기
    def saveBackgroundFolder(self):
        global filePath
        filePath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.backgroundFolder.setText(filePath)
        self.make_thumb2()
        
        
        
    
    
    #사진 저장
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()