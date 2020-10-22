
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Scheduler v1.1'
        self.font_name = 'Arial'

        self.window_size = (1280, 1080)
        self.table_size = (1260, 300)
        self.label_size = (350, 20)
        self.progress_size = (-1, 20)
        self.margin_size = (20, 10)

        self.setWindowTitle(self.title)
        self.setGeometry(self.get_bbox(100, 100, self.window_size[0], self.window_size[1]))

        self.table_header_labels = ['Finish', 'Index', 'Task']
        
        self.section_start_x = self.margin_size[0]
        self.section_start_y = self.margin_size[1]

        self.section_dic = {}
        self.get_section(1, '# Monthly Goals', 3)
        self.get_section(2, '# Weekly Goals', 5)
        self.get_section(3, '# Daily Goals', 10)

    def get_section(self, section_index, label_name, the_number_of_box):
        section_name = f'section_{section_index}'

        self.section_dic[section_name] = []
        
        label = QtWidgets.QLabel(self)
        label.setGeometry(self.get_bbox(self.section_start_x, self.section_start_y, self.label_size[0], self.label_size[1]))
        label.setFont(self.get_font(self.font_name, 15, True))
        label.setText(label_name)

        progressbar = QtWidgets.QProgressBar(self)
        progressbar.setGeometry(
            self.get_bbox(
                self.section_start_x + self.label_size[0] + self.margin_size[0], self.section_start_y, 
                self.window_size[0] - (self.section_start_x + self.label_size[0] + self.margin_size[0] * 2), self.progress_size[1]
            )
        )
        progressbar.setProperty('value', 50)
        
        table = QtWidgets.QTableWidget(the_number_of_box, len(self.table_header_labels), parent=self)
        table.setGeometry(self.get_bbox(self.section_start_x, self.section_start_y + self.progress_size[1] + self.margin_size[1], self.table_size[0], self.table_size[1]))
        
        table.setColumnWidth(0, 30)
        table.setColumnWidth(1, 30)
        table.setColumnWidth(2, self.table_size[0] - (30 * 2))
        
        for i in range(the_number_of_box):
            table.setRowHeight(i, 30)
        
        table.setHorizontalHeaderLabels(self.table_header_labels)
        table.verticalHeader().setVisible(False)

        self.section_dic[section_name].append(label)
        self.section_dic[section_name].append(progressbar)
        self.section_dic[section_name].append(table)

        self.section_start_y += self.table_size[1]
        self.section_start_y += self.label_size[1]
        self.section_start_y += self.progress_size[1]
        self.section_start_y += self.margin_size[1]
        
    def get_bbox(self, xmin, ymin, width, height):
        return QtCore.QRect(xmin, ymin, width, height)

    def get_font(self, font_name, size, bold):
        font = QtGui.QFont()

        font.setFamily(font_name)
        font.setPointSize(size)
        font.setBold(bold)

        return font