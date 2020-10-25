
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'Scheduler v1.1'
        self.font_name = 'Arial'

        self.window_size = (1280, 800)
        self.table_size = (1240, 200)
        self.label_size = (350, 20)
        self.progress_size = (-1, 20)
        self.margin_size = (20, 10)

        self.setWindowTitle(self.title)
        self.setGeometry(self.get_bbox(100, 100, self.window_size[0], self.window_size[1]))

        self.table_header_labels = ['Finish', 'Task']
        
        self.section_start_x = self.margin_size[0]
        self.section_start_y = self.margin_size[1]

        self.section_dic = {}
        self.get_section(1, '# Monthly Goals', 1)
        self.get_section(2, '# Weekly Goals', 2)
        self.get_section(3, '# Daily Goals', 5)

    def keyPressEvent(self, event):
        print(event)

    def keypressed(self, event, section_name):
        print(event.key(), section_name)
        return QtWidgets.QTableWidget.keyPressEvent(self.section_dic[section_name]['table'], event)

    def get_section(self, section_index, label_name, the_number_of_box):
        section_name = f'section_{section_index}'
        self.section_dic[section_name] = {}
        
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
        
        table.setColumnWidth(0, 60)
        # table.setColumnWidth(1, 60)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        
        for row_index in range(the_number_of_box):
            self.add_cell(row_index, table)
        
        table.setHorizontalHeaderLabels(self.table_header_labels)
        table.verticalHeader().setVisible(False)

        table.keyPressEvent = lambda event: self.keypressed(event, section_name)

        self.section_dic[section_name]['label'] = label
        self.section_dic[section_name]['progressbar'] = progressbar
        self.section_dic[section_name]['table'] = table

        self.section_start_y += self.table_size[1]
        self.section_start_y += self.label_size[1]
        self.section_start_y += self.progress_size[1]
        self.section_start_y += self.margin_size[1]

    def add_cell(self, row_index, table):
        table.setRowHeight(row_index, 30)
        table.setCellWidget(row_index, 0, QCheckBox())
        
    def get_bbox(self, xmin, ymin, width, height):
        return QtCore.QRect(xmin, ymin, width, height)

    def get_font(self, font_name, size, bold):
        font = QtGui.QFont()

        font.setFamily(font_name)
        font.setPointSize(size)
        font.setBold(bold)

        return font