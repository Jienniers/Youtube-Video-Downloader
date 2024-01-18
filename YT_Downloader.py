from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import time
from pytube import YouTube

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 487)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(106, 107, 104);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Url_label = QtWidgets.QLabel(self.frame)
        self.Url_label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Url_label.setObjectName("Url_label")
        self.horizontalLayout.addWidget(self.Url_label)
        self.Url_linedit = QtWidgets.QLineEdit(self.frame)
        self.Url_linedit.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"border:2px solid rgb(37, 150, 255);\n"
"")
        self.Url_linedit.setObjectName("Url_linedit")
        self.horizontalLayout.addWidget(self.Url_linedit)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Download_btn = QtWidgets.QPushButton(self.frame_2)
        self.Download_btn.setStyleSheet("QPushButton{\n"
"border:3px solid rgb(46, 140, 255);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(29, 93, 176);\n"
"}\n"
"QPushButton:Pressed{\n"
"border:2px solid rgb(33, 73, 255);\n"
"}")
        self.Download_btn.setObjectName("Download_btn")
        self.verticalLayout_3.addWidget(self.Download_btn)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.Downalod_location_label = QtWidgets.QLabel(self.frame_4)
        self.Downalod_location_label.setGeometry(QtCore.QRect(10, 20, 231, 51))
        self.Downalod_location_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.Downalod_location_label.setObjectName("Downalod_location_label")
        self.Download_location_linedit = QtWidgets.QLineEdit(self.frame_4)
        self.Download_location_linedit.setGeometry(QtCore.QRect(250, 20, 321, 51))
        self.Download_location_linedit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"border:2px solid rgb(37, 150, 255);\n"
"")
        self.Download_location_linedit.setObjectName("Download_location_linedit")
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Status_label = QtWidgets.QLabel(self.frame_3)
        self.Status_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 48pt \"MS Shell Dlg 2\";")
        self.Status_label.setObjectName("Status_label")
        self.horizontalLayout_2.addWidget(self.Status_label)
        self.Status_linedit = QtWidgets.QLineEdit(self.frame_3)
        self.Status_linedit.setMinimumSize(QtCore.QSize(358, 0))
        self.Status_linedit.setStyleSheet("font: 48pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"border:2px solid rgb(37, 150, 255);\n"
"")
        self.Status_linedit.setText("")
        self.Status_linedit.setObjectName("Status_linedit")
        self.horizontalLayout_2.addWidget(self.Status_linedit)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 21))
        self.menubar.setObjectName("menubar")
        self.menuYoutube = QtWidgets.QMenu(self.menubar)
        self.menuYoutube.setObjectName("menuYoutube")
        MainWindow.setMenuBar(self.menubar)
        self.actionVideo_Title = QtWidgets.QAction(MainWindow)
        self.actionVideo_Title.setObjectName("actionVideo_Title")
        self.actionVideo_Thumbnail_URl = QtWidgets.QAction(MainWindow)
        self.actionVideo_Thumbnail_URl.setObjectName("actionVideo_Thumbnail_URl")
        self.menuYoutube.addAction(self.actionVideo_Title)
        self.menuYoutube.addAction(self.actionVideo_Thumbnail_URl)
        self.menubar.addAction(self.menuYoutube.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


####################################################################################################
#######################################Connections#################################################
###################################################################################################

        self.Download_btn.clicked.connect(self.download)
        self.actionVideo_Title.triggered.connect(self.video_title)
        self.actionVideo_Thumbnail_URl.triggered.connect(self.Thumb_URL)


####################################################################################################
#######################################Connections End#############################################
###################################################################################################




####################################################################################################
#######################################Functions###################################################
###################################################################################################

    def download(self):
            url = YouTube(str(self.Url_linedit.text()))
            video = url.streams.get_highest_resolution()
            video.download(self.Download_location_linedit.text())
            self.Status_linedit.setText('Downloaded')


    def video_title(self):
            yt = YouTube(str(self.Url_linedit.text()))
            self.Status_linedit.setText(yt.title)

    def Thumb_URL(self):
            self.Status_linedit.setText('processing')
            Thumb = YouTube(str(self.Url_linedit.text()))
            self.Status_linedit.setText(Thumb.thumbnail_url)


####################################################################################################
#######################################Functions End################################################
###################################################################################################


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MGB Video Downloader"))
        self.Url_label.setText(_translate("MainWindow", "Url:"))
        self.Download_btn.setText(_translate("MainWindow", "Download"))
        self.Downalod_location_label.setText(_translate("MainWindow", "Download Location:"))
        self.Status_label.setText(_translate("MainWindow", "Status:"))
        self.menuYoutube.setTitle(_translate("MainWindow", "Youtube"))
        self.actionVideo_Title.setText(_translate("MainWindow", "Video Title"))
        self.actionVideo_Thumbnail_URl.setText(_translate("MainWindow", "Video Thumbnail URl"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
