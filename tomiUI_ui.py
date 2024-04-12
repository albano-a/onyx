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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QDockWidget,
    QFrame, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(936, 877)
        icon = QIcon()
        icon.addFile(u"tomi_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionSidebar = QAction(MainWindow)
        self.actionSidebar.setObjectName(u"actionSidebar")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border: 1px solid #212121;\n"
"	background-color: #fff;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")

        self.gridLayout.addWidget(self.homeButton, 0, 0, 1, 1)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout.addWidget(self.backButton, 0, 1, 1, 1)

        self.forwardButton = QPushButton(self.centralwidget)
        self.forwardButton.setObjectName(u"forwardButton")

        self.gridLayout.addWidget(self.forwardButton, 0, 2, 1, 1)

        self.zoomButton = QPushButton(self.centralwidget)
        self.zoomButton.setObjectName(u"zoomButton")

        self.gridLayout.addWidget(self.zoomButton, 1, 0, 1, 1)

        self.panButton = QPushButton(self.centralwidget)
        self.panButton.setObjectName(u"panButton")

        self.gridLayout.addWidget(self.panButton, 1, 1, 1, 1)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName(u"editButton")

        self.gridLayout.addWidget(self.editButton, 1, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.plotTOMIBtn = QPushButton(self.centralwidget)
        self.plotTOMIBtn.setObjectName(u"plotTOMIBtn")
        self.plotTOMIBtn.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.plotTOMIBtn.setFont(font)

        self.verticalLayout_4.addWidget(self.plotTOMIBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 936, 21))
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(220, 0))
        self.tabWidget.setMovable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.fileTOMIComboBox = QComboBox(self.groupBox)
        self.fileTOMIComboBox.setObjectName(u"fileTOMIComboBox")
        self.fileTOMIComboBox.setFont(font1)

        self.verticalLayout_3.addWidget(self.fileTOMIComboBox)

        self.importFileBtn = QPushButton(self.groupBox)
        self.importFileBtn.setObjectName(u"importFileBtn")
        self.importFileBtn.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	border: 1px solid #ababab;\n"
"	height: 20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.454545, y1:0, x2:0.454545, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0.454545, y1:0, x2:0.454545, y2:1, stop:0 rgba(254, 254, 254, 255), stop:1 rgba(248, 248, 248, 255));\n"
"}")

        self.verticalLayout_3.addWidget(self.importFileBtn)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.csvFileRadioButton = QRadioButton(self.groupBox)
        self.fileTOMIBtnGroup = QButtonGroup(MainWindow)
        self.fileTOMIBtnGroup.setObjectName(u"fileTOMIBtnGroup")
        self.fileTOMIBtnGroup.addButton(self.csvFileRadioButton)
        self.csvFileRadioButton.setObjectName(u"csvFileRadioButton")
        self.csvFileRadioButton.setSizeIncrement(QSize(0, 0))
        self.csvFileRadioButton.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"J:/Universidade/GIECAR/mpanicon/csv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.csvFileRadioButton.setIcon(icon1)
        self.csvFileRadioButton.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.csvFileRadioButton, 0, Qt.AlignHCenter)

        self.txtFileRadioButton = QRadioButton(self.groupBox)
        self.fileTOMIBtnGroup.addButton(self.txtFileRadioButton)
        self.txtFileRadioButton.setObjectName(u"txtFileRadioButton")
        self.txtFileRadioButton.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"J:/Universidade/GIECAR/mpanicon/txt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.txtFileRadioButton.setIcon(icon2)
        self.txtFileRadioButton.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.txtFileRadioButton, 0, Qt.AlignHCenter)

        self.xlsxFileRadioButton = QRadioButton(self.groupBox)
        self.fileTOMIBtnGroup.addButton(self.xlsxFileRadioButton)
        self.xlsxFileRadioButton.setObjectName(u"xlsxFileRadioButton")
        self.xlsxFileRadioButton.setEnabled(True)
        self.xlsxFileRadioButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"J:/Universidade/GIECAR/mpanicon/xlsx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.xlsxFileRadioButton.setIcon(icon3)
        self.xlsxFileRadioButton.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.xlsxFileRadioButton, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.mesaRotativaInput = QLineEdit(self.groupBox)
        self.mesaRotativaInput.setObjectName(u"mesaRotativaInput")

        self.verticalLayout_3.addWidget(self.mesaRotativaInput)

        self.plotTOMIBtn_2 = QPushButton(self.groupBox)
        self.plotTOMIBtn_2.setObjectName(u"plotTOMIBtn_2")
        self.plotTOMIBtn_2.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	border: 1px solid #ababab;\n"
