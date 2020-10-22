
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(self.get_bbox(100, 100, 800, 800))
        self.setWindowTitle('Scheduler v1.0')

        self.font_name = 'Arial'
        
        self.label_time = QtWidgets.QLabel(self)
        self.label_time.setGeometry(self.get_bbox(10, 10, 330, 30))
        self.label_time.setFont(self.get_font(self.font_name, 20, True))
        self.label_time.setText('2020-10-21 00 : 00 : 00')

        self.daily_progressbar = QtWidgets.QProgressBar(self)
        self.daily_progressbar.setGeometry(self.get_bbox(370, 15, 380, 20))
        self.daily_progressbar.setProperty('value', 50)

        self.section_start_x = 10
        self.section_start_y = 60

        self.section_dic = {}
        for section_index in range(2):
            self.get_section(section_index + 1, 100, (600, 20), 10)

    def get_section(self, section_index, btn_width, box_size, the_number_of_check_box):
        section_name = f'section_{section_index}'

        self.section_dic[section_name] = []

        for box_index in range(the_number_of_check_box):
            box = QtWidgets.QCheckBox(self)
            box.setEnabled(True)
            box.setGeometry(
                self.get_bbox(
                    self.section_start_x + btn_width + 30,
                    self.section_start_y + (box_size[1] + 5) * box_index, 
                    box_size[0], box_size[1]
                )
            )
            box.setFont(self.get_font(self.font_name, 12, False))
            self.section_dic[section_name].append(box)

        edit_box = QtWidgets.QLineEdit(self)
        edit_box.setGeometry(
            self.get_bbox(
                self.section_start_x + btn_width + 30,
                self.section_start_y + (box_size[1] + 5) * the_number_of_check_box,
                box_size[0], box_size[1]
            )
        )
        edit_box.setFont(self.get_font(self.font_name, 12, False))
        self.section_dic[section_name].append(edit_box)
        
        btn = QtWidgets.QPushButton(self)
        btn.setEnabled(False)
        btn.setGeometry(
            self.get_bbox(
                self.section_start_x, self.section_start_y, 
                btn_width, (box_size[1] + 5) * (the_number_of_check_box + 1)
            )
        )
        self.section_dic[section_name].append(btn)

        self.section_start_y += (box_size[1] + 5) * (the_number_of_check_box + 1)
        self.section_start_y += 20
        
    def get_bbox(self, xmin, ymin, width, height):
        return QtCore.QRect(xmin, ymin, width, height)

    def get_font(self, font_name, size, bold):
        font = QtGui.QFont()

        font.setFamily(font_name)
        font.setPointSize(size)
        font.setBold(bold)

        return font