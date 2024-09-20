from PySide6.QtCore import QTimer, Slot
from PySide6.QtGui import QCloseEvent
from UI.mainWindow_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from mat_48 import Mat
# from mat_Test import Mat
import time
import os
from plot import SIZE_X, SIZE_Y
import csv
from spectrum import SpecWindow


class mainWindow(QMainWindow, Ui_MainWindow):
    data_timer = QTimer(interval=5)

    def __init__(self) -> None:
        from plot import matPlot

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Mat data reader")
        self.plot = matPlot()
        self.gridLayout_2.addWidget(self.plot)
        self.dev = None
        self.dir_path = ""
        self.record_flag = False
        self.data_timer.timeout.connect(self.plot.update_plot)
        self.data_timer.timeout.connect(self.process_data)
        self.last_path = os.path.join(os.path.expanduser("~"), "record")
        # self.btn_spectrum.setCheckable(True)
        self.btn_spectrum.setVisible(False)
        # self.spectrum = SpecWindow(
        #     8, {i: f"R{i//SIZE_Y}_C{i%SIZE_Y}" for i in range(SIZE_X * SIZE_Y)}
        # )
        # self.spectrum.finished.connect(
        #     lambda: self.on_btn_spectrum_clicked(check=False)
        # )
        self.show()

    # @Slot(bool)
    # def on_btn_spectrum_clicked(self, check):
    #     self.btn_spectrum.setChecked(check)
    #     if check:
    #         self.spectrum.timer.start()
    #         self.spectrum.show()
    #     else:
    #         self.spectrum.close()

    @Slot()
    def on_btn_connect_clicked(self):
        if self.dev is None:
            try:
                self.dev = Mat()
                self.data_timer.start()
                self.btn_connect.setText("Disconnect")
            except Exception:
                import traceback

                traceback.print_exc()
                self.dev = None
                warn = "Device not found, please plug in usb cable and power on mat."
                QMessageBox.warning(self, "Warning", warn)
        else:
            self.btn_connect.setText("Connect")
            self.data_timer.stop()
            self.dev.close_dev()
            if self.record_flag:
                self.on_btn_record_clicked()
            self.dev = None

    @Slot()
    def on_pushButton_3_clicked(self):
        self.dir_path, _ = QFileDialog.getSaveFileName(
            self, "save", self.last_path, "CSV (*.csv)"
        )
        self.statusbar.showMessage(f"Selected filename: {self.dir_path}")
        self.last_path = self.dir_path[:-4] if self.dir_path else ""

    def process_data(self):
        if self.dev is None:
            return
        if not self.dev.run_flag:
            self.on_btn_connect_clicked()
            QMessageBox.warning(self, "Warning", "Mat disconnected!")
            return
        if not self.dev.data_q.empty():
            timestamp, data = self.dev.data_q.get()
            self.plot.data_q.put(data)
            # if hasattr(self, "spectrum"):
            #     self.spectrum.update_data([data])
            if self.record_flag:
                with open(self.save_filename, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp] + data.flatten().tolist())

    @Slot()
    def on_btn_record_clicked(self):
        if not self.record_flag:
            if self.dev is None:
                warn = "Please connect device first."
                self.btn_record.setChecked(False)
                QMessageBox.warning(self, "Warning", warn)
                return
            if not self.dir_path:
                self.btn_record.setChecked(False)
                QMessageBox.warning(self, "Warning", "Please select save path first.")
                return
            self.save_filename = (
                f"{self.dir_path[:-4]}_{time.strftime('%Y%m%d%H%M%S')}.csv"
            )
            header = ["timestamp"] + [
                f"R{i//SIZE_Y}_C{i%SIZE_Y}" for i in range(SIZE_X * SIZE_Y)
            ]
            with open(self.save_filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(header)
            self.record_flag = True
            self.statusbar.showMessage(f"Data file path: {self.save_filename}")
            self.btn_record.setText("Stop")
        else:
            self.statusbar.showMessage(f"File saved to: {self.save_filename}")
            self.save_filename = ""
            self.record_flag = False
            self.btn_record.setChecked(False)
            self.btn_record.setText("Record")

    def closeEvent(self, event: QCloseEvent) -> None:
        if self.dev is not None:
            self.on_btn_connect_clicked()
        return super().closeEvent(event)
