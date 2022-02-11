# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def __init__(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(850, 670)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)
        self.main_widget = QtWidgets.QWidget(main_window)
        self.main_widget.setObjectName("main_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_toolBox_layout = QtWidgets.QGridLayout()
        self.main_toolBox_layout.setObjectName("main_toolBox_layout")
        self.toolBox_frame = QtWidgets.QFrame(self.main_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.toolBox_frame.sizePolicy().hasHeightForWidth())
        self.toolBox_frame.setSizePolicy(size_policy)
        self.toolBox_frame.setMinimumSize(QtCore.QSize(163, 609))
        self.toolBox_frame.setBaseSize(QtCore.QSize(163, 609))
        self.toolBox_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.toolBox_frame.setObjectName("toolBox_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.toolBox_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox_title = QtWidgets.QLabel(self.toolBox_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.toolBox_title.sizePolicy().hasHeightForWidth())
        self.toolBox_title.setSizePolicy(size_policy)
        self.toolBox_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolBox_title.setFont(font)
        self.toolBox_title.setAutoFillBackground(False)
        self.toolBox_title.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.toolBox_title.setFrameShape(QtWidgets.QFrame.Panel)
        self.toolBox_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBox_title.setAlignment(QtCore.Qt.AlignCenter)
        self.toolBox_title.setObjectName("toolBox_title")
        self.verticalLayout.addWidget(self.toolBox_title)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.toolBox_sizes_title = QtWidgets.QLabel(self.toolBox_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.toolBox_sizes_title.sizePolicy().hasHeightForWidth())
        self.toolBox_sizes_title.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBox_sizes_title.setFont(font)
        self.toolBox_sizes_title.setAlignment(QtCore.Qt.AlignCenter)
        self.toolBox_sizes_title.setObjectName("toolBox_sizes_title")
        self.verticalLayout.addWidget(self.toolBox_sizes_title)
        self.toolBox_vertical_layout = QtWidgets.QVBoxLayout()
        self.toolBox_vertical_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.toolBox_vertical_layout.setObjectName("toolBox_vertical_layout")
        self.wxh_label_horizontal_layout = QtWidgets.QHBoxLayout()
        self.wxh_label_horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.wxh_label_horizontal_layout.setObjectName("wxh_label_horizontal_layout")
        self.width_label = QtWidgets.QLabel(self.toolBox_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.width_label.sizePolicy().hasHeightForWidth())
        self.width_label.setSizePolicy(size_policy)
        self.width_label.setAlignment(QtCore.Qt.AlignCenter)
        self.width_label.setObjectName("width_label")
        self.wxh_label_horizontal_layout.addWidget(self.width_label)
        self.height_label = QtWidgets.QLabel(self.toolBox_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.height_label.sizePolicy().hasHeightForWidth())
        self.height_label.setSizePolicy(size_policy)
        self.height_label.setAlignment(QtCore.Qt.AlignCenter)
        self.height_label.setObjectName("height_label")
        self.wxh_label_horizontal_layout.addWidget(self.height_label)
        self.toolBox_vertical_layout.addLayout(self.wxh_label_horizontal_layout)
        self.wxh_spinBox_horizontal_layout = QtWidgets.QHBoxLayout()
        self.wxh_spinBox_horizontal_layout.setObjectName("wxh_spinBox_horizontal_layout")
        self.width_spinBox = QtWidgets.QSpinBox(self.toolBox_frame)
        self.width_spinBox.setObjectName("width_spinBox")
        self.wxh_spinBox_horizontal_layout.addWidget(self.width_spinBox)
        self.height_spinBox = QtWidgets.QSpinBox(self.toolBox_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.height_spinBox.sizePolicy().hasHeightForWidth())
        self.height_spinBox.setSizePolicy(size_policy)
        self.height_spinBox.setObjectName("height_spinBox")
        self.wxh_spinBox_horizontal_layout.addWidget(self.height_spinBox)
        self.toolBox_vertical_layout.addLayout(self.wxh_spinBox_horizontal_layout)
        self.verticalLayout.addLayout(self.toolBox_vertical_layout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.toolBox_line_1 = QtWidgets.QFrame(self.toolBox_frame)
        self.toolBox_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.toolBox_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.toolBox_line_1.setObjectName("toolBox_line_1")
        self.verticalLayout.addWidget(self.toolBox_line_1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.toolBox_colors_title = QtWidgets.QLabel(self.toolBox_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.toolBox_colors_title.sizePolicy().hasHeightForWidth())
        self.toolBox_colors_title.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBox_colors_title.setFont(font)
        self.toolBox_colors_title.setAlignment(QtCore.Qt.AlignCenter)
        self.toolBox_colors_title.setObjectName("toolBox_colors_title")
        self.verticalLayout.addWidget(self.toolBox_colors_title)
        self.colors_comboBox = QtWidgets.QComboBox(self.toolBox_frame)
        self.colors_comboBox.setObjectName("colors_comboBox")
        self.verticalLayout.addWidget(self.colors_comboBox)
        self.colors_table_button = QtWidgets.QPushButton(self.toolBox_frame)
        self.colors_table_button.setObjectName("colors_table_button")
        self.verticalLayout.addWidget(self.colors_table_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.toolBox_line_2 = QtWidgets.QFrame(self.toolBox_frame)
        self.toolBox_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.toolBox_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.toolBox_line_2.setObjectName("toolBox_line_2")
        self.verticalLayout.addWidget(self.toolBox_line_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.reset_button_horizontal_layout = QtWidgets.QHBoxLayout()
        self.reset_button_horizontal_layout.setObjectName("reset_button_horizontal_layout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reset_button_horizontal_layout.addItem(spacerItem5)
        self.reset_button = QtWidgets.QPushButton(self.toolBox_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(size_policy)
        self.reset_button.setObjectName("reset_button")
        self.reset_button_horizontal_layout.addWidget(self.reset_button)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.reset_button_horizontal_layout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.reset_button_horizontal_layout)
        self.save_button_horizontal_layout = QtWidgets.QHBoxLayout()
        self.save_button_horizontal_layout.setObjectName("save_button_horizontal_layout")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.save_button_horizontal_layout.addItem(spacerItem7)
        self.save_button = QtWidgets.QPushButton(self.toolBox_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(size_policy)
        self.save_button.setObjectName("save_button")
        self.save_button_horizontal_layout.addWidget(self.save_button)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.save_button_horizontal_layout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.save_button_horizontal_layout)
        self.export_button_horizontal_layout = QtWidgets.QHBoxLayout()
        self.export_button_horizontal_layout.setObjectName("export_button_horizontal_layout")
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.export_button_horizontal_layout.addItem(spacerItem9)
        self.export_button = QtWidgets.QPushButton(self.toolBox_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(size_policy)
        self.export_button.setObjectName("export_button")
        self.export_button_horizontal_layout.addWidget(self.export_button)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.export_button_horizontal_layout.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.export_button_horizontal_layout)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem11)
        self.main_toolBox_layout.addWidget(self.toolBox_frame, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.main_toolBox_layout)
        self.main_pattern_layout = QtWidgets.QGridLayout()
        self.main_pattern_layout.setObjectName("main_pattern_layout")
        self.pattern_frame = QtWidgets.QFrame(self.main_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.pattern_frame.sizePolicy().hasHeightForWidth())
        self.pattern_frame.setSizePolicy(size_policy)
        self.pattern_frame.setMinimumSize(QtCore.QSize(659, 609))
        self.pattern_frame.setBaseSize(QtCore.QSize(659, 609))
        self.pattern_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.pattern_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pattern_frame.setObjectName("pattern_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.pattern_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pattern_openGL_widget = QtWidgets.QOpenGLWidget(self.pattern_frame)
        self.pattern_openGL_widget.setObjectName("pattern_openGL_widget")
        self.gridLayout.addWidget(self.pattern_openGL_widget, 0, 0, 1, 1)
        self.main_pattern_layout.addWidget(self.pattern_frame, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.main_pattern_layout)
        main_window.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_export_as = QtWidgets.QMenu(self.menu_file)
        self.menu_export_as.setObjectName("menu_export_as")
        self.menu_matrix = QtWidgets.QMenu(self.menu_export_as)
        self.menu_matrix.setObjectName("menu_matrix")
        self.menu_pattern = QtWidgets.QMenu(self.menu_export_as)
        self.menu_pattern.setObjectName("menu_pattern")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.action_new = QtWidgets.QAction(main_window)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(main_window)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(main_window)
        self.action_save.setObjectName("action_save")
        self.action_save_as = QtWidgets.QAction(main_window)
        self.action_save_as.setObjectName("action_save_as")
        self.action_matrix_text_file_txt = QtWidgets.QAction(main_window)
        self.action_matrix_text_file_txt.setObjectName("action_matrix_text_file_txt")
        self.action_matrix_json = QtWidgets.QAction(main_window)
        self.action_matrix_json.setObjectName("action_matrix_json")
        self.action_matrix_tabler_csv = QtWidgets.QAction(main_window)
        self.action_matrix_tabler_csv.setObjectName("action_matrix_tabler_csv")
        self.action_matrix_tabler_xls = QtWidgets.QAction(main_window)
        self.action_matrix_tabler_xls.setObjectName("action_matrix_tabler_xls")
        self.action_matrix_tabler_xlsx = QtWidgets.QAction(main_window)
        self.action_matrix_tabler_xlsx.setObjectName("action_matrix_tabler_xlsx")
        self.action_matrix_image = QtWidgets.QAction(main_window)
        self.action_matrix_image.setObjectName("action_matrix_image")
        self.action_matrix_image_jpg = QtWidgets.QAction(main_window)
        self.action_matrix_image_jpg.setObjectName("action_matrix_image_jpg")
        self.action_matrix_image_wout_bg_png = QtWidgets.QAction(main_window)
        self.action_matrix_image_wout_bg_png.setObjectName("action_matrix_image_wout_bg_png")
        self.action_matrix_image_white_bg_png = QtWidgets.QAction(main_window)
        self.action_matrix_image_white_bg_png.setObjectName("action_matrix_image_white_bg_png")
        self.action_matrix_vector_svg = QtWidgets.QAction(main_window)
        self.action_matrix_vector_svg.setObjectName("action_matrix_vector_svg")
        self.action_matrix_pdf = QtWidgets.QAction(main_window)
        self.action_matrix_pdf.setObjectName("action_matrix_pdf")
        self.action_pattern_image_jpeg = QtWidgets.QAction(main_window)
        self.action_pattern_image_jpeg.setObjectName("action_pattern_image_jpeg")
        self.action_pattern_image_jpg = QtWidgets.QAction(main_window)
        self.action_pattern_image_jpg.setObjectName("action_pattern_image_jpg")
        self.action_pattern_wout_bg_png = QtWidgets.QAction(main_window)
        self.action_pattern_wout_bg_png.setObjectName("action_pattern_wout_bg_png")
        self.action_pattern_white_bg_png = QtWidgets.QAction(main_window)
        self.action_pattern_white_bg_png.setObjectName("action_pattern_white_bg_png")
        self.action_pattern_vector = QtWidgets.QAction(main_window)
        self.action_pattern_vector.setObjectName("action_pattern_vector")
        self.action_pattern_pdf = QtWidgets.QAction(main_window)
        self.action_pattern_pdf.setObjectName("action_pattern_pdf")
        self.action_help = QtWidgets.QAction(main_window)
        self.action_help.setObjectName("action_help")
        self.action_about_pb = QtWidgets.QAction(main_window)
        self.action_about_pb.setObjectName("action_about_pb")
        self.action_about_author = QtWidgets.QAction(main_window)
        self.action_about_author.setObjectName("action_about_author")
        self.action_join_us = QtWidgets.QAction(main_window)
        self.action_join_us.setObjectName("action_join_us")
        self.menu_matrix.addAction(self.action_matrix_text_file_txt)
        self.menu_matrix.addAction(self.action_matrix_json)
        self.menu_matrix.addSeparator()
        self.menu_matrix.addAction(self.action_matrix_tabler_csv)
        self.menu_matrix.addAction(self.action_matrix_tabler_xls)
        self.menu_matrix.addAction(self.action_matrix_tabler_xlsx)
        self.menu_matrix.addSeparator()
        self.menu_matrix.addAction(self.action_matrix_image)
        self.menu_matrix.addAction(self.action_matrix_image_jpg)
        self.menu_matrix.addAction(self.action_matrix_image_wout_bg_png)
        self.menu_matrix.addAction(self.action_matrix_image_white_bg_png)
        self.menu_matrix.addAction(self.action_matrix_vector_svg)
        self.menu_matrix.addAction(self.action_matrix_pdf)
        self.menu_pattern.addAction(self.action_pattern_image_jpeg)
        self.menu_pattern.addAction(self.action_pattern_image_jpg)
        self.menu_pattern.addAction(self.action_pattern_wout_bg_png)
        self.menu_pattern.addAction(self.action_pattern_white_bg_png)
        self.menu_pattern.addAction(self.action_pattern_vector)
        self.menu_pattern.addAction(self.action_pattern_pdf)
        self.menu_export_as.addAction(self.menu_matrix.menuAction())
        self.menu_export_as.addAction(self.menu_pattern.menuAction())
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_file.addAction(self.menu_export_as.menuAction())
        self.menu_help.addAction(self.action_help)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.action_about_pb)
        self.menu_help.addAction(self.action_about_author)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.action_join_us)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Pattern Builder by lyl-Lynx"))
        self.toolBox_title.setText(_translate("main_window", "Tool box"))
        self.toolBox_sizes_title.setText(_translate("main_window", "Sizes"))
        self.width_label.setText(_translate("main_window", "Width"))
        self.height_label.setText(_translate("main_window", "Height"))
        self.toolBox_colors_title.setText(_translate("main_window", "Colors"))
        self.colors_table_button.setText(_translate("main_window", "Open colors table"))
        self.reset_button.setText(_translate("main_window", "Reset pattern"))
        self.save_button.setText(_translate("main_window", "Save"))
        self.export_button.setText(_translate("main_window", "Export"))
        self.menu_file.setTitle(_translate("main_window", "File"))
        self.menu_export_as.setTitle(_translate("main_window", "Export as..."))
        self.menu_matrix.setTitle(_translate("main_window", "Matrix"))
        self.menu_pattern.setTitle(_translate("main_window", "Pattern"))
        self.menu_help.setTitle(_translate("main_window", "Help"))
        self.action_new.setText(_translate("main_window", "New..."))
        self.action_open.setText(_translate("main_window", "Open..."))
        self.action_save.setText(_translate("main_window", "Save"))
        self.action_save_as.setText(_translate("main_window", "Save as..."))
        self.action_matrix_text_file_txt.setText(_translate("main_window", "Text file (.txt)"))
        self.action_matrix_json.setText(_translate("main_window", "JSON (.json)"))
        self.action_matrix_tabler_csv.setText(_translate("main_window", "Tabler (.csv)"))
        self.action_matrix_tabler_xls.setText(_translate("main_window", "Tabler (.xls)"))
        self.action_matrix_tabler_xlsx.setText(_translate("main_window", "Tabler (.xlsx)"))
        self.action_matrix_image.setText(_translate("main_window", "Image (.jpeg)"))
        self.action_matrix_image_jpg.setText(_translate("main_window", "Image (.jpg)"))
        self.action_matrix_image_wout_bg_png.setText(_translate("main_window", "Without background (.png)"))
        self.action_matrix_image_white_bg_png.setText(_translate("main_window", "With white background (.png)"))
        self.action_matrix_vector_svg.setText(_translate("main_window", "Vector (.svg)"))
        self.action_matrix_pdf.setText(_translate("main_window", "PDF (.pdf)"))
        self.action_pattern_image_jpeg.setText(_translate("main_window", "Image (.jpeg)"))
        self.action_pattern_image_jpg.setText(_translate("main_window", "Image (.jpg)"))
        self.action_pattern_wout_bg_png.setText(_translate("main_window", "Without background (.png)"))
        self.action_pattern_white_bg_png.setText(_translate("main_window", "With white background (.png)"))
        self.action_pattern_vector.setText(_translate("main_window", "Vector (.svg)"))
        self.action_pattern_pdf.setText(_translate("main_window", "PDF (.pdf)"))
        self.action_help.setText(_translate("main_window", "Pattern builder help"))
        self.action_about_pb.setText(_translate("main_window", "About Pattern builder"))
        self.action_about_author.setText(_translate("main_window", "About lyl-Lynx"))
        self.action_join_us.setText(_translate("main_window", "Join us on GitHub !"))

app = QtWidgets.QApplication(sys.argv)
# create window
window = QtWidgets.QMainWindow()

ui = UiMainWindow(window)
# fill window
#ui.setupUi(window)

window.show()

sys.exit(app.exec_())
