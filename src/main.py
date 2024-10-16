if __name__ == "__main__":
    import os
    import sys

    from PySide6.QtWidgets import QApplication
    import resource_rc  # noqa: F401
    from utils.mainWindow import mainWindow

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    app = QApplication()
    main = mainWindow()
    sys.exit(app.exec())
