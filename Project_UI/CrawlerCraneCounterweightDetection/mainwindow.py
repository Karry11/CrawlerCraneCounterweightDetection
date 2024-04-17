# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
import sys
from PySide6.QtWidgets import QApplication, QWidget,QFileDialog
from PySide6.QtCore import QDir,Qt
from PySide6.QtGui import QPixmap
from ui_form import Ui_MainWindow
from Stream_Inference import Stream_Inference

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
        self.stream_inference_thread=""
        self.imgsz=640
        self.conf=0.5
        self.device="cuda:0"
        self.half=False
        self.weight_path="D:\Download\yolov8s-seg.pt"

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
        self.stream_path = int(self.stream_path) if str.isdigit(self.stream_path) else self.stream_path
        self.stream_inference_thread = Stream_Inference(self.stream_path,self.weight_path,self.imgsz,self.conf,self.device,self.half)
        self.stream_inference_thread.processed_image.connect(self.display_processed_image)
        self.stream_inference_thread.start()
        self.ui.stackedWidget.setCurrentIndex(1)

    def stream_reload(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def display_processed_image(self, image):
        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.scaled(self.ui.annotated_image.size())
        self.ui.annotated_image.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
