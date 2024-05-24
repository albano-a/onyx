from PyQt5.QtWidgets import (
    QFileDialog,
    QApplication,
    QPushButton,
    QToolBar,
    QVBoxLayout,
    QMainWindow,
    QMessageBox,
)
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QFile, QRectF, QUrl, Qt
from PyQt5.QtGui import QIcon, QDesktopServices
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from tomiUI import Ui_MainWindow
import plotly.graph_objects as go
from pykrige.ok import OrdinaryKriging
import os
import sys
import shutil
from openpyxl import Workbook

# plt.style.use(['ggplot'])


class MainProgramWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainProgramWindow, self).__init__()

        self.setupUi(self)
        self.setWindowTitle("TOMI Calculator")
        # self.setWindowIcon(QIcon("../icons/Icon.ico"))

        self.figure = Figure(figsize=(5, 6))
        self.canvas = FigureCanvasQTAgg(self.figure)

        # Create a QVBoxLayout within your QWidget
        self.plotLayout = QVBoxLayout(self.frame)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.plotLayout.setSpacing(0)  # Remove spacing
        # Add the FigureCanvasQTAgg object to the layout
        self.plotLayout.addWidget(self.canvas)

        # Hiding the excel sheet options
        self.xlsxFileRadioButton.toggled.connect(self.show_xlsx_options)
        # Initializing the state
        self.sheetTabLabel.hide()
        self.sheetPageInput.hide()

        # Set the layout of the parent widget
        self.matplotlib_toolbar = NavigationToolbar2QT(self.canvas)
        # Create a custom toolbar
        # Create a button for each function and add it to the custom toolbar
        self.homeButton.clicked.connect(self.matplotlib_toolbar.home)
        self.backButton.clicked.connect(self.matplotlib_toolbar.back)
        self.forwardButton.clicked.connect(self.matplotlib_toolbar.forward)
        self.panButton.clicked.connect(self.matplotlib_toolbar.pan)
        self.zoomButton.clicked.connect(self.matplotlib_toolbar.zoom)
        self.editButton.clicked.connect(self.matplotlib_toolbar.edit_parameters)
        self.saveButton.clicked.connect(self.matplotlib_toolbar.save_figure)

        self.actionSidebar.triggered.connect(self.toggle_sidebar)
        self.actionDocumentation.triggered.connect(
            lambda: self.open_documentation(
                "https://github.com/albano-a/onyx-tomi-index-plotter"
            )
        )

        self.selected_file = None

        self.importFileBtn.clicked.connect(self.import_file)

        chooseColors = [
            "Blue",
            "Red",
            "Yellow",
            "Green",
            "Purple",
            "Orange",
            "Pink",
            "Black",
            "White",
        ]

        self.lineColorComboBox_2.addItems(chooseColors)

        interpolationModels = [
            "Linear",
            "Gaussian",
            "Power",
            "Spherical",
            "Exponential",
            "Hole-Effect",
        ]

        self.krigingInterpolationModel.addItems(interpolationModels)

        self.plotTOMIBtn.clicked.connect(self.plot_tomi_index)
        self.plotTOMIBtn_2.clicked.connect(self.plot_tomi_index)
        self.exportDataButton.clicked.connect(self.export_data)

        self.show()

    def open_documentation(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def toggle_sidebar(self):
        if self.dockWidget.isVisible():
            self.dockWidget.hide()
        else:
            self.dockWidget.show()

    def import_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Open File",
            "uploads",
            "CSV, TXT, XLSX (*.csv *.txt *.xlsx);;All Files (*)",
        )
        # import .csv and .txt files

        if file_path:
            self.fileNameInput.setText(file_path)

    def redraw_plot(self):
        self.plot_tomi_index()

    def show_xlsx_options(self):
        if self.xlsxFileRadioButton.isChecked():
            self.sheetTabLabel.show()
            self.sheetPageInput.show()
        else:
            self.sheetTabLabel.hide()
            self.sheetPageInput.hide()

    def read_file(self):
        dataframe = pd.DataFrame()

        checked_button = self.fileTOMIBtnGroup.checkedButton()
        if checked_button is None:
            QMessageBox.warning(self, "Error", "Selecione o tipo de arquivo")
            return pd.DataFrame()

        self.file_type_button_text = self.fileTOMIBtnGroup.checkedButton().text()
        self.selected_file = self.fileNameInput.text()

        if self.file_type_button_text == ".csv":
            try:
                dataframe = pd.read_csv(self.selected_file, skiprows=0, delimiter=";")
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()

        elif self.file_type_button_text == ".txt":
            try:
                dataframe = pd.read_txt(
                    self.selected_file, skiprows=0, delimiter=";"
                )
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()

        elif self.file_type_button_text == ".xlsx":
            sheetTab = self.sheetPageInput.text()
            try:
                dataframe = pd.read_excel(
                    self.selected_file,
                    skiprows=0,
                    decimal=",",
                    sheet_name=sheetTab,
                )
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()
        else:
            QMessageBox.warning(self, "Error", "Selecione o tipo de arquivo")
            return pd.DataFrame()

    def tomi_index_calculation(self):
        dataframe = self.read_file()
        d13C = dataframe.iloc[:, 5]
        TOC_TN = dataframe.iloc[:, 6]
        self.krigingModel = self.krigingInterpolationModel.currentText()
        self.krigingModel = self.krigingModel.lower()

        # do artigo
        art_toc_tn = np.array([4, 4, 4, 4, 10, 10, 10, 10, 100, 100, 100, 100])
        art_c13corg = np.array(
            [-10, -22, -25, -34, -10, -22, -25, -34, -10, -22, -25, -34]
        )
        probabilidade = np.array([0, 10, 20, 30, 20, 30, 40, 50, 90, 95, 98, 100])

        # Dados das suas amostras
        amostra_art_toc_tn = (
            TOC_TN  # Lista/array dos valores de TOC:TN das suas amostras
        )
        amostra_art_c13corg = (
            d13C  # Lista/array dos valores de δ13Corg das suas amostras
        )

        # Grade de valores para interpolação
        art_toc_tn_grid = np.linspace(0, 100, 1001)  # Valores de TOC:TN para a grade
        art_c13corg_grid = np.linspace(-34, -10, 241)  # Valores de δ13Corg para a grade

        # Kriging
        OK = OrdinaryKriging(
            art_toc_tn, art_c13corg, probabilidade, variogram_model=self.krigingModel
        )
        z, ss = OK.execute("grid", art_toc_tn_grid, art_c13corg_grid)

        # Aplicação dos dados das suas amostras na grade interpolada
        amostra_probabilidade, ss = OK.execute(
            "points", amostra_art_toc_tn, amostra_art_c13corg
        )

        return amostra_probabilidade

    def mesa_rotativa_conversion(self, mesaRotativaInput, profundidade):
        return mesaRotativaInput - profundidade

    def plot_tomi_index(self):
        self.figure.clear()
        self.lineColor = self.lineColorComboBox_2.currentText()
        self.lineColor = self.lineColor.lower()
        self.Title = self.plotTitleInput_2.text()
        self.mesa = self.mesaRotativaInput.text()

        invert_axis = False

        dataframe = self.read_file()
        profundidade = dataframe.iloc[:, 0]

        if self.mesa == "":
            tvd = profundidade
            invert_axis = True
        else:
            try:
                invert_axis = False
                tvd = self.mesa_rotativa_conversion(int(self.mesa), profundidade)
            except ValueError:
                QMessageBox.critical(
                    self, "Error", "Digite um valor numérico para a mesa rotativa."
                )
                return

        amostra_probabilidade = self.tomi_index_calculation()
        ax = self.canvas.figure.add_subplot(111)
        ax.set_title(self.Title, fontweight="bold", fontsize=14, color="#212121")
        ax.plot(amostra_probabilidade, tvd, "s-", color=self.lineColor, label="TOMI")
        if invert_axis:
            ax.invert_yaxis()
        # ax.invert_yaxis()
        ax.set_xlim(0, 100)
        ax.set_xlabel("TOMI index (%)")
        ax.set_ylabel("Profundidade (m)")
        ax.grid()
        # self.canvas.figure.set_tight_layout(True)
        self.canvas.draw()

    def export_data(self):
        dataframe = self.read_file()
        profundidade = dataframe.iloc[:, 0]
        tvdss = dataframe.iloc[:, 1]
        d13C = dataframe.iloc[:, 5]
        TOC_TN = dataframe.iloc[:, 6]
        amostra_probabilidade = self.tomi_index_calculation()

        self.formationName = self.formationNameInput.text()

        # Create a new dataframe
        export_dataframe = pd.DataFrame(
            {
                "Prof": profundidade,
                "TVDSS": tvdss,
                "d13C": d13C,
                "TOC_TN": TOC_TN,
                "TOMI Index": amostra_probabilidade,
            }
        )

        # Open a file dialog for the user to select the file name and location
        dialog = QFileDialog()
        filename, _ = dialog.getSaveFileName(filter="Excel files (*.xlsx)")

        self.formationCheck = [self.formationName if self.formationName else "Formação"]

        if filename:
            # If a file name is selected, export the dataframe to a .csv file
            for col in export_dataframe.columns:
                if export_dataframe[col].dtype == "float64":
                    export_dataframe[col] = export_dataframe[col].apply(
                        lambda x: str(x).replace(".", ",")
                    )

            export_dataframe.to_excel(
                filename, sheet_name=self.formationCheck[0], index=False
            )
            QMessageBox.information(
                self,
                "Exportação de dados",
                f"Os dados foram exportados com sucesso para {filename}",
            )
            QMessageBox.information(
                self,
                "Delimitação",
                f"Lembre-se que os dados foram exportados com '.' ao invés de ','",
            )


def main():
    appctx = ApplicationContext()
    window = MainProgramWindow()
    window.show()
    sys.exit(appctx.app.exec())


if __name__ == "__main__":
    main()
