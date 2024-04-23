# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 768)
        MainWindow.setStyleSheet(u"background-color: rgb(56, 57, 52);")
        self.verticalLayoutWidget = QWidget(MainWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1261, 751))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"font/logo.png"))

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.home = QPushButton(self.verticalLayoutWidget)
        self.home.setObjectName(u"home")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy)
        self.home.setMinimumSize(QSize(80, 80))
        self.home.setMaximumSize(QSize(80, 80))
        self.home.setLayoutDirection(Qt.LeftToRight)
        self.home.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        icon = QIcon()
        icon.addFile(u"font/\u4e3b\u9875.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home.setIcon(icon)
        self.home.setIconSize(QSize(60, 60))

        self.horizontalLayout.addWidget(self.home)

        self.config = QPushButton(self.verticalLayoutWidget)
        self.config.setObjectName(u"config")
        sizePolicy.setHeightForWidth(self.config.sizePolicy().hasHeightForWidth())
        self.config.setSizePolicy(sizePolicy)
        self.config.setMinimumSize(QSize(80, 80))
        self.config.setMaximumSize(QSize(80, 80))
        self.config.setLayoutDirection(Qt.LeftToRight)
        self.config.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        icon1 = QIcon()
        icon1.addFile(u"font/\u8bbe\u7f6e.png", QSize(), QIcon.Normal, QIcon.Off)
        self.config.setIcon(icon1)
        self.config.setIconSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.config)

        self.exit = QPushButton(self.verticalLayoutWidget)
        self.exit.setObjectName(u"exit")
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QSize(80, 80))
        self.exit.setMaximumSize(QSize(80, 80))
        self.exit.setLayoutDirection(Qt.LeftToRight)
        self.exit.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        icon2 = QIcon()
        iconThemeName = u"face-laugh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"font/\u9000\u51fa.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit.setIcon(icon2)
        self.exit.setIconSize(QSize(70, 70))

        self.horizontalLayout.addWidget(self.exit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setMinimumSize(QSize(1020, 0))
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.groupBox_2 = QGroupBox(self.page_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, -1, 1001, 211))
        self.groupBox_2.setStyleSheet(u"QGroupBox\n"
"{\n"
"	\n"
"	background-color: transparent;\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	color: rgb(131, 131, 131);\n"
"	border-radius:10px;\n"
"	border:2px solid gray;\n"
"}")
        self.stream_file_list = QComboBox(self.groupBox_2)
        self.stream_file_list.setObjectName(u"stream_file_list")
        self.stream_file_list.setGeometry(QRect(140, 80, 651, 40))
        self.stream_file_list.setMinimumSize(QSize(0, 40))
        self.stream_file_list.setMaximumSize(QSize(16777215, 40))
        self.stream_file_list.setMouseTracking(False)
        self.stream_file_list.setTabletTracking(False)
        self.stream_file_list.setAcceptDrops(False)
        self.stream_file_list.setLayoutDirection(Qt.LeftToRight)
        self.stream_file_list.setAutoFillBackground(False)
        self.stream_file_list.setStyleSheet(u"QComboBox::down-arrow\n"
"{\n"
"	/*image:url(:/font/down-arrow.png);*/\n"
"}\n"
"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	background-color:transparent;\n"
"	border:2px solid gray;\n"
"	border-radius:15px;\n"
"}\n"
"QComboBox::drop-down \n"
"{\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 50px;\n"
"}\n"
"\n"
"  QComboBox QAbstractItemView{\n"
"  border:2px solid gray;\n"
"  border-radius:3px;\n"
"	background-color:rgb(56, 57, 52);\n"
"    outline: 0px;  \n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"	height:36px;\n"
"	color:white;\n"
"	padding-left:0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected{\n"
"  background-color:#97BE15;\n"
"  color:#ffffff;\n"
"  border:2px solid gray;\n"
"  border-radius:15px;\n"
"}")
        self.stream_file_list.setEditable(True)
        self.stream_file_list.setMaxVisibleItems(5)
        self.stream_file_list.setMaxCount(10)
        self.stream_file_list.setIconSize(QSize(30, 30))
        self.stream_file_list.setDuplicatesEnabled(False)
        self.stream_file_list.setFrame(True)
        self.open_stream_file = QPushButton(self.groupBox_2)
        self.open_stream_file.setObjectName(u"open_stream_file")
        self.open_stream_file.setGeometry(QRect(840, 70, 60, 60))
        sizePolicy.setHeightForWidth(self.open_stream_file.sizePolicy().hasHeightForWidth())
        self.open_stream_file.setSizePolicy(sizePolicy)
        self.open_stream_file.setMinimumSize(QSize(60, 60))
        self.open_stream_file.setMaximumSize(QSize(60, 60))
        self.open_stream_file.setLayoutDirection(Qt.LeftToRight)
        self.open_stream_file.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        icon3 = QIcon()
        iconThemeName = u"face-laugh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u"font/\u641c\u7d22.png", QSize(), QIcon.Normal, QIcon.Off)

        self.open_stream_file.setIcon(icon3)
        self.open_stream_file.setIconSize(QSize(60, 60))
        self.groupBox_4 = QGroupBox(self.page_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(9, 219, 1001, 351))
        self.groupBox_4.setStyleSheet(u"QGroupBox\n"
"{\n"
"	\n"
"	background-color: transparent;\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	color: rgb(131, 131, 131);\n"
"	border-radius:10px;\n"
"	border:2px solid gray;\n"
"}")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 111, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 151, 151);")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 120, 91, 21))
        self.label_6.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 151, 151);")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 180, 91, 21))
        self.label_7.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 151, 151);")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 280, 91, 21))
        self.label_8.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 151, 151);")
        self.conf = QSlider(self.groupBox_4)
        self.conf.setObjectName(u"conf")
        self.conf.setGeometry(QRect(140, 280, 651, 16))
        self.conf.setStyleSheet(u"QSlider::groove:horizontal\n"
"{\n"
"    height: 10px;\n"
"    background: #C0C0C0;\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"    padding-left:-1px;\n"
"    padding-right:-1px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: white; /* \u6ed1\u5757\u7684\u80cc\u666f\u8272 */\n"
"    border: 1px solid #5c5c5c; /* \u6ed1\u5757\u7684\u8fb9\u6846\u6837\u5f0f */\n"
"    width: 15px; /* \u6ed1\u5757\u7684\u5bbd\u5ea6 */\n"
"    margin: -4px 0; /* \u6ed1\u5757\u4e0e\u8f68\u9053\u7684\u95f4\u8ddd */\n"
"    border-radius: 7px; /* \u6ed1\u5757\u7684\u5706\u89d2\u534a\u5f84 */\n"
"}\n"
"QSlider::sub-page:horizontal\n"
"{\n"
"    height: 10px;\n"
"    background:  #97BE15;\n"
"    border: none ;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"// \u8fd8\u6ca1\u5212\u8fc7\u7684\u5730\u65b9\n"
"QSlider::add-page:horizontal\n"
"{\n"
"    height: 10px;\n"
"    background: #gray;\n"
"    border: 0px solid ;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"")
        self.conf.setMaximum(100)
        self.conf.setSingleStep(1)
        self.conf.setValue(70)
        self.conf.setOrientation(Qt.Horizontal)
        self.conf_value = QLabel(self.groupBox_4)
        self.conf_value.setObjectName(u"conf_value")
        self.conf_value.setGeometry(QRect(830, 280, 91, 20))
        self.conf_value.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 151, 151);")
        self.open_weight_file = QPushButton(self.groupBox_4)
        self.open_weight_file.setObjectName(u"open_weight_file")
        self.open_weight_file.setGeometry(QRect(840, 30, 60, 60))
        sizePolicy.setHeightForWidth(self.open_weight_file.sizePolicy().hasHeightForWidth())
        self.open_weight_file.setSizePolicy(sizePolicy)
        self.open_weight_file.setMinimumSize(QSize(60, 60))
        self.open_weight_file.setMaximumSize(QSize(60, 60))
        self.open_weight_file.setLayoutDirection(Qt.LeftToRight)
        self.open_weight_file.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        self.open_weight_file.setIcon(icon3)
        self.open_weight_file.setIconSize(QSize(60, 60))
        self.weight_file_list = QComboBox(self.groupBox_4)
        self.weight_file_list.addItem("")
        self.weight_file_list.addItem("")
        self.weight_file_list.addItem("")
        self.weight_file_list.setObjectName(u"weight_file_list")
        self.weight_file_list.setGeometry(QRect(140, 40, 651, 40))
        self.weight_file_list.setMinimumSize(QSize(0, 40))
        self.weight_file_list.setMaximumSize(QSize(16777215, 40))
        self.weight_file_list.setMouseTracking(False)
        self.weight_file_list.setTabletTracking(False)
        self.weight_file_list.setAcceptDrops(False)
        self.weight_file_list.setLayoutDirection(Qt.LeftToRight)
        self.weight_file_list.setAutoFillBackground(False)
        self.weight_file_list.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	background-color:transparent;\n"