"	height: 20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.454545, y1:0, x2:0.454545, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0.454545, y1:0, x2:0.454545, y2:1, stop:0 rgba(254, 254, 254, 255), stop:1 rgba(248, 248, 248, 255));\n"
"}")

        self.verticalLayout_3.addWidget(self.plotTOMIBtn_2)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.formationNameInput = QLineEdit(self.groupBox_2)
        self.formationNameInput.setObjectName(u"formationNameInput")

        self.verticalLayout_6.addWidget(self.formationNameInput)

        self.exportDataButton = QPushButton(self.groupBox_2)
        self.exportDataButton.setObjectName(u"exportDataButton")

        self.verticalLayout_6.addWidget(self.exportDataButton)

        self.saveButton = QPushButton(self.groupBox_2)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout_6.addWidget(self.saveButton)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_5.addWidget(self.label_10, 4, 0, 1, 3)

        self.plotTitleInput_2 = QLineEdit(self.tab_2)
        self.plotTitleInput_2.setObjectName(u"plotTitleInput_2")
        self.plotTitleInput_2.setMinimumSize(QSize(0, 20))
        self.plotTitleInput_2.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid #d2d2d2;\n"
"	background: #fdfdfd;\n"
"}")

        self.gridLayout_5.addWidget(self.plotTitleInput_2, 1, 0, 1, 3)

        self.krigingInterpolationModel = QComboBox(self.tab_2)
        self.krigingInterpolationModel.setObjectName(u"krigingInterpolationModel")
        self.krigingInterpolationModel.setStyleSheet(u"QComboBox::item {\n"
"	text-align: center;\n"
"}")
        self.krigingInterpolationModel.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.krigingInterpolationModel.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.krigingInterpolationModel, 5, 0, 1, 3)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 3)

        self.lineColorComboBox_2 = QComboBox(self.tab_2)
        self.lineColorComboBox_2.setObjectName(u"lineColorComboBox_2")
        self.lineColorComboBox_2.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_5.addWidget(self.lineColorComboBox_2, 3, 0, 1, 3)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 3)


        self.verticalLayout_5.addLayout(self.gridLayout_5)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.menuView.menuAction())
        self.menuView.addAction(self.actionSidebar)
        self.menuView.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSidebar.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.forwardButton.setText(QCoreApplication.translate("MainWindow", u"Avan\u00e7ar", None))
        self.zoomButton.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.panButton.setText(QCoreApplication.translate("MainWindow", u"Movimentar", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.plotTOMIBtn.setText(QCoreApplication.translate("MainWindow", u"Plotar", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.dockWidget.setWindowTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Arquivo:</p></body></html>", None))
        self.importFileBtn.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tipo de arquivo:", None))
        self.csvFileRadioButton.setText(QCoreApplication.translate("MainWindow", u".csv", None))
        self.txtFileRadioButton.setText(QCoreApplication.translate("MainWindow", u".txt", None))
        self.xlsxFileRadioButton.setText(QCoreApplication.translate("MainWindow", u".xlsx", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Mesa Rotativa:</span></p></body></html>", None))
        self.plotTOMIBtn_2.setText(QCoreApplication.translate("MainWindow", u"Plotar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Nome da Forma\u00e7\u00e3o:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.exportDataButton.setToolTip(QCoreApplication.translate("MainWindow", u"Exportar o dado de TOMI Index", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.exportDataButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Exportar o dado de TOMI Index. Lembre-se que o dado vai ser exportado utilizando '.' ao inv\u00e9s de ',' para delimitar o decimal.", None))
#endif // QT_CONFIG(statustip)
        self.exportDataButton.setText(QCoreApplication.translate("MainWindow", u"Exportar Dados", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Salvar Imagem", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Importa\u00e7\u00e3o", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Modelo de Interpola\u00e7\u00e3o:</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">T\u00edtulo do plot:</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cor da linha:</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Config. plot", None))
    # retranslateUi

