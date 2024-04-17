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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

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
        iconThemeName = u"application-exit"
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
        self.groupBox_2.setGeometry(QRect(9, -1, 1001, 641))
        self.groupBox_2.setStyleSheet(u"QGroupBox\n"
"{\n"
"	\n"
"	background-color: transparent;\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	color: rgb(131, 131, 131);\n"
"	border-radius:10px;\n"
"	border:2px solid gray;\n"
"}")
        self.file_list = QComboBox(self.groupBox_2)
        self.file_list.addItem("")
        self.file_list.addItem("")
        self.file_list.setObjectName(u"file_list")
        self.file_list.setGeometry(QRect(190, 270, 651, 40))
        self.file_list.setMinimumSize(QSize(0, 40))
        self.file_list.setMaximumSize(QSize(16777215, 40))
        self.file_list.setMouseTracking(False)
        self.file_list.setTabletTracking(False)
        self.file_list.setAcceptDrops(False)
        self.file_list.setLayoutDirection(Qt.LeftToRight)
        self.file_list.setAutoFillBackground(False)
        self.file_list.setStyleSheet(u"QComboBox{\n"
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
        self.file_list.setEditable(False)
        self.file_list.setIconSize(QSize(30, 30))
        self.file_list.setDuplicatesEnabled(False)
        self.file_list.setFrame(True)
        self.open_file = QPushButton(self.groupBox_2)
        self.open_file.setObjectName(u"open_file")
        self.open_file.setGeometry(QRect(840, 260, 60, 60))
        sizePolicy.setHeightForWidth(self.open_file.sizePolicy().hasHeightForWidth())
        self.open_file.setSizePolicy(sizePolicy)
        self.open_file.setMinimumSize(QSize(60, 60))
        self.open_file.setMaximumSize(QSize(60, 60))
        self.open_file.setLayoutDirection(Qt.LeftToRight)
        self.open_file.setStyleSheet(u"background-color:  transparent;\n"
"border:none;")
        icon1 = QIcon()
        iconThemeName = u"face-laugh"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"font/\u641c\u7d22.png", QSize(), QIcon.Normal, QIcon.Off)

        self.open_file.setIcon(icon1)
        self.open_file.setIconSize(QSize(60, 60))
        self.stream_import = QPushButton(self.groupBox_2)
        self.stream_import.setObjectName(u"stream_import")
        self.stream_import.setGeometry(QRect(890, 540, 60, 60))
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
        iconThemeName = u"accessories-calculator"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"font/\u8fdb\u5165.png", QSize(), QIcon.Normal, QIcon.Off)

        self.stream_import.setIcon(icon2)
        self.stream_import.setIconSize(QSize(60, 60))
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
        self.file_list.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.file_list.setItemText(1, QCoreApplication.translate("MainWindow", u"111111111111111111111111111111", None))

        self.stream_import.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u9884\u89c8", None))
        self.annotated_image.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.stream_reload.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u663e\u793a", None))
    # retranslateUi