"	border:2px solid gray;\n"
"	border-radius:15px;\n"
"}\n"
"QComboBox::drop-down \n"
"{\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 50px;\n"
"}\n"
"QComboBox::down-arrow\n"
"{\n"
"	/*image:url(:/font/down-arrow.png);*/\n"
"}\n"
"  QComboBox QAbstractItemView{\n"
"  border:2px solid gray;\n"
"  border-radius:3px;\n"
"	background-color:rgb(56, 57, 52);\n"
"    outline: 0px;  \n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"	height:36px;\n"
"	color:white;\n"
"	padding-left:0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected{\n"
"  background-color:#97BE15;\n"
"  color:#ffffff;\n"
"  border:2px solid gray;\n"
"  border-radius:15px;\n"
"}")
        self.weight_file_list.setEditable(False)
        self.weight_file_list.setIconSize(QSize(30, 30))
        self.weight_file_list.setDuplicatesEnabled(False)
        self.weight_file_list.setFrame(True)
        self.horizontalLayoutWidget = QWidget(self.groupBox_4)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(140, 110, 741, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.GPU = QCheckBox(self.horizontalLayoutWidget)
        self.GPU.setObjectName(u"GPU")
        self.GPU.setStyleSheet(u"QCheckBox {\n"
"color: white; \n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"}\n"
"QCheckBox::indicator {\n"
"width: 20px; \n"
"height: 20px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	background-color: rgb(151, 190, 21);\n"
"border: 2px solid  rgb(200\uff0c200\uff0c200);\n"
"border-radius:5px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: white;\n"
"border: 2px solid rgb(200\uff0c200\uff0c200);\n"
"border-radius:5px\n"
" }")
        self.GPU.setChecked(True)

        self.horizontalLayout_4.addWidget(self.GPU)

        self.CPU = QCheckBox(self.horizontalLayoutWidget)
        self.CPU.setObjectName(u"CPU")
        self.CPU.setStyleSheet(u"QCheckBox {\n"
"color: white; \n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"}\n"
"QCheckBox::indicator {\n"
"width: 20px; \n"
"height: 20px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	background-color: rgb(151, 190, 21);\n"
"border: 2px solid  rgb(200\uff0c200\uff0c200);\n"
"border-radius:5px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: white;\n"
"border: 2px solid rgb(200\uff0c200\uff0c200);\n"
"border-radius:5px\n"
" }")

        self.horizontalLayout_4.addWidget(self.CPU)

        self.imgsz = QLineEdit(self.groupBox_4)
        self.imgsz.setObjectName(u"imgsz")
        self.imgsz.setGeometry(QRect(140, 180, 113, 31))
        self.imgsz.setLayoutDirection(Qt.LeftToRight)
        self.imgsz.setStyleSheet(u"border:2px solid gray;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"border-radius:4px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"")
        self.imgsz.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_2 = QWidget(self.page_5)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(9, 570, 1001, 94))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color:transparent;\n"
