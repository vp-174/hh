# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QMainWindow,
    QSizePolicy, QStatusBar, QWidget)
import rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(542, 104)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(542, 104))
        MainWindow.setMaximumSize(QSize(542, 104))
        icon = QIcon()
        icon.addFile(u":/icon/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.506, y1:1, x2:0.522, y2:0, stop:0 rgba(140, 140, 140, 255), stop:1 rgba(150, 150, 150, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineSearch = QLineEdit(self.centralwidget)
        self.lineSearch.setObjectName(u"lineSearch")
        self.lineSearch.setGeometry(QRect(11, 43, 522, 31))
        font = QFont()
        font.setPointSize(12)
        self.lineSearch.setFont(font)
        self.lineSearch.setCursor(QCursor(Qt.IBeamCursor))
        self.lineSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 4px 4px 8px 4px;\n"
"border-radius: 4px;")
        self.lineSearch.setClearButtonEnabled(True)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 10, 521, 24))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"hh parse | build/0003", None))
#if QT_CONFIG(tooltip)
        self.lineSearch.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineSearch.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineSearch.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.lineSearch.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.lineSearch.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.lineSearch.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0433\u043e\u0440\u043e\u0434\u0430", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0441\u043a\u0432\u0430", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0440\u043d\u0430\u0443\u043b", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u043e\u044f\u0440\u0441\u043a", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0427\u0435\u043b\u044f\u0431\u0438\u043d\u0441\u043a", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0433\u043e\u0440\u043e\u0434\u0430", None))
    # retranslateUi

