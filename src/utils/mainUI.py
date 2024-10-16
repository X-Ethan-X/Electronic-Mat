# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QScrollBar, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1096, 842)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plotLayout = QGridLayout()
        self.plotLayout.setObjectName(u"plotLayout")

        self.gridLayout_2.addLayout(self.plotLayout, 0, 0, 1, 1)

        self.menuLayout = QVBoxLayout()
        self.menuLayout.setObjectName(u"menuLayout")
        self.menuLayout.setContentsMargins(5, 5, 5, 5)
        self.button_file_path_select = QPushButton(self.centralwidget)
        self.button_file_path_select.setObjectName(u"button_file_path_select")
        self.button_file_path_select.setMinimumSize(QSize(0, 50))

        self.menuLayout.addWidget(self.button_file_path_select)

        self.button_replay = QPushButton(self.centralwidget)
        self.button_replay.setObjectName(u"button_replay")
        self.button_replay.setMinimumSize(QSize(0, 50))
        self.button_replay.setCheckable(True)

        self.menuLayout.addWidget(self.button_replay)

        self.button_matrix_analysis = QPushButton(self.centralwidget)
        self.button_matrix_analysis.setObjectName(u"button_matrix_analysis")
        self.button_matrix_analysis.setMinimumSize(QSize(0, 50))
        self.button_matrix_analysis.setCheckable(True)

        self.menuLayout.addWidget(self.button_matrix_analysis)

        self.button_pictures_save = QPushButton(self.centralwidget)
        self.button_pictures_save.setObjectName(u"button_pictures_save")
        self.button_pictures_save.setMinimumSize(QSize(0, 50))

        self.menuLayout.addWidget(self.button_pictures_save)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.menuLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.menuLayout, 0, 1, 1, 1)

        self.replayScrollBar = QScrollBar(self.centralwidget)
        self.replayScrollBar.setObjectName(u"replayScrollBar")
        self.replayScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.replayScrollBar, 1, 0, 1, 2)

        self.gridLayout_2.setColumnStretch(0, 10)
        self.gridLayout_2.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_file_path_select.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.button_replay.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
        self.button_matrix_analysis.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.button_pictures_save.setText(QCoreApplication.translate("MainWindow", u"Picture Save", None))
    # retranslateUi