"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 190, 21);")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.stream_import = QPushButton(self.horizontalLayoutWidget_2)
        self.stream_import.setObjectName(u"stream_import")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stream_import.sizePolicy().hasHeightForWidth())
        self.stream_import.setSizePolicy(sizePolicy2)
        self.stream_import.setMinimumSize(QSize(60, 60))
        self.stream_import.setMaximumSize(QSize(60, 60))
        self.stream_import.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        icon4 = QIcon()
        icon4.addFile(u"font/\u8fdb\u5165.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stream_import.setIcon(icon4)
        self.stream_import.setIconSize(QSize(60, 60))

        self.horizontalLayout_10.addWidget(self.stream_import)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.groupBox_3 = QGroupBox(self.page_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(9, -1, 1001, 651))
        self.groupBox_3.setStyleSheet(u"QGroupBox\n"
"{\n"
"	\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	color: rgb(131, 131, 131);\n"
"	border-radius:10px;\n"
"	border:2px solid gray;\n"
"}")
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 19, 981, 621))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.annotated_image = QLabel(self.verticalLayoutWidget_3)
        self.annotated_image.setObjectName(u"annotated_image")
        sizePolicy2.setHeightForWidth(self.annotated_image.sizePolicy().hasHeightForWidth())
        self.annotated_image.setSizePolicy(sizePolicy2)
        self.annotated_image.setMinimumSize(QSize(960, 540))
        self.annotated_image.setStyleSheet(u"color: rgb(115, 115, 115);\n"
"font: 700 14pt \"Microsoft YaHei UI\";")
        self.annotated_image.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.annotated_image, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 10, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.box = QCheckBox(self.verticalLayoutWidget_3)
        self.box.setObjectName(u"box")
        self.box.setStyleSheet(u"QCheckBox {\n"
"color: white; \n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"}\n"
"QCheckBox::indicator {\n"
"width: 20px; \n"
"height: 20px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	background-color: rgb(151, 190, 21);\n"
"border: 2px solid  rgb(56, 57, 52);\n"
"border-radius:5px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: white;\n"
"border: 2px solid rgb(56, 57, 52);\n"
"border-radius:5px\n"
" }")
        self.box.setIconSize(QSize(40, 40))
        self.box.setChecked(True)

        self.horizontalLayout_3.addWidget(self.box)

        self.Label = QCheckBox(self.verticalLayoutWidget_3)
        self.Label.setObjectName(u"Label")
        self.Label.setStyleSheet(u"QCheckBox {\n"
"color: white; \n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"}\n"
"QCheckBox::indicator {\n"
"width: 20px; \n"
"height: 20px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	background-color: rgb(151, 190, 21);\n"
"border: 2px solid  rgb(56, 57, 52);\n"
"border-radius:5px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: white;\n"
"border: 2px solid rgb(56, 57, 52);\n"
"border-radius:5px\n"
" }")
        self.Label.setChecked(True)

        self.horizontalLayout_3.addWidget(self.Label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_6)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox\n"
