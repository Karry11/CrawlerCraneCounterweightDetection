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

        self.exit = QPushButton(self.verticalLayoutWidget)
        self.exit.setObjectName(u"exit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QSize(80, 80))
        self.exit.setMaximumSize(QSize(80, 80))
        self.exit.setLayoutDirection(Qt.LeftToRight)
        self.exit.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        icon = QIcon()
        iconThemeName = u"face-laugh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"font/\u9000\u51fa.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit.setIcon(icon)
        self.exit.setIconSize(QSize(80, 80))

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
        self.stream_file_list.addItem("")
        self.stream_file_list.addItem("")
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
        self.stream_file_list.setEditable(False)
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
        icon1 = QIcon()
        iconThemeName = u"face-laugh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"font/\u641c\u7d22.png", QSize(), QIcon.Normal, QIcon.Off)

        self.open_stream_file.setIcon(icon1)
        self.open_stream_file.setIconSize(QSize(60, 60))
        self.stream_import = QPushButton(self.page_5)
        self.stream_import.setObjectName(u"stream_import")
        self.stream_import.setGeometry(QRect(940, 580, 60, 60))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stream_import.sizePolicy().hasHeightForWidth())
        self.stream_import.setSizePolicy(sizePolicy2)
        self.stream_import.setMinimumSize(QSize(60, 60))
        self.stream_import.setMaximumSize(QSize(60, 60))
        self.stream_import.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        icon2 = QIcon()
        iconThemeName = u"face-laugh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"font/\u8fdb\u5165.png", QSize(), QIcon.Normal, QIcon.Off)

        self.stream_import.setIcon(icon2)
        self.stream_import.setIconSize(QSize(60, 60))
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
        self.conf.setGeometry(QRect(120, 280, 651, 16))
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
        self.conf.setValue(50)
        self.conf.setOrientation(Qt.Horizontal)
        self.conf_value = QLabel(self.groupBox_4)
        self.conf_value.setObjectName(u"conf_value")
        self.conf_value.setGeometry(QRect(820, 280, 91, 20))
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
        self.open_weight_file.setIcon(icon1)
        self.open_weight_file.setIconSize(QSize(60, 60))
        self.weight_file_list = QComboBox(self.groupBox_4)
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
"    color:white;\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    /* \u9009\u62e9\u6846\u5c3a\u5bf8 */\n"
"    width:40px;\n"
"    height:40px;\n"
"}\n"
"")
        self.GPU.setChecked(True)

        self.horizontalLayout_4.addWidget(self.GPU)

        self.CPU = QCheckBox(self.horizontalLayoutWidget)
        self.CPU.setObjectName(u"CPU")
        self.CPU.setStyleSheet(u"QCheckBox {\n"
"    color:white;\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    /* \u9009\u62e9\u6846\u5c3a\u5bf8 */\n"
"    width:40px;\n"
"    height:40px;\n"
"}")

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
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.groupBox_3 = QGroupBox(self.page_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(9, -1, 1001, 641))
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
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 19, 981, 611))
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
        self.stream_reload = QPushButton(self.verticalLayoutWidget_3)
        self.stream_reload.setObjectName(u"stream_reload")
        self.stream_reload.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        icon3 = QIcon()
        icon3.addFile(u"font/\u5de6\u7bad\u5934.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stream_reload.setIcon(icon3)
        self.stream_reload.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.stream_reload)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


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

        self.verticalLayout_2.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.exit.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u6d41\u5bfc\u5165", None))
        self.stream_file_list.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.stream_file_list.setItemText(1, QCoreApplication.translate("MainWindow", u"111111111111111111111111111111", None))

        self.stream_import.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u63a8\u7406\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6743\u91cd\u6587\u4ef6", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u7406\u8bbe\u5907", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5c3a\u5bf8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u7406\u7f6e\u4fe1\u5ea6", None))
        self.conf_value.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weight_file_list.setItemText(0, QCoreApplication.translate("MainWindow", u"D:\\Download\\best.pt", None))

        self.GPU.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.CPU.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.imgsz.setText(QCoreApplication.translate("MainWindow", u"640", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u9884\u89c8", None))
        self.annotated_image.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stream_reload.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u663e\u793a", None))
    # retranslateUi

