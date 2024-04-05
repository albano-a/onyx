from PySide6.QtWidgets import QFileDialog, QApplication, QPushButton, QToolBar, QVBoxLayout, QMainWindow, QMessageBox, QGraphicsScene, QGraphicsView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QRectF
from PySide6.QtGui import QIcon, Qt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import scienceplots
from tomiUI import Ui_MainWindow
from pykrige.ok import OrdinaryKriging
import os
import sys
import shutil

plt.style.use(['ggplot', 'grid'])

class MainProgramWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainProgramWindow, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("TOMI Calculator")

        self.figure = Figure(figsize=(5, 6))
        self.canvas = FigureCanvasQTAgg(self.figure)

        # Create a QVBoxLayout within your QWidget
        self.plotLayout = QVBoxLayout(self.widget)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.plotLayout.setSpacing(0)  # Remove spacing
        # Add the FigureCanvasQTAgg object to the layout
        self.plotLayout.addWidget(self.canvas)

        # Set the layout of the parent widget
        self.matplotlib_toolbar = NavigationToolbar2QT(self.canvas, self)
        # Create a custom toolbar
        # Create a button for each function and add it to the custom toolbar
        self.homeButton.clicked.connect(self.matplotlib_toolbar.home)
        self.backButton.clicked.connect(self.matplotlib_toolbar.back)
        self.forwardButton.clicked.connect(self.matplotlib_toolbar.forward)
        self.panButton.clicked.connect(self.matplotlib_toolbar.pan)
        self.zoomButton.clicked.connect(self.matplotlib_toolbar.zoom)
        self.editButton.clicked.connect(self.matplotlib_toolbar.edit_parameters)
        self.saveButton.clicked.connect(self.matplotlib_toolbar.save_figure)

        self.selected_file = None

        self.importFileBtn.clicked.connect(self.import_file)

        # list of files in the uploads directory - Select the file option
        self.files = os.listdir('uploads')
        self.fileTOMIComboBox.addItems(self.files)

        self.lineColorComboBox.addItems(['blue', 'red', 'yellow',
                                         'green', 'purple', 'orange',
                                         'pink', 'black', 'white'])

        self.lineTypeComboBox.addItem("")
        self.lineTypeComboBox.addItem("")
        self.lineTypeComboBox.addItem("")
        self.lineTypeComboBox.addItem("")

        self.lineTypeComboBox.setItemData(0, QIcon("./mpanicon/square.png"), Qt.DecorationRole)
        self.lineTypeComboBox.setItemData(1, QIcon("./mpanicon/circle.png"), Qt.DecorationRole)
        self.lineTypeComboBox.setItemData(2, QIcon("./mpanicon/dashed.png"), Qt.DecorationRole)
        self.lineTypeComboBox.setItemData(3, QIcon("./mpanicon/dashedCircle.png"), Qt.DecorationRole)

        self.plotTOMIBtn.clicked.connect(self.plot_tomi_index)

        self.show()

    def import_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File',
                                                   'uploads',
                                                   'CSV, TXT, XLSX (*.csv *.txt *.xlsx);;All Files (*)')
        # import .csv and .txt files

        if file_path:  # If a file was selected
            # Get the base name of the file
            file_name = os.path.basename(file_path)

            # Copy the file to the ./uploads directory
            shutil.copy(file_path, f'./uploads/{file_name}')

            QMessageBox.information(self, "Arquivo importado\n",
                                    f"Arquivo {file_name} importado com sucesso!")

            # Update the combo box
            self.fileTOMIComboBox.clear()
            self.files = os.listdir('uploads')
            self.fileTOMIComboBox.addItems(self.files)


    def redraw_plot(self):
        self.plot_tomi_index()

    def read_file(self):
        dataframe = pd.DataFrame()

        checked_button = self.fileTOMIBtnGroup.checkedButton()
        if checked_button is None:
            QMessageBox.warning(self, "Error", "Selecione o tipo de arquivo")
            return pd.DataFrame()

        self.file_type_button_text = self.fileTOMIBtnGroup.checkedButton().text()
        self.selected_file = self.fileTOMIComboBox.currentText()

        if self.file_type_button_text == '.csv':
            try:
                dataframe = pd.read_csv(f'uploads/{self.selected_file}',
                                        skiprows=0,
                                        delimiter=';',
                                        usecols=(0,1,2,3,4,5,6))
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()

        elif self.file_type_button_text == '.txt':
            try:
                dataframe = pd.read_csv(f'uploads/{self.selected_file}',
                                        skiprows=0,
                                        delimiter=';',
                                        usecols=(0,1,2,3,4,5,6))
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()

        elif self.file_type_button_text == '.xlsx':
            pass

        else:
            QMessageBox.warning(self, "Error", "Selecione o tipo de arquivo")
            return pd.DataFrame()

    def tomi_index_calculation(self):
        dataframe = self.read_file()
        profundidade = dataframe.iloc[:,0]
        d13C = dataframe.iloc[:,5]
        TOC_TN = dataframe.iloc[:,6]

        # do artigo
        art_toc_tn = np.array([4,4,4,4,10,10,10,10,100,100,100,100])
        art_c13corg = np.array([-10,-22,-25,-34,-10,-22,-25,-34,-10,-22,-25,-34])
        probabilidade = np.array([0,10,20,30,20,30,40,50,90,95,98,100])

        # Dados das suas amostras
        amostra_art_toc_tn = TOC_TN  # Lista/array dos valores de TOC:TN das suas amostras
        amostra_art_c13corg = d13C  # Lista/array dos valores de δ13Corg das suas amostras

        # Grade de valores para interpolação
        art_toc_tn_grid = np.linspace(0, 100, 1001)  # Valores de TOC:TN para a grade
        art_c13corg_grid = np.linspace(-34, -10, 241)  # Valores de δ13Corg para a grade

        # Kriging
        OK = OrdinaryKriging(art_toc_tn, art_c13corg, probabilidade, variogram_model='linear')
        z, ss = OK.execute('grid', art_toc_tn_grid, art_c13corg_grid)

        # Aplicação dos dados das suas amostras na grade interpolada
        amostra_probabilidade, ss = OK.execute('points', amostra_art_toc_tn, amostra_art_c13corg)

        return amostra_probabilidade

    def plot_tomi_index(self):
        self.figure.clear()
        self.lineType = self.lineColorComboBox.currentText()
        self.Title = self.plotTitleInput.text()

        dataframe = self.read_file()
        profundidade = dataframe.iloc[:,0]

        amostra_probabilidade = self.tomi_index_calculation()
        ax = self.canvas.figure.add_subplot(111)
        ax.set_title(self.Title, fontsize=12, color='#212121')
        ax.plot(amostra_probabilidade,
                 profundidade,
                 's-',
                 label='TOMI')
        ax.invert_yaxis()
        ax.set_xlim(0,100)
        ax.set_xlabel("TOMI index (%)")
        ax.set_ylabel("Profundidade (m)")
        # self.canvas.figure.set_tight_layout(True)
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = MainProgramWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()