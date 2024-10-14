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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QPushButton, QScrollBar, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 862)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_display = QWidget()
        self.page_display.setObjectName(u"page_display")
        self.page_display_layout = QHBoxLayout(self.page_display)
        self.page_display_layout.setObjectName(u"page_display_layout")
        self.display_plot_layout = QGridLayout()
        self.display_plot_layout.setObjectName(u"display_plot_layout")

        self.page_display_layout.addLayout(self.display_plot_layout)

        self.display_func_layout = QVBoxLayout()
        self.display_func_layout.setObjectName(u"display_func_layout")
        self.display_func_layout.setContentsMargins(5, 5, 5, 5)
        self.button_connect = QPushButton(self.page_display)
        self.button_connect.setObjectName(u"button_connect")
        self.button_connect.setMinimumSize(QSize(0, 50))
        self.button_connect.setCheckable(True)

        self.display_func_layout.addWidget(self.button_connect)

        self.button_file_path_save = QPushButton(self.page_display)
        self.button_file_path_save.setObjectName(u"button_file_path_save")
        self.button_file_path_save.setMinimumSize(QSize(0, 50))

        self.display_func_layout.addWidget(self.button_file_path_save)

        self.button_record = QPushButton(self.page_display)
        self.button_record.setObjectName(u"button_record")
        self.button_record.setMinimumSize(QSize(0, 50))
        self.button_record.setCheckable(True)

        self.display_func_layout.addWidget(self.button_record)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.display_func_layout.addItem(self.verticalSpacer)


        self.page_display_layout.addLayout(self.display_func_layout)

        self.page_display_layout.setStretch(0, 10)
        self.page_display_layout.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_display)
        self.page_analysis = QWidget()
        self.page_analysis.setObjectName(u"page_analysis")
        self.gridLayout = QGridLayout(self.page_analysis)
        self.gridLayout.setObjectName(u"gridLayout")
        self.analysis_fuc_layout = QVBoxLayout()
        self.analysis_fuc_layout.setObjectName(u"analysis_fuc_layout")
        self.analysis_fuc_layout.setContentsMargins(5, 5, 5, 5)
        self.button_file_path_select = QPushButton(self.page_analysis)
        self.button_file_path_select.setObjectName(u"button_file_path_select")
        self.button_file_path_select.setMinimumSize(QSize(0, 50))

        self.analysis_fuc_layout.addWidget(self.button_file_path_select)

        self.button_replay = QPushButton(self.page_analysis)
        self.button_replay.setObjectName(u"button_replay")
        self.button_replay.setMinimumSize(QSize(0, 50))
        self.button_replay.setCheckable(True)

        self.analysis_fuc_layout.addWidget(self.button_replay)

        self.button_matrix_analysis = QPushButton(self.page_analysis)
        self.button_matrix_analysis.setObjectName(u"button_matrix_analysis")
        self.button_matrix_analysis.setMinimumSize(QSize(0, 50))
        self.button_matrix_analysis.setCheckable(True)

        self.analysis_fuc_layout.addWidget(self.button_matrix_analysis)

        self.button_pictures_save = QPushButton(self.page_analysis)
        self.button_pictures_save.setObjectName(u"button_pictures_save")
        self.button_pictures_save.setMinimumSize(QSize(0, 50))

        self.analysis_fuc_layout.addWidget(self.button_pictures_save)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.analysis_fuc_layout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.analysis_fuc_layout, 0, 1, 1, 1)

        self.analysis_plot_layout = QGridLayout()
        self.analysis_plot_layout.setObjectName(u"analysis_plot_layout")

        self.gridLayout.addLayout(self.analysis_plot_layout, 0, 0, 1, 1)

        self.replayScrollBar = QScrollBar(self.page_analysis)
        self.replayScrollBar.setObjectName(u"replayScrollBar")
        self.replayScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.replayScrollBar, 1, 0, 1, 2)

        self.gridLayout.setColumnStretch(0, 10)
        self.gridLayout.setColumnStretch(1, 1)
        self.stackedWidget.addWidget(self.page_analysis)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.menuLayout = QHBoxLayout()
        self.menuLayout.setObjectName(u"menuLayout")
        self.button_data_display = QPushButton(self.centralwidget)
        self.button_data_display.setObjectName(u"button_data_display")
        self.button_data_display.setMinimumSize(QSize(0, 50))

        self.menuLayout.addWidget(self.button_data_display)

        self.button_data_analysis = QPushButton(self.centralwidget)
        self.button_data_analysis.setObjectName(u"button_data_analysis")
        self.button_data_analysis.setMinimumSize(QSize(0, 50))

        self.menuLayout.addWidget(self.button_data_analysis)


        self.verticalLayout.addLayout(self.menuLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.button_file_path_save.setText(QCoreApplication.translate("MainWindow", u"Select Path", None))
        self.button_record.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.button_file_path_select.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.button_replay.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
        self.button_matrix_analysis.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.button_pictures_save.setText(QCoreApplication.translate("MainWindow", u"Picture Save", None))
        self.button_data_display.setText(QCoreApplication.translate("MainWindow", u"Data Display", None))
        self.button_data_analysis.setText(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
    # retranslateUi