"{\n"
"	\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	color: rgb(131, 131, 131);\n"
"	border-radius:10px;\n"
"	border:2px solid gray;\n"
"}")
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 21, 221, 630))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color:transparent;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 190, 21);")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.num_weight = QLabel(self.verticalLayoutWidget_2)
        self.num_weight.setObjectName(u"num_weight")
        sizePolicy2.setHeightForWidth(self.num_weight.sizePolicy().hasHeightForWidth())
        self.num_weight.setSizePolicy(sizePolicy2)
        self.num_weight.setMinimumSize(QSize(50, 50))
        self.num_weight.setMaximumSize(QSize(150, 50))
        self.num_weight.setStyleSheet(u"border:2px solid gray;\n"
"border-radius:15px;\n"
"background-color:transparent;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"")
        self.num_weight.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.num_weight)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, -1, 10, -1)
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color:transparent;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 190, 21);")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.total_mass = QLabel(self.verticalLayoutWidget_2)
        self.total_mass.setObjectName(u"total_mass")
        sizePolicy2.setHeightForWidth(self.total_mass.sizePolicy().hasHeightForWidth())
        self.total_mass.setSizePolicy(sizePolicy2)
        self.total_mass.setMinimumSize(QSize(50, 50))
        self.total_mass.setMaximumSize(QSize(150, 50))
        self.total_mass.setStyleSheet(u"border:2px solid gray;\n"
"border-radius:15px;\n"
"background-color:transparent;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"")
        self.total_mass.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.total_mass)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, -1, 10, -1)
        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color:transparent;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 190, 21);")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.total_mass_L = QLabel(self.verticalLayoutWidget_2)
        self.total_mass_L.setObjectName(u"total_mass_L")
        sizePolicy2.setHeightForWidth(self.total_mass_L.sizePolicy().hasHeightForWidth())
        self.total_mass_L.setSizePolicy(sizePolicy2)
        self.total_mass_L.setMinimumSize(QSize(50, 50))
        self.total_mass_L.setMaximumSize(QSize(150, 50))
        self.total_mass_L.setStyleSheet(u"border:2px solid gray;\n"
"border-radius:15px;\n"
"background-color:transparent;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"")
        self.total_mass_L.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.total_mass_L)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, -1, 10, -1)
        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background-color:transparent;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 190, 21);")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.total_mass_R = QLabel(self.verticalLayoutWidget_2)
        self.total_mass_R.setObjectName(u"total_mass_R")
        sizePolicy2.setHeightForWidth(self.total_mass_R.sizePolicy().hasHeightForWidth())
        self.total_mass_R.setSizePolicy(sizePolicy2)
        self.total_mass_R.setMinimumSize(QSize(50, 50))
        self.total_mass_R.setMaximumSize(QSize(150, 50))
        self.total_mass_R.setStyleSheet(u"border:2px solid gray;\n"
"border-radius:15px;\n"
"background-color:transparent;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"")
        self.total_mass_R.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.total_mass_R)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.groupBox_5 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.groupBox_5.setMinimumSize(QSize(0, 300))
        self.groupBox_5.setStyleSheet(u"color: rgb(151, 190, 21);\n"
"font: 12pt \"Microsoft YaHei UI\";")
        self.warming_info = QLabel(self.groupBox_5)
        self.warming_info.setObjectName(u"warming_info")
        self.warming_info.setGeometry(QRect(10, 20, 181, 271))
        self.warming_info.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft YaHei UI\";")
        self.warming_info.setAlignment(Qt.AlignCenter)
        self.warming_info.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.groupBox_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, -1, 10, 10)
        self.warming_alarm = QLabel(self.verticalLayoutWidget_2)
        self.warming_alarm.setObjectName(u"warming_alarm")
        sizePolicy2.setHeightForWidth(self.warming_alarm.sizePolicy().hasHeightForWidth())
        self.warming_alarm.setSizePolicy(sizePolicy2)
        self.warming_alarm.setMinimumSize(QSize(50, 50))
        self.warming_alarm.setMaximumSize(QSize(50, 50))
        self.warming_alarm.setStyleSheet(u"background-color:transparent;\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 190, 21);")
        self.warming_alarm.setPixmap(QPixmap(u"font/\u7eff\u706f.png"))
        self.warming_alarm.setScaledContents(True)
        self.warming_alarm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.warming_alarm)

        self.label_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color:transparent;\n"
