from PyQt5.QtWidgets import (
    QFileDialog,
    QVBoxLayout,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
from sklearn.impute import SimpleImputer
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import uic
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
import sys

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

        self.exportDataButton.clicked.connect(self.export_data)

        self.tomi_dataframe = None

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
            "tests",
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
        self.tomi_dataframe = self.read_file()
        d15N = self.tomi_dataframe["d15N"].values
        d13C = self.tomi_dataframe["d13C"].values
        TOC_TN = self.tomi_dataframe["TOC/TN"].values

        # Dados dos pontos-chave de probabilidade do
        TOC_TN_ARTIGO = np.array(
            [4, 4, 4, 4, 10, 10, 10, 10, 100, 100, 100, 100]
        )  # Lista/array dos valores de TOC:TN dos pontos-chave
        C13CORG_ARTIGO = np.array(
            [-10, -22, -25, -34, -10, -22, -25, -34, -10, -22, -25, -34]
        )  # Lista/array dos valores de δ13Corg dos pontos-chave
        D15N_ARTIGO = np.array(
            [12, 3, 0, -12, 12, 3, 0, -12, 12, 3, 0, -12]  # MUDAR
        )  # Lista/array dos valores do terceiro variável

        PROBABILIDADE = np.array(
            [0, 10, 20, 30, 20, 30, 40, 50, 90, 95, 98, 100]
        )  # Lista/array dos valores de probabilidade dos pontos-chave

        # Dados das suas amostras
        amostra_TOC_TN = TOC_TN
        amostra_C13CORG = d13C
        amostra_D15N = d15N

        # Sample data
        X = np.column_stack((TOC_TN_ARTIGO, C13CORG_ARTIGO, D15N_ARTIGO))
        y = PROBABILIDADE

        # Define the kernel
        kernel = C(1.0, (1e-3, 1e3)) * RBF(
            length_scale=1.0, length_scale_bounds=(1e-2, 1e2)
        )

        # Create the Gaussian Process model
        gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

        # Fit to the data
        gp.fit(X, y)

        # Predict on new data
        X_new = np.column_stack((amostra_TOC_TN, amostra_C13CORG, amostra_D15N))

        # Handle NaN values by imputing them
        imputer = SimpleImputer(strategy="mean")
        X_new_imputed = imputer.fit_transform(X_new)

        # Predict with the imputed data
        y_pred, sigma = gp.predict(X_new_imputed, return_std=True)

        amostra = 100 - y_pred

        return amostra

    def mesa_rotativa_conversion(self, mesaRotativaInput, profundidade):
        return mesaRotativaInput - profundidade

    def plot_TOMI_index(self):
        self.tomi_dataframe = self.read_file()
        profundidade = self.tomi_dataframe.iloc[:, 0]

        tomi_index = self.tomi_index_calculation()
        print(tomi_index)
        tomi_index = pd.Series(tomi_index)

        canvas = self.create_plot(
            tomi_index,
            profundidade,
            "TOMI index",
            "Profundidade (m)",
            "TOMI Index",
            color="blue",
        )
        self.matplotlib_toolbar = NavigationToolbar2QT(canvas)
        self.saveButton.clicked.connect(self.matplotlib_toolbar.save_figure)

        self.clear_and_set_layout(self.plotWidget, canvas)

    def create_plot(self, x_data, y_data, x_label, y_label, title, color=None):
        fig, ax = plt.subplots()

        if color:
            ax.plot(x_data, y_data, "s-", color=color, label="TOMI")
        else:
            ax.plot(x_data, y_data, "s-", label="TOMI")

        ax.invert_yaxis()

        ax.set_xlim(0, 100)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title, fontsize=14)
        ax.grid()

        return FigureCanvas(fig)

    def clear_and_set_layout(self, widget, canvas):
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

    def export_data(self):
        self.tomi_dataframe = self.read_file()
        profundidade = self.tomi_dataframe.iloc[:, 0]
        # tvdss = self.tomi_dataframe.iloc[:, 1]
        d15N = self.tomi_dataframe["d15N"].values
        d13C = self.tomi_dataframe["d13C"].values
        TOC_TN = self.tomi_dataframe["TOC/TN"].values
        amostra_probabilidade = self.tomi_index_calculation()

        export_dataframe = pd.DataFrame(
            {
                "Prof": profundidade,
                "d15N": d15N,
                "d13C": d13C,
                "TOC_TN": TOC_TN,
                "TOMI Index": amostra_probabilidade,
            }
        )

        export_dataframe = self.format_dataframe(export_dataframe)

        # Open a file dialog for the user to select the file name and location
        dialog = QFileDialog()
        filename, _ = dialog.getSaveFileName(filter="Excel files (*.xlsx)")

        self.formationCheck = "Formação"

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

    def format_dataframe(self, dataframe):
        new_dataframe = pd.DataFrame(columns=dataframe.columns)

        for index, row in dataframe.iterrows():
            # Repeat each row three times
            for i in range(3):
                new_row = row.copy()
                new_row.iloc[0] = row.iloc[0] - 2 + i
                new_dataframe = pd.concat(
                    [new_dataframe, pd.DataFrame([new_row])], ignore_index=True
                )

        dataframe = new_dataframe

        return dataframe


def main():
    appctx = ApplicationContext()
    window = MainWindow()
    window.show()
    sys.exit(appctx.app.exec())


if __name__ == "__main__":
    main()
