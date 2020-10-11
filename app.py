#gui dep
from PyQt5.QtWidgets import QPlainTextEdit, QMainWindow, QApplication, QPushButton, QTextEdit, QComboBox, QLineEdit, qApp, QMessageBox
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
#function dep
import pyperclip
from googletrans import Translator, LANGUAGES
#for images and other sources
import image_rc

#icon taskbar
try:
    from PyQt5.QtWinExtras import QtWin
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass

# variables
#language = LANGCODES = list(LANGUAGES.values()) #not using the complete list from googletrans
language = ["norwegian", "swedish", "english", "polish"]

# GUI
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        UIFile = QtCore.QFile('main.ui')
        UIFile.open(QtCore.QFile.ReadOnly)
        uic.loadUi(UIFile, self)
        UIFile.close()

        #button to clear all textboxes
        self.ClearBox.clicked.connect(self.cmdClearBox)

        #copy translation
        self.CopyTrans.clicked.connect(self.cmdCopy)

        #Combobox for destination langugage
        self.DestLang.addItems(language)
        self.DestLang.currentText()


        #button for detecting langugage
        self.DetectLang_2.setToolTip("Guesses the langugage if confidence is above 50% \nwhen guessing language output of the translation is set to Swedish")
        self.DetectLang_2.clicked.connect(self.cmdDetect)

        #button for source language
        self.SrcLang.addItems(language)
        self.SrcLang.currentText()

        #button for translation
        self.Translate.clicked.connect(self.cmdTranslate)

        #paste clipboard to translate
        self.PasteCP.clicked.connect(self.cmdPasteCP)

        #exit app
        self.Exit.clicked.connect(qApp.quit)
        
        #show gui
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def cmdPasteCP(self):
        self.textEdit.clear()
        paste = pyperclip.paste()
        self.textEdit.setText(paste)

    def cmdClearBox(self):
        self.DestText.clear()
        self.DetectLang.clear()
        self.textEdit.clear()

    def cmdCopy(self):
        pyperclip.copy(self.DestText.toPlainText())
    
    def cmdDetect(self):
        translator = Translator()
        guess = translator.detect(text=self.textEdit.toPlainText())
        if guess.confidence > 0.5:
            translated=translator.translate(text= self.textEdit.toPlainText() , src = guess.lang, dest = 'swedish')
            self.DestText.setText(translated.text)
            fixfloat = str(guess.confidence)
            self.DetectLang.setText(guess.lang +" with an confidence of : " + fixfloat)
    
    def cmdTranslate(self):
        translator = Translator()
        SrcLangText = self.SrcLang.currentText()
        DestLangText = self.DestLang.currentText()
        self.CheckBlank = self.textEdit.toPlainText()

        if len(self.CheckBlank) == 0:
            QMessageBox.information(self, "ERROR!", "No text to translate, add text and try again!")
        
        else:
            translated=translator.translate(text= self.textEdit.toPlainText(), src = SrcLangText, dest = DestLangText)
            self.DestText.setText(translated.text)
            self.DetectLang.clear()

    #move window frameless
    def mousePressEvent(self, event):
    
        if event.buttons() == Qt.RightButton:
            self.dragPos = event.globalPos()
            event.accept()
        elif event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
    
        if event.buttons() == Qt.RightButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
        elif event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


app = QApplication(sys.argv)
app.setStyleSheet('QMainWindow{border: 1px solid black;}')
app.setWindowIcon(QtGui.QIcon('sources/Volue_icon.svg'))
window = UI()
app.exec_()