"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color: rgb(151, 190, 21);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_15)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.home.setText("")
        self.config.setText("")
        self.exit.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u6d41\u5bfc\u5165", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u63a8\u7406\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6743\u91cd\u6587\u4ef6", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u7406\u8bbe\u5907", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5c3a\u5bf8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u7406\u7f6e\u4fe1\u5ea6", None))
        self.conf_value.setText(QCoreApplication.translate("MainWindow", u"0.70", None))
        self.weight_file_list.setItemText(0, QCoreApplication.translate("MainWindow", u"../../utils/best_FP16.engine", None))
        self.weight_file_list.setItemText(1, QCoreApplication.translate("MainWindow", u"D:\\Download\\best.pt", None))
        self.weight_file_list.setItemText(2, QCoreApplication.translate("MainWindow", u"../../utils/best.pt", None))

        self.GPU.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.CPU.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.imgsz.setText(QCoreApplication.translate("MainWindow", u"640", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u542f   \u52a8", None))
        self.stream_import.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u9884\u89c8", None))
        self.annotated_image.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u5f85\u89c6\u9891\u6d41\u5bfc\u5165...", None))
        self.box.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u6846", None))
        self.Label.setText(QCoreApplication.translate("MainWindow", u"\u6807\u7b7e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u663e\u793a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u914d\u91cd\u603b\u6570\u91cf", None))
        self.num_weight.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u914d\u91cd\u603b\u91cd\u91cf(t)", None))
        self.total_mass.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u4fa7\u603b\u91cd\u91cf(t)", None))
        self.total_mass_L.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u4fa7\u603b\u91cd\u91cf(t)", None))
        self.total_mass_R.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u9884\u8b66\u4fe1\u606f", None))
        self.warming_info.setText("")
        self.warming_alarm.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u72b6\u6001", None))
    # retranslateUi

