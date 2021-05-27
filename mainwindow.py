# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# TODO:
# 点击列表中视频，将视频加载到播放区域，点击播放才播放
# 将还没有剪辑的视频放到未剪辑文件夹，读取出文件夹中所有的文件，将名称显示在界面上
# 将剪辑完的视频放到剪辑完成文件夹
# 将已经发布的视频放到已发布文件夹
# 统计视频件数
# 统计发布平台
# 获取平台信息并进行观看反馈分析


import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 398)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.widget_video_play = QtWidgets.QWidget(self.centralWidget)
        self.widget_video_play.setGeometry(QtCore.QRect(260, 20, 241, 241))
        self.widget_video_play.setObjectName("widget_video_play")

        # 设置视频播放区域
        self.mdiArea = QVideoWidget(MainWindow)
        self.mdiArea.setGeometry(QtCore.QRect(280, 80, 200, 160))
        self.mdiArea.show()
        self.player = QMediaPlayer()

        self.pushButton = QtWidgets.QPushButton(self.widget_video_play)
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_video_play)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget_orignial_list = QtWidgets.QWidget(self.centralWidget)
        self.widget_orignial_list.setGeometry(QtCore.QRect(10, 20, 201, 91))
        self.widget_orignial_list.setObjectName("widget_orignial_list")
        self.listWidget = QtWidgets.QListWidget(self.widget_orignial_list)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 181, 71))
        self.listWidget.setObjectName("listWidget")
        self.widget_already_changed_list = QtWidgets.QWidget(self.centralWidget)
        self.widget_already_changed_list.setGeometry(QtCore.QRect(10, 130, 201, 91))
        self.widget_already_changed_list.setObjectName("widget_already_changed_list")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_already_changed_list)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 10, 181, 71))
        self.listWidget_2.setObjectName("listWidget_2")
        self.widget_published_list = QtWidgets.QWidget(self.centralWidget)
        self.widget_published_list.setGeometry(QtCore.QRect(10, 240, 201, 91))
        self.widget_published_list.setObjectName("widget_published_list")
        self.listWidget_3 = QtWidgets.QListWidget(self.widget_published_list)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 10, 181, 71))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 54, 12))
        self.label_3.setObjectName("label_3")
        self.widget_next_video_to_deal = QtWidgets.QWidget(self.centralWidget)
        self.widget_next_video_to_deal.setGeometry(QtCore.QRect(260, 269, 241, 51))
        self.widget_next_video_to_deal.setObjectName("widget_next_video_to_deal")
        self.undoView = QtWidgets.QUndoView(self.widget_next_video_to_deal)
        self.undoView.setGeometry(QtCore.QRect(10, 20, 231, 21))
        self.undoView.setObjectName("undoView")
        self.label_4 = QtWidgets.QLabel(self.widget_next_video_to_deal)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 171, 16))
        self.label_4.setObjectName("label_4")
        self.widget_orignial_list.raise_()
        self.widget_already_changed_list.raise_()
        self.widget_published_list.raise_()
        self.widget_video_play.raise_()
        self.mdiArea.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.widget_next_video_to_deal.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 545, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.actionversion_1_0_1 = QtWidgets.QAction(MainWindow)
        self.actionversion_1_0_1.setObjectName("actionversion_1_0_1")
        self.actionAuthor_Y = QtWidgets.QAction(MainWindow)
        self.actionAuthor_Y.setObjectName("actionAuthor_Y")
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionversion_1_0_1)
        self.menu_2.addAction(self.actionAuthor_Y)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小鱼资源管理系统"))
        self.pushButton.setText(_translate("MainWindow", "播放"))
        self.pushButton_2.setText(_translate("MainWindow", "停止"))
        self.label.setText(_translate("MainWindow", "未剪辑"))
        self.label_2.setText(_translate("MainWindow", "已剪辑"))
        self.label_3.setText(_translate("MainWindow", "已发布"))
        self.label_4.setText(_translate("MainWindow", "下一个要处理的视频"))
        self.menu.setTitle(_translate("MainWindow", "资源管理系统"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.actionversion_1_0_1.setText(_translate("MainWindow", "version:1.0.1"))
        self.actionAuthor_Y.setText(_translate("MainWindow", "Author:-Y-"))


class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 给button的点击动作绑定一个事件处理函数
        # 播放按钮
        self.ui.pushButton.clicked.connect(self.play_video)
        # 停止按钮
        self.ui.pushButton_2.clicked.connect(self.stop_playing_video)

    def get_namelist_in_target_dictionary(self, target_dictionary):
        target_dictionary_path = target_dictionary
        filelist = []

        for file in os.walk(target_dictionary_path):
            # print(file[2])
            for i in file[2]:
                filelist.append(i)
        print(filelist)
        for name in filelist:
            global j
            if j == 0:
                self.ui.listWidget.addItem(name)
            elif j == 1:
                self.ui.listWidget_2.addItem(name)
            elif j == 2:
                self.ui.listWidget_3.addItem(name)

    def exec_time(self):
        target = input("请输入目标文件目录：")
        window.get_namelist_in_target_dictionary(target)

    def play_video(self):
        # 点击按钮进行播放
        # 先获取播放路径

        print("点击了播放")

        # 在指定的条件下播放
        self.ui.player.setVideoOutput(self.ui.mdiArea)
        self.ui.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.ui.player.play()

    def stop_playing_video(self):
        print("点击了停止")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = query_window()
    j = 0
    while j < 3:
        window.exec_time()
        j += 1
    window.show()
    sys.exit(app.exec_())
