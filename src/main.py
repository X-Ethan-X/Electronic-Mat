if __name__ == "__main__":
    import os
    import sys

    from PySide6.QtGui import QPixmap
    from PySide6.QtWidgets import QApplication

    from mainWindow import mainWindow
    from UI import res_rc

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    app = QApplication()
    app.setWindowIcon(QPixmap(":/def/econ.ico"))
    main = mainWindow()
    sys.exit(app.exec())
