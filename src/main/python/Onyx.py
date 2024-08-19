from PyQt5.QtWidgets import (
    QFileDialog,
    QApplication,
    QPushButton,
    QToolBar,
    QVBoxLayout,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QFile, QRectF, QUrl, Qt
from PyQt5 import uic
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

GUI = "src/main/python/gui/MainWindowOnyx.ui"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi(GUI, self)

        self.nextPage.clicked.connect(self.go_to_page2)
        self.backPage.clicked.connect(self.go_to_page1)

        self.importFileBtn.clicked.connect(self.import_file)
        self.refreshButton.clicked.connect(self.refresh_combobox)
        self.showDataPushButton.clicked.connect(self.add_data_to_table)
        self.plotTOMIBtn.clicked.connect(self.plot_TOMI_index)

        self.show()

    def go_to_page1(self):
        self.stackedWidget.setCurrentIndex(0)

    def go_to_page2(self):
        self.stackedWidget.setCurrentIndex(1)

    def import_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Open File",
            "uploads",
            "XLSX (*.xlsx);;All Files (*)",
        )
        # import .csv and .txt files

        if file_path:
            self.fileNameInput.setText(file_path)

    def refresh_combobox(self):
        file_path = self.fileNameInput.text()
        if file_path:
            try:
                workbooks = pd.ExcelFile(file_path).sheet_names
                self.workbookComboBox.clear()
                self.workbookComboBox.addItems(workbooks)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load Excel file: {str(e)}"
                )
        else:
            QMessageBox.warning(self, "Warning", "Please select an Excel file first.")

    def add_data_to_table(self):
        file_path = self.fileNameInput.text()
        workbook_name = self.workbookComboBox.currentText()

        if file_path and workbook_name:
            try:
                # Load the Excel file
                excel_file = pd.ExcelFile(file_path)
                sheet_names = excel_file.sheet_names

                # Clear existing tabs
                self.showExcelFileDataTab.clear()

                # Create a tab for each sheet in the workbook
                for sheet_name in sheet_names:
                    sheet_data = pd.read_excel(file_path, sheet_name=sheet_name)
                    table_widget = QTableWidget()
                    table_widget.setRowCount(sheet_data.shape[0])
                    table_widget.setColumnCount(sheet_data.shape[1])
                    table_widget.setHorizontalHeaderLabels(sheet_data.columns)

                    # Populate the table with data
                    for i, row in enumerate(sheet_data.iterrows()):
                        for j, value in enumerate(row[1]):
                            item = QTableWidgetItem(str(value))
                            table_widget.setItem(i, j, item)

                    # Add the table widget to the tab
                    self.showExcelFileDataTab.addTab(table_widget, sheet_name)

                # Show the tab widget
                self.stackedWidget.setCurrentIndex(2)

            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load Excel data: {str(e)}"
                )
        else:
            QMessageBox.warning(
                self, "Warning", "Please select an Excel file and workbook first."
            )

    def tomi_index_calculation(self):
        dataframe = self.read_file()
        d13C = dataframe.iloc[:, 5]
        TOC_TN = dataframe.iloc[:, 6]
        self.krigingModel = "linear"

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

    def plot_TOMI_index(self):
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
        amostra_probabilidade = pd.Series(amostra_probabilidade)

        # Remove NaN values
        mask = ~amostra_probabilidade.isna()
        amostra_probabilidade = amostra_probabilidade[mask]
        tvd = tvd[mask]

        print(f"Length of amostra_probabilidade: {len(amostra_probabilidade)}")
        print(f"Length of tvd: {len(tvd)}")
        print(f"Type of amostra_probabilidade: {type(amostra_probabilidade)}")
        print(f"Type of tvd: {type(tvd)}")
        print(f"Contents of amostra_probabilidade: {amostra_probabilidade}")
        print(f"Contents of tvd: {tvd}")

        canvas = self.create_plot(
            amostra_probabilidade,
            tvd,
            "TOMI index",
            "Profundidade (m)",
            "TOMI Index",
            invert_axis=invert_axis,
        )

        self.clear_and_set_layout(self.plotWidget, canvas)

    def create_plot(
        x_data, y_data, x_label, y_label, title, color=None, invert_axis=False
    ):
        fig, ax = plt.subplots()

        if color:
            ax.plot(x_data, y_data, color=color)
        else:
            ax.plot(x_data, y_data)

        if invert_axis:
            ax.invert_yaxis()

        ax.set_xlim(0, 100)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title, fontsize=14)

        return FigureCanvas(fig)

    def clear_and_set_layout(widget, canvas):
        """Modular function belonging to preview_wavelet"""
        if widget.layout() is not None:
            for i in reversed(range(widget.layout().count())):
                widget.layout().itemAt(i).widget().setParent(None)
        else:
            layout = QVBoxLayout(widget)
            widget.setLayout(layout)
        widget.layout().addWidget(canvas)

    def read_file(self):
        dataframe = pd.DataFrame()

        self.selected_file = self.fileNameInput.text()

        sheetTab = self.workbookComboBox.currentText()
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


def main():
    appctx = ApplicationContext()
    window = MainWindow()
    window.show()
    sys.exit(appctx.app.exec())


if __name__ == "__main__":
    main()
