from PySide6.QtCore import QTimer, Slot, Qt
from PySide6.QtGui import QCloseEvent, QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QButtonGroup
from .mainUI import Ui_MainWindow
from .mat_48 import Mat

import time
import os
from .plot import SIZE_X, SIZE_Y
import csv


class mainWindow(QMainWindow, Ui_MainWindow):
    data_timer = QTimer(interval=5)

    def __init__(self) -> None:
        from .plot import MatMatrixPlot, MatMatrixRecord
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Mat Data Analysis")
        self.setWindowIcon(QIcon("src/resources/econ.ico"))
        self.plot = MatMatrixPlot()
        self.display_plot_layout.addWidget(self.plot)
        self.record = MatMatrixRecord()
        self.analysis_plot_layout.addWidget(self.record)

        self.dev = None
        self.dir_path = ""
        self.save_filename = None
        self.record_flag = False
        self.last_path = os.path.join(os.path.expanduser("~"), "mat")
        self.data_timer.timeout.connect(self.process_data)

        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.addButton(self.button_replay)
        self.buttonGroup.addButton(self.button_matrix_analysis)
        self.buttonGroup.addButton(self.button_pictures_save)
        self.buttonGroup.buttonClicked.connect(self.on_button_group_clicked)
        self.replayScrollBar.setVisible(False)
        self.replayScrollBar.valueChanged.connect(self.animation_replay)

        self.show()

    @Slot()
    def on_button_data_display_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    @Slot()
    def on_button_data_analysis_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    @Slot()
    def on_button_connect_clicked(self):
        if self.dev is None:
            try:
                self.dev = Mat()
                self.data_timer.start()
                self.button_connect.setText("Disconnect")
            except Exception:
                import traceback

                traceback.print_exc()
                self.dev = None
                warn = "Device not found, please plug in usb cable and power on mat."
                QMessageBox.warning(self, "Warning", warn)
        else:
            self.button_connect.setText("Connect")
            self.data_timer.stop()
            self.dev.close_dev()
            if self.record_flag:
                self.on_button_record_clicked()
            self.dev = None

    @Slot()
    def on_button_file_path_save_clicked(self):
        self.dir_path, _ = QFileDialog.getSaveFileName(
            self, "save", self.last_path, "CSV (*.csv)"
        )
        self.statusbar.showMessage(f"Selected filename: {self.dir_path}")
        self.last_path = self.dir_path[:-4] if self.dir_path else ""

    @Slot()
    def on_button_file_path_select_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "select", self.last_path, "CSV (*.csv)"
        )
        self.statusbar.showMessage(f"Selected filename: {file_path}")
        if file_path:
            self.last_path = file_path[:-4]
            self.record.upload_data(file_path)

    def process_data(self):
        if self.dev is None:
            return
        if not self.dev.run_flag:
            self.on_button_connect_clicked()
            QMessageBox.warning(self, "Warning", "Mat disconnected!")
            return
        if not self.dev.data_q.empty():
            timestamp, data = self.dev.data_q.get()
            self.plot.matrix_queue.put(data)
            if self.record_flag:
                with open(self.save_filename, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp] + data.flatten().tolist())

    @Slot()
    def on_button_record_clicked(self):
        if not self.record_flag:
            if self.dev is None:
                warn = "Please connect device first."
                self.button_record.setChecked(False)
                QMessageBox.warning(self, "Warning", warn)
                return
            if not self.dir_path:
                self.button_record.setChecked(False)
                QMessageBox.warning(self, "Warning", "Please select save path first.")
                return
            self.save_filename = (
                f"{self.dir_path[:-4]}-{time.strftime('%Y-%m-%d%-H%-M-%S')}.csv"
            )
            header = ["timestamp"] + [
                f"R{i//SIZE_Y}_C{i%SIZE_Y}" for i in range(SIZE_X * SIZE_Y)
            ]
            with open(self.save_filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(header)
            self.record_flag = True
            self.statusbar.showMessage(f"Data file path: {self.save_filename}")
            self.button_record.setText("Stop")
            self.plot.plot_start()
        else:
            self.statusbar.showMessage(f"File saved to: {self.save_filename}")
            self.save_filename = ""
            self.record_flag = False
            self.button_record.setChecked(False)
            self.button_record.setText("Record")
            self.plot.plot_stop()

    @Slot()
    def on_button_group_clicked(self, button):
        if self.record.matrix is None:
            button.setChecked(False)
            QMessageBox.warning(self, "Warning", "Please select a csv file first.")
        else:
            if button == self.button_replay:
                self.record.show(0)
                self.replayScrollBar.setVisible(True)
                self.replayScrollBar.setRange(0, len(self.record.matrix) - 1)
            elif button == self.button_matrix_analysis:
                self.record.analysis(0)
                self.replayScrollBar.setVisible(True)
                self.replayScrollBar.setRange(0, 3)
            elif button == self.button_pictures_save:
                self.replayScrollBar.setVisible(False)
                self.setEnabled(False)
                self.record.generate_analysed_pictures()
                self.record.generate_original_pictures()
                self.setEnabled(True)

    @Slot(int)
    def animation_replay(self, value: int):
        try:
            if self.button_replay.isChecked():
                self.record.show(value)
            else:
                self.record.analysis(value)
        except ValueError:
            QMessageBox.warning(self, "Warning", "No data to replay!")

    def keyPressEvent(self, event):
        if not self.replayScrollBar.isVisible():
            return
        if event.key() == Qt.Key_Left:
            self.replayScrollBar.setValue(self.replayScrollBar.value() - 1)
        elif event.key() == Qt.Key_Right:
            self.replayScrollBar.setValue(self.replayScrollBar.value() + 1)
