# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tomiUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QComboBox,
    QDockWidget,
    QFrame,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QStatusBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 888)
        icon = QIcon()
        icon.addFile("tomi_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionSidebar = QAction(MainWindow)
        self.actionSidebar.setObjectName("actionSidebar")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(
            "QFrame {\n"
            "	border: 1px solid #212121;\n"
            "	background-color: #fff;\n"
            "}"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName("homeButton")

        self.gridLayout.addWidget(self.homeButton, 0, 0, 1, 1)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")

        self.gridLayout.addWidget(self.backButton, 0, 1, 1, 1)

        self.forwardButton = QPushButton(self.centralwidget)
        self.forwardButton.setObjectName("forwardButton")

        self.gridLayout.addWidget(self.forwardButton, 0, 2, 1, 1)

        self.zoomButton = QPushButton(self.centralwidget)
        self.zoomButton.setObjectName("zoomButton")

        self.gridLayout.addWidget(self.zoomButton, 1, 0, 1, 1)

        self.panButton = QPushButton(self.centralwidget)
        self.panButton.setObjectName("panButton")

        self.gridLayout.addWidget(self.panButton, 1, 1, 1, 1)

        self.editButton = QPushButton(self.centralwidget)
        self.editButton.setObjectName("editButton")

        self.gridLayout.addWidget(self.editButton, 1, 2, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.plotTOMIBtn = QPushButton(self.centralwidget)
        self.plotTOMIBtn.setObjectName("plotTOMIBtn")
        self.plotTOMIBtn.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.plotTOMIBtn.setFont(font)

        self.verticalLayout_4.addWidget(self.plotTOMIBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1101, 21))
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setMinimumSize(QSize(220, 0))
        self.tabWidget.setMovable(False)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)

        self.fileTOMIComboBox = QComboBox(self.groupBox)
        self.fileTOMIComboBox.setObjectName("fileTOMIComboBox")
        self.fileTOMIComboBox.setFont(font1)

        self.verticalLayout_3.addWidget(self.fileTOMIComboBox)

        self.importFileBtn = QPushButton(self.groupBox)
        self.importFileBtn.setObjectName("importFileBtn")

        self.verticalLayout_3.addWidget(self.importFileBtn)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.csvFileRadioButton = QRadioButton(self.groupBox)
        self.fileTOMIBtnGroup = QButtonGroup(MainWindow)
        self.fileTOMIBtnGroup.setObjectName("fileTOMIBtnGroup")
        self.fileTOMIBtnGroup.addButton(self.csvFileRadioButton)
        self.csvFileRadioButton.setObjectName("csvFileRadioButton")
        self.csvFileRadioButton.setSizeIncrement(QSize(0, 0))
        self.csvFileRadioButton.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(
            "J:/Universidade/GIECAR/mpanicon/csv.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.csvFileRadioButton.setIcon(icon1)
        self.csvFileRadioButton.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.csvFileRadioButton, 0, Qt.AlignHCenter)

        self.txtFileRadioButton = QRadioButton(self.groupBox)
        self.fileTOMIBtnGroup.addButton(self.txtFileRadioButton)
        self.txtFileRadioButton.setObjectName("txtFileRadioButton")
        self.txtFileRadioButton.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(
            "J:/Universidade/GIECAR/mpanicon/txt.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.txtFileRadioButton.setIcon(icon2)
        self.txtFileRadioButton.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.txtFileRadioButton, 0, Qt.AlignHCenter)

        self.xlsxFileRadioButton = QRadioButton(self.groupBox)
        self.fileTOMIBtnGroup.addButton(self.xlsxFileRadioButton)
        self.xlsxFileRadioButton.setObjectName("xlsxFileRadioButton")
        self.xlsxFileRadioButton.setEnabled(True)
        self.xlsxFileRadioButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(
            "J:/Universidade/GIECAR/mpanicon/xlsx.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.xlsxFileRadioButton.setIcon(icon3)
        self.xlsxFileRadioButton.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.xlsxFileRadioButton, 0, Qt.AlignHCenter)

        self.sheetTabLabel = QLabel(self.groupBox)
        self.sheetTabLabel.setObjectName("sheetTabLabel")

        self.verticalLayout_3.addWidget(self.sheetTabLabel)

        self.sheetPageInput = QLineEdit(self.groupBox)
        self.sheetPageInput.setObjectName("sheetPageInput")
        self.sheetPageInput.setStyleSheet(
            "QLineEdit { \n" "	text-align: center; \n" "}"
        )

        self.verticalLayout_3.addWidget(self.sheetPageInput)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.mesaRotativaInput = QLineEdit(self.groupBox)
        self.mesaRotativaInput.setObjectName("mesaRotativaInput")

        self.verticalLayout_3.addWidget(self.mesaRotativaInput)

        self.plotTOMIBtn_2 = QPushButton(self.groupBox)
        self.plotTOMIBtn_2.setObjectName("plotTOMIBtn_2")

        self.verticalLayout_3.addWidget(self.plotTOMIBtn_2)

        self.verticalLayout_7.addWidget(self.groupBox)

        self.line = QFrame(self.tab)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName("label")

        self.verticalLayout_6.addWidget(self.label)

        self.formationNameInput = QLineEdit(self.groupBox_2)
        self.formationNameInput.setObjectName("formationNameInput")

        self.verticalLayout_6.addWidget(self.formationNameInput)

        self.exportDataButton = QPushButton(self.groupBox_2)
        self.exportDataButton.setObjectName("exportDataButton")

        self.verticalLayout_6.addWidget(self.exportDataButton)

        self.saveButton = QPushButton(self.groupBox_2)
        self.saveButton.setObjectName("saveButton")

        self.verticalLayout_6.addWidget(self.saveButton)

        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName("frame_2")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(font1)

        self.gridLayout_5.addWidget(self.label_10, 4, 0, 1, 3)

        self.plotTitleInput_2 = QLineEdit(self.tab_2)
        self.plotTitleInput_2.setObjectName("plotTitleInput_2")
        self.plotTitleInput_2.setMinimumSize(QSize(0, 20))
        self.plotTitleInput_2.setStyleSheet(
            "QLineEdit {\n"
            "	border: 1px solid #d2d2d2;\n"
            "	background: #fdfdfd;\n"
            "}"
        )

        self.gridLayout_5.addWidget(self.plotTitleInput_2, 1, 0, 1, 3)

        self.krigingInterpolationModel = QComboBox(self.tab_2)
        self.krigingInterpolationModel.setObjectName("krigingInterpolationModel")
        self.krigingInterpolationModel.setStyleSheet(
            "QComboBox::item {\n" "	text-align: center;\n" "}"
        )
        self.krigingInterpolationModel.setSizeAdjustPolicy(
            QComboBox.AdjustToContentsOnFirstShow
        )
        self.krigingInterpolationModel.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.krigingInterpolationModel, 5, 0, 1, 3)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font1)

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 3)

        self.lineColorComboBox_2 = QComboBox(self.tab_2)
        self.lineColorComboBox_2.setObjectName("lineColorComboBox_2")
        self.lineColorComboBox_2.setSizeAdjustPolicy(
            QComboBox.AdjustToContentsOnFirstShow
        )

        self.gridLayout_5.addWidget(self.lineColorComboBox_2, 3, 0, 1, 3)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(font1)

        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 3)

        self.verticalLayout_5.addLayout(self.gridLayout_5)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName("frame_3")
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
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionSidebar.setText(
            QCoreApplication.translate("MainWindow", "Sidebar", None)
        )
        self.actionDocumentation.setText(
            QCoreApplication.translate("MainWindow", "Documentation", None)
        )
        self.homeButton.setText(QCoreApplication.translate("MainWindow", "Reset", None))
        self.backButton.setText(
            QCoreApplication.translate("MainWindow", "Voltar", None)
        )
        self.forwardButton.setText(
            QCoreApplication.translate("MainWindow", "Avan\u00e7ar", None)
        )
        self.zoomButton.setText(QCoreApplication.translate("MainWindow", "Zoom", None))
        self.panButton.setText(
            QCoreApplication.translate("MainWindow", "Movimentar", None)
        )
        self.editButton.setText(
            QCoreApplication.translate("MainWindow", "Editar", None)
        )
        self.plotTOMIBtn.setText(
            QCoreApplication.translate("MainWindow", "Plotar", None)
        )
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", "View", None))
        self.dockWidget.setWindowTitle("")
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Arquivo", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Arquivo:</p></body></html>',
                None,
            )
        )
        self.importFileBtn.setText(
            QCoreApplication.translate("MainWindow", "Importar", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "Tipo de arquivo:", None)
        )
        self.csvFileRadioButton.setText(
            QCoreApplication.translate("MainWindow", ".csv", None)
        )
        self.txtFileRadioButton.setText(
            QCoreApplication.translate("MainWindow", ".txt", None)
        )
        self.xlsxFileRadioButton.setText(
            QCoreApplication.translate("MainWindow", ".xlsx", None)
        )
        self.sheetTabLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt;">Aba da Planilha</span></p></body></html>',
                None,
            )
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt;">Mesa Rotativa:</span></p></body></html>',
                None,
            )
        )
        self.plotTOMIBtn_2.setText(
            QCoreApplication.translate("MainWindow", "Plotar", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", "Exportar", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt;">Nome da Forma\u00e7\u00e3o:</span></p></body></html>',
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.exportDataButton.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Exportar o dado de TOMI Index", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.exportDataButton.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Exportar o dado de TOMI Index. Lembre-se que o dado vai ser exportado utilizando '.' ao inv\u00e9s de ',' para delimitar o decimal.",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.exportDataButton.setText(
            QCoreApplication.translate("MainWindow", "Exportar Dados", None)
        )
        self.saveButton.setText(
            QCoreApplication.translate("MainWindow", "Salvar Imagem", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Importa\u00e7\u00e3o", None),
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Modelo de Interpola\u00e7\u00e3o:</p></body></html>',
                None,
            )
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">T\u00edtulo do plot:</p></body></html>',
                None,
            )
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Cor da linha:</p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Config. plot", None),
        )

    # retranslateUi
