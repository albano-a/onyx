# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tomiUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QToolBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(598, 860)
        self.actionReset_Original_View = QAction(MainWindow)
        self.actionReset_Original_View.setObjectName(u"actionReset_Original_View")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(580, 200))
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.toolBox = QToolBox(self.frame)
        self.toolBox.setObjectName(u"toolBox")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet(u"QToolBox {\n"
"	border: None;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QToolBox::Tab {\n"
"	border: 1px solid #d9d9d9;\n"
"	background-color: #f7f7f7;\n"
"	border-radius: 15px;\n"
"}")
        self.toolBox.setFrameShape(QFrame.Panel)
        self.fileImportTool = QWidget()
        self.fileImportTool.setObjectName(u"fileImportTool")
        self.fileImportTool.setGeometry(QRect(0, 0, 560, 98))
        self.horizontalLayout = QHBoxLayout(self.fileImportTool)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.fileTOMIComboBox = QComboBox(self.fileImportTool)
        self.fileTOMIComboBox.setObjectName(u"fileTOMIComboBox")
        font1 = QFont()
        font1.setPointSize(12)
        self.fileTOMIComboBox.setFont(font1)

        self.gridLayout.addWidget(self.fileTOMIComboBox, 0, 1, 1, 2)

        self.label_2 = QLabel(self.fileImportTool)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, Qt.AlignRight)

        self.label_3 = QLabel(self.fileImportTool)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1, Qt.AlignRight)

        self.txtFileRadioButton = QRadioButton(self.fileImportTool)
        self.fileTOMIBtnGroup = QButtonGroup(MainWindow)
        self.fileTOMIBtnGroup.setObjectName(u"fileTOMIBtnGroup")
        self.fileTOMIBtnGroup.addButton(self.txtFileRadioButton)
        self.txtFileRadioButton.setObjectName(u"txtFileRadioButton")
        self.txtFileRadioButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u"mpanicon/txt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.txtFileRadioButton.setIcon(icon)
        self.txtFileRadioButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.txtFileRadioButton, 1, 2, 1, 1, Qt.AlignHCenter)

        self.xlsxFileRadioButton = QRadioButton(self.fileImportTool)
        self.fileTOMIBtnGroup.addButton(self.xlsxFileRadioButton)
        self.xlsxFileRadioButton.setObjectName(u"xlsxFileRadioButton")
        self.xlsxFileRadioButton.setEnabled(False)
        self.xlsxFileRadioButton.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"mpanicon/xlsx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.xlsxFileRadioButton.setIcon(icon1)
        self.xlsxFileRadioButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.xlsxFileRadioButton, 1, 3, 1, 1, Qt.AlignHCenter)

        self.csvFileRadioButton = QRadioButton(self.fileImportTool)
        self.fileTOMIBtnGroup.addButton(self.csvFileRadioButton)
        self.csvFileRadioButton.setObjectName(u"csvFileRadioButton")
        self.csvFileRadioButton.setSizeIncrement(QSize(0, 0))
        self.csvFileRadioButton.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"mpanicon/csv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.csvFileRadioButton.setIcon(icon2)
        self.csvFileRadioButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.csvFileRadioButton, 1, 1, 1, 1, Qt.AlignHCenter)

        self.importFileBtn = QPushButton(self.fileImportTool)
        self.importFileBtn.setObjectName(u"importFileBtn")

        self.gridLayout.addWidget(self.importFileBtn, 0, 3, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.toolBox.addItem(self.fileImportTool, u"Importa\u00e7\u00e3o de arquivo")
        self.plotConfigTool = QWidget()
        self.plotConfigTool.setObjectName(u"plotConfigTool")
        self.plotConfigTool.setGeometry(QRect(0, 0, 560, 98))
        self.horizontalLayout_2 = QHBoxLayout(self.plotConfigTool)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.plotConfigTool)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.plotTitleInput = QLineEdit(self.plotConfigTool)
        self.plotTitleInput.setObjectName(u"plotTitleInput")
        self.plotTitleInput.setMinimumSize(QSize(0, 20))
        self.plotTitleInput.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #d2d2d2;\n"
"	background: #fdfdfd;\n"
"}")

        self.gridLayout_2.addWidget(self.plotTitleInput, 0, 1, 1, 4)

        self.label_6 = QLabel(self.plotConfigTool)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineColorComboBox = QComboBox(self.plotConfigTool)
        self.lineColorComboBox.setObjectName(u"lineColorComboBox")
        self.lineColorComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_2.addWidget(self.lineColorComboBox, 1, 1, 1, 1)

        self.label_5 = QLabel(self.plotConfigTool)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)

        self.lineTypeComboBox = QComboBox(self.plotConfigTool)
        self.lineTypeComboBox.setObjectName(u"lineTypeComboBox")
        self.lineTypeComboBox.setStyleSheet(u"QComboBox::item {\n"
"	text-align: center;\n"
"}")
        self.lineTypeComboBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.lineTypeComboBox.setIconSize(QSize(24, 24))

        self.gridLayout_2.addWidget(self.lineTypeComboBox, 1, 3, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.toolBox.addItem(self.plotConfigTool, u"Configura\u00e7\u00f5es do plot")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout.addWidget(self.frame)

        self.plotTOMIBtn = QPushButton(self.centralwidget)
        self.plotTOMIBtn.setObjectName(u"plotTOMIBtn")
        self.plotTOMIBtn.setMinimumSize(QSize(250, 0))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.plotTOMIBtn.setFont(font2)

        self.verticalLayout.addWidget(self.plotTOMIBtn, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: #fff;\n"
"	border: 1px solid #212121\n"
"}")

        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.frame_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")

        self.horizontalLayout_3.addWidget(self.homeButton)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout_3.addWidget(self.backButton)

        self.forwardButton = QPushButton(self.centralwidget)
        self.forwardButton.setObjectName(u"forwardButton")

        self.horizontalLayout_3.addWidget(self.forwardButton)

        self.panButton = QPushButton(self.centralwidget)
        self.panButton.setObjectName(u"panButton")

        self.horizontalLayout_3.addWidget(self.panButton)

        self.zoomButton = QPushButton(self.centralwidget)
        self.zoomButton.setObjectName(u"zoomButton")

        self.horizontalLayout_3.addWidget(self.zoomButton)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")

        self.horizontalLayout_3.addWidget(self.editButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_3.addWidget(self.saveButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 598, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionReset_Original_View.setText(QCoreApplication.translate("MainWindow", u"Reset Original View", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">TOMI Index</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Arquivo:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tipo de arquivo:", None))
        self.txtFileRadioButton.setText(QCoreApplication.translate("MainWindow", u".txt", None))
        self.xlsxFileRadioButton.setText(QCoreApplication.translate("MainWindow", u".xlsx", None))
        self.csvFileRadioButton.setText(QCoreApplication.translate("MainWindow", u".csv", None))
        self.importFileBtn.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.fileImportTool), QCoreApplication.translate("MainWindow", u"Importa\u00e7\u00e3o de arquivo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo do plot:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cor da linha:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tipo de linha:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.plotConfigTool), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es do plot", None))
        self.plotTOMIBtn.setText(QCoreApplication.translate("MainWindow", u"Plotar", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.forwardButton.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        self.panButton.setText(QCoreApplication.translate("MainWindow", u"Movimentar", None))
        self.zoomButton.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

