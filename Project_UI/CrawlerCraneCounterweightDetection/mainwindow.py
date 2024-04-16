# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget,QFileDialog
from PySide6.QtCore import QDir
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stream_import.clicked.connect(self.stream_import)
        self.ui.stream_reload.clicked.connect(self.stream_reload)
        self.stream_path=""
        self.ui.open_file.clicked.connect(self.open_file)

    def is_unique(self,current_item, combo_box):
        for index in range(combo_box.count()):
            if combo_box.itemText(index) == current_item:
                return False
        return True

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open File")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mov)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if len(selected_files) == 1:
                if self.is_unique(selected_files[0], self.ui.file_list):
                    self.ui.file_list.addItem(selected_files[0])
                self.ui.file_list.setCurrentText(selected_files[0])
            else:
                return

    def stream_import(self):
        self.stream_path = str(self.ui.file_list.currentText())
        self.ui.stackedWidget.setCurrentIndex(1)

    def stream_reload(self):
        self.ui.stackedWidget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
