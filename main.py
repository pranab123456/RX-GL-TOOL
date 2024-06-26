# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMessageBox
import sys
import os
import subprocess
import tempfile
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 250)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Optional: make the background translucent
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: #222831; border-radius: 18px; border:")
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(260, 70, 90, 90))
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 70, 100, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(25, 224, 255, 1), stop: 1 rgba(85, 98, 112,
226));
	color:rgba(255,255,255,210);
                border: 2px solid #59D5E0;
                border-radius: 50px;
                padding: 0px 0px;
                font-size: 17px;
                
            }
            QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop: 1 rgba(25, 224, 255, 1));
	color:rgba(255,255,255,210);
                color: #41C9E2;
                
            }
            QPushButton:pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop: 1 rgba(85, 98, 112,
226));
	color:rgba(255,255,255,210);
                color: #41C9E2;
                border: 2px solid #222831;
                
            }
            
        """)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 10, 20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: #FF204E;
                color: #000000;
                border: 2px solid red;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 20px;
                
            }
            QPushButton:hover {
                background-color: darkred;
                border: 3px solid red;
                color: white;
            }
            QPushButton:pressed {
                background-color: transparent;
                color: white;
            }
            
        """)  # Close function
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 10, 20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(MainWindow.showMinimized)
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                background-color: #41C9E2;
                color: #000000;
                border: 2px solid cyan;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 20px;
                
            }
            QPushButton:hover {
                background-color: #41C567;
                color: white;
            }
            QPushButton:pressed {
                background-color: transparent;
                color: white;
            }
            
        """)  # Minimize function
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 200, 75, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.unlock)
        MainWindow.setCentralWidget(self.centralwidget)

        self.loadImage()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadImage(self):
        image_paths = [
            r"C:\Program Files\BlueStacks\ProductLogo.png",
            r"C:\Program Files\BlueStacks_msi2\ProductLogo.png",
            r"C:\Program Files\BlueStacks_msi5\ProductLogo.png",
            r"C:\Program Files\BlueStacks_arabica\ProductLogo.png",
            r"C:\Program Files\BlueStacks_nxt\ProductLogo.png"
        ]

        for path in image_paths:
            if os.path.exists(path):
                self.label.setPixmap(QtGui.QPixmap(path))
                break

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "ACTIVATE"))
        self.pushButton.clicked.connect(self.setHighPerformance)
        self.pushButton_2.setText(_translate("MainWindow", "X"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "RATE99"))

    def setHighPerformance(self):
        directories = [
            r"C:\ProgramData\BlueStacks\Client",
            r"C:\Program Files\BlueStacks",
            r"C:\Program Files\BlueStacks_msi2",
            r"C:\Program Files\BlueStacks_msi5",
            r"C:\Program Files\BlueStacks_arabica",
            r"C:\Program Files\BlueStacks_nxt",
        ]
        executables = [
            "Bluestacks.exe",
            "HD-Player.exe",
            "HD-ForceGPU.exe",
            "HD-GLCheck.exe",
        ]
        success = []
        failure = []

        for directory in directories:
            for exe in executables:
                filePath = os.path.join(directory, exe)
                if os.path.exists(filePath):
                    result = self.setGraphicsPreference(filePath)
                    if result:
                        success.append(filePath)
                    else:
                        failure.append(filePath)

        if success:
            QMessageBox.information(None, "Success", f"Set high performance for:\n" + "\n".join(success))
        if failure:
            QMessageBox.warning(None, "Failure", f"Failed to set high performance for:\n" + "\n".join(failure))

    def setGraphicsPreference(self, filePath):
        script = f'''
        $path = "{filePath}"
        $key = "HKCU:\\SOFTWARE\\Microsoft\\DirectX\\UserGpuPreferences"

        if (-not (Test-Path $key)) {{
            New-Item -Path $key -Force
        }}

        Set-ItemProperty -Path $key -Name "{filePath}" -Value "GpuPreference=2;"
        '''

        with tempfile.NamedTemporaryFile(delete=False, suffix=".ps1") as script_file:
            script_file.write(script.encode('utf-8'))
            script_file_path = script_file.name

        try:
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_file_path], check=True)
            return True
        except subprocess.CalledProcessError:
            return False
        finally:
            os.remove(script_file_path)

    def unlock(self):
           QDesktopServices.openUrl(QUrl('https://rate99.blogspot.com/'))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
