# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFontComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.imagePanel = QLabel(self.centralwidget)
        self.imagePanel.setObjectName(u"imagePanel")
        self.imagePanel.setGeometry(QRect(20, 70, 600, 600))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 231, 51))
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(650, 30, 581, 661))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 533, 155))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.titleInput = QLineEdit(self.verticalLayoutWidget)
        self.titleInput.setObjectName(u"titleInput")

        self.horizontalLayout.addWidget(self.titleInput)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_2.addWidget(self.label_8)

        self.widthCombo = QComboBox(self.verticalLayoutWidget)
        self.widthCombo.setObjectName(u"widthCombo")
        self.widthCombo.setMinimumSize(QSize(150, 0))
        self.widthCombo.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_2.addWidget(self.widthCombo)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(100, 100))

        self.horizontalLayout_2.addWidget(self.label_9)

        self.heightCombo = QComboBox(self.verticalLayoutWidget)
        self.heightCombo.setObjectName(u"heightCombo")
        self.heightCombo.setMinimumSize(QSize(150, 0))
        self.heightCombo.setMaximumSize(QSize(150, 100))

        self.horizontalLayout_2.addWidget(self.heightCombo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.customWidth = QLineEdit(self.verticalLayoutWidget)
        self.customWidth.setObjectName(u"customWidth")
        self.customWidth.setMinimumSize(QSize(150, 0))
        self.customWidth.setMaximumSize(QSize(150, 100))

        self.horizontalLayout_3.addWidget(self.customWidth)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.customHeight = QLineEdit(self.verticalLayoutWidget)
        self.customHeight.setObjectName(u"customHeight")
        self.customHeight.setMinimumSize(QSize(150, 0))
        self.customHeight.setMaximumSize(QSize(150, 100))

        self.horizontalLayout_3.addWidget(self.customHeight)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 0))
        self.label_10.setMaximumSize(QSize(100, 16777215))
        self.label_10.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.fontComboBox = QFontComboBox(self.verticalLayoutWidget)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.horizontalLayout_4.addWidget(self.fontComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imagePanel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc378\ub124\uc77c \uc0dd\uc131\ud504\ub85c\uadf8\ub7a8 ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\ucee8\ud2b8\ub864 \ubc15\uc2a4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud0c0\uc774\ud2c0 \uc785\ub825 ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300 15\uae00\uc790\ub97c \uc785\ub825\ud558\uc2e4 \uc218 \uc788\uc2b5\ub2c8\ub2e4.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ube44\uc728 \uc120\ud0dd", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uac00\ub85c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\uc138\ub85c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uc9c1\uc811 \uc785\ub825", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uac00\ub85c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc138\ub85c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\ud3f0\ud2b8 \uc124\uc815", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc378\ub124\uc77c \uc0dd\uc131", None))
    # retranslateUi

