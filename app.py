#gui dep
from PyQt5.QtWidgets import QPlainTextEdit, QMainWindow, QApplication, QPushButton, QTextEdit, QComboBox, QLineEdit, qApp
from PyQt5 import uic
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
import sys
#function dep
import pyperclip
from googletrans import Translator, LANGUAGES
#for images and other sources
import image_rc

# variables
#language = LANGCODES = list(LANGUAGES.values()) #not using the complete list from googletrans
language = ["norwegian", "swedish", "english", "polish"]

# GUI
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("main.ui", self)
        ## find the widgets in the xml file

        #button to clear all textboxes
        self.ClearBox = self.findChild(QPushButton, "ClearBox")
        self.ClearBox.clicked.connect(self.cmdClearBox)

        #copy translation
        self.CopyTrans = self.findChild(QPushButton, "CopyTrans")
        self.CopyTrans.clicked.connect(self.cmdCopy)

        #Combobox for destination langugage
        self.DestLang = self.findChild(QComboBox, "DestLang")
        self.DestLang.addItems(language)
        self.DestLang.currentText()

        #Textbox for translation
        self.DestText = self.findChild(QTextEdit, "DestText")

        #output for detecting langugage
        self.DetectLang = self.findChild(QTextEdit, "DetectLang")

        #button for detecting langugage
        self.DetectLang_2 = self.findChild(QPushButton, "DetectLang_2")
        self.DetectLang_2.setToolTip("Guesses the langugage if confidence is above 50% \nwhen guessing language output of the translation is set to Swedish")
        self.DetectLang_2.clicked.connect(self.cmdDetect)

        #button for source language
        self.SrcLang = self.findChild(QComboBox, "SrcLang")
        self.SrcLang.addItems(language)
        self.SrcLang.currentText()

        #button for translation
        self.Translate = self.findChild(QPushButton, "Translate")
        self.Translate.clicked.connect(self.cmdTranslate)

        #textbox to be translated
        self.textedit = self.findChild(QTextEdit, "textEdit")

        #paste clipboard to translate
        self.PasteCP = self.findChild(QPushButton, "PasteCP")
        self.PasteCP.clicked.connect(self.cmdPasteCP)

        #exit app
        self.ExitApp = self.findChild(QPushButton, "Exit")
        self.ExitApp.clicked.connect(qApp.quit)
        #show gui
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def cmdPasteCP(self):
        self.textedit.clear()
        paste = pyperclip.paste()
        self.textedit.setText(paste)

    def cmdClearBox(self):
        self.DestText.clear()
        self.DetectLang.clear()
        self.textedit.clear()

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
window = UI()
app.exec_()