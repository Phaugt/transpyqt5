#gui dep
from PyQt5.QtWidgets import QPlainTextEdit, QMainWindow, QApplication, QPushButton, QTextEdit, QComboBox
from PyQt5 import uic
import sys
#function dep
import pyperclip
from googletrans import Translator, LANGUAGES
#for images and other sources
import image_rc

# variables
language = LANGCODES = list(LANGUAGES.values())

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

        #Textbox for translation
        self.DestText = self.findChild(QTextEdit, "DestText")

        #output for detecting langugage
        self.DetectLang = self.findChild(QPlainTextEdit, "DetectLang")

        #button for detecting langugage
        self.DetectLang_2 = self.findChild(QPushButton, "DetectLang_2")

        #button for source language
        self.SrcLang = self.findChild(QComboBox, "SrcLang")
        self.SrcLang.addItems(language)
        #button for translation
        self.Translate = self.findChild(QPushButton, "Translate")

        #textbox to be translated
        self.textedit = self.findChild(QTextEdit, "textEdit")


        #show gui
        self.show()

    def cmdClearBox(self):
        self.DestText.clear()
        self.DetectLang.clear()
        self.textedit.clear()

    def cmdCopy(self):
        pyperclip.copy(self.DestText.toPlainText())


app = QApplication(sys.argv)
window = UI()
app.exec_()