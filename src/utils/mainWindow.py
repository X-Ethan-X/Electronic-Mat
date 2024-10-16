from PySide6.QtCore import QTimer, Slot, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QButtonGroup

from .mainUI import Ui_MainWindow

import os


class mainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        from .plot import MatMatrixRecord
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Mat Data Analysis")
        self.setWindowIcon(QIcon(":/src/resources/econ.ico"))
        self.plot = MatMatrixRecord()
        self.plotLayout.addWidget(self.plot, 0, 0)

        self.dev = None
        self.dir_path = ""
        self.save_filename = None
        self.record_flag = False
        self.last_path = os.path.join(os.path.expanduser("~"), "mat")

        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.addButton(self.button_replay)
        self.buttonGroup.addButton(self.button_matrix_analysis)
        self.buttonGroup.addButton(self.button_pictures_save)
        self.buttonGroup.buttonClicked.connect(self.on_button_group_clicked)
        self.replayScrollBar.setVisible(False)
        self.replayScrollBar.valueChanged.connect(self.animation_replay)

        self.show()

    @Slot()
    def on_button_file_path_select_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "select", self.last_path, "CSV (*.csv)"
        )
        self.statusbar.showMessage(f"Selected filename: {file_path}")
        if file_path:
            self.last_path = file_path[:-4]
            self.plot.upload_data(file_path)

    @Slot()
    def on_button_group_clicked(self, button):
        if self.plot.matrix is None:
            button.setChecked(False)
            QMessageBox.warning(self, "Warning", "Please select a csv file first.")
        else:
            if button == self.button_replay:
                self.plot.show(0)
                self.replayScrollBar.setVisible(True)
                self.replayScrollBar.setRange(0, len(self.plot.matrix) - 1)
            elif button == self.button_matrix_analysis:
                self.plot.analysis(0)
                self.replayScrollBar.setVisible(True)
                self.replayScrollBar.setRange(0, 3)
            elif button == self.button_pictures_save:
                self.replayScrollBar.setVisible(False)
                self.setEnabled(False)
                self.plot.generate_analysed_pictures()
                self.plot.generate_original_pictures()
                self.setEnabled(True)

    @Slot(int)
    def animation_replay(self, value: int):
        try:
            if self.button_replay.isChecked():
                self.plot.show(value)
            else:
                self.plot.analysis(value)
        except ValueError:
            QMessageBox.warning(self, "Warning", "No data to replay!")

    def keyPressEvent(self, event):
        if not self.replayScrollBar.isVisible():
            return
        if event.key() == Qt.Key_Left:
            self.replayScrollBar.setValue(self.replayScrollBar.value() - 1)
        elif event.key() == Qt.Key_Right:
            self.replayScrollBar.setValue(self.replayScrollBar.value() + 1)
