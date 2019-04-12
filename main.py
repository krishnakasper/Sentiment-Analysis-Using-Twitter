# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from search import Search

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.threadStart)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.clear)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 641, 391))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 389))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(-1, -1, 641, 391))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.createApi()
        # status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # setting text in status bar
        self.statusbar.showMessage("Welcome")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))

    def threadStart(self):
        thread = threading.Thread(target=self.startSearch)
        thread.start()

    def createApi(self):
        # creating object of TwitterClient Class
        self.api = Search()

    def startSearch(self):
        string = str(self.plainTextEdit.toPlainText())
        # calling function to get tweets
        tweets = self.api.get_tweets(query=string , count=200)

        # picking positive tweets from tweets
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        # percentage of positive tweets
        print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
        # picking negative tweets from tweets
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        # percentage of negative tweets
        result = "Negative tweets percentage: {} %\n".format(100 * len(ntweets) / len(tweets))
        # percentage of neutral tweets
        result = result + "Neutral tweets percentage: {} % \ \n".format(100 * len(tweets - ntweets - ptweets) / len(tweets))

        # printing first 5 positive tweets
        result = result + "\n\nPositive tweets:\n"
        for tweet in ptweets[:10]:
            result = result + tweet['text'] +"\n"

        # printing first 5 negative tweets
        result = result + "\n\nNegative tweets:"
        for tweet in ntweets[:10]:
            result = result + tweet['text']+"\n"
        self.plainTextEdit_2.setPlainText(result)

    def clear(self):
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit.setPlainText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

