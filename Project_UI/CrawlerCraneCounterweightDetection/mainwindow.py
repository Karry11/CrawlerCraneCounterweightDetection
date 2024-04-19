# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
import sys
from PySide6.QtWidgets import QApplication, QWidget,QFileDialog,QButtonGroup
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
        self.ui.open_stream_file.clicked.connect(lambda:self.open_file(0))
        self.ui.open_weight_file.clicked.connect(lambda:self.open_file(1))
        self.deviceButtonGroup = QButtonGroup()
        self.deviceButtonGroup.addButton(self.ui.GPU)
        self.deviceButtonGroup.addButton(self.ui.CPU)
        self.deviceButtonGroup.buttonClicked.connect(self.device_select)
        self.ui.conf_value.setText("0.50")
        self.ui.mask.clicked.connect(self.show_mask)
        self.ui.box.clicked.connect(self.show_box)
        self.ui.Label.clicked.connect(self.show_label)
        self.stream_inference_thread=""
        self.imgsz=640
        self.conf=0.5
        self.device="cuda:0"
        self.half=False
        self.weight_path="../../utils/best.pt"
        self.weight_sr = "../../utils/ESPCN_x2.pb"
        self.weight_character = "../../CounterweightCharacterRecognition/detect/train/weights/best.pt"
        self.ui.conf.valueChanged.connect(self.sliderChanged)

    def show_mask(self):
        self.stream_inference_thread.mask = (lambda x: True if x.isChecked() else False)(self.ui.mask)

    def show_box(self):
        self.stream_inference_thread.box = (lambda x: True if x.isChecked() else False)(self.ui.box)

    def show_label(self):
        self.stream_inference_thread.label = (lambda x: True if x.isChecked() else False)(self.ui.Label)

    def sliderChanged(self, value):
        formatted_str = "{:.2f}".format(value/100)
        self.ui.conf_value.setText(formatted_str)

    def is_unique(self,current_item, combo_box):
        for index in range(combo_box.count()):
            if combo_box.itemText(index) == current_item:
                return False
        return True

    def open_file(self,type):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Open File")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setViewMode(QFileDialog.Detail)
        if type==0:
            file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mov)")
            if file_dialog.exec():
                selected_files = file_dialog.selectedFiles()
                if len(selected_files) == 1:
                    if self.is_unique(selected_files[0], self.ui.stream_file_list):
                        self.ui.stream_file_list.addItem(selected_files[0])
                    self.ui.stream_file_list.setCurrentText(selected_files[0])
                else:
                    return
        elif type ==1:
            file_dialog.setNameFilter("Weight Files (*.pt)")
            if file_dialog.exec():
                selected_files = file_dialog.selectedFiles()
                if len(selected_files) == 1:
                    if self.is_unique(selected_files[0], self.ui.weight_file_list):
                        self.ui.weight_file_list.addItem(selected_files[0])
                    self.ui.weight_file_list.setCurrentText(selected_files[0])
                else:
                    return

    def stream_import(self):
        self.stream_path = str(self.ui.stream_file_list.currentText())
        self.stream_path = int(self.stream_path) if str.isdigit(self.stream_path) else self.stream_path
        self.weight_path = str(self.ui.weight_file_list.currentText())
        self.imgsz = int(self.ui.imgsz.text())
        self.device = "cuda:0" if self.ui.GPU.isChecked() else "CPU"
        self.conf = self.ui.conf.value()*0.01
        self.stream_inference_thread = Stream_Inference(self.stream_path,self.weight_path,self.imgsz,self.conf,self.device,self.half,self.weight_sr, self.weight_character)
        self.stream_inference_thread.processed_image.connect(self.display_processed_image)
        self.stream_inference_thread.result_info.connect(self.display_results)
        self.stream_inference_thread.start()
        self.ui.stackedWidget.setCurrentIndex(1)

    def stream_reload(self):
        self.stream_inference_thread.stop()
        self.ui.stackedWidget.setCurrentIndex(0)

    def display_processed_image(self, image):
        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.scaled(self.ui.annotated_image.size())
        self.ui.annotated_image.setPixmap(pixmap)

    def display_results(self,num_weight,total_mass,total_mass_L,total_mass_R,warming_info):
        self.ui.num_weight.setText(str(num_weight))
        self.ui.total_mass.setText(str(total_mass))
        self.ui.total_mass_L.setText(str(total_mass_L))
        self.ui.total_mass_R.setText(str(total_mass_R))
        self.ui.warming_info.setText(warming_info)

    def device_select(self,button):
        buttons = self.deviceButtonGroup.buttons()
        for item in buttons:
            if item==button:
                item.setChecked(True)
            else:
                item.setChecked(False)
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
