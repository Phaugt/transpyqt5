#gui dep
from PyQt5.QtWidgets import QPlainTextEdit, QMainWindow, QApplication, QPushButton, QTextEdit, QComboBox, QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import sys
#function dep
import pyperclip
from googletrans import Translator, LANGUAGES
#for images and other sources
import image_rc

# variables
#language = LANGCODES = list(LANGUAGES.values()) #not using the complete list from googletrans
language = ["norwegian", "swedish", "english"]

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
        self.DetectLang = self.findChild(QTextEdit, "DetectLang")

        #button for detecting langugage
        self.DetectLang_2 = self.findChild(QPushButton, "DetectLang_2")
        self.DetectLang_2.setToolTip("Guesses the langugage if confidence is above 50% \nwhen guessing language outpuy of the translation is set to Swedish")
        self.DetectLang_2.clicked.connect(self.cmdDetect)

        #button for source language
        self.SrcLang = self.findChild(QComboBox, "SrcLang")
        self.SrcLang.addItems(language)

        #button for translation
        self.Translate = self.findChild(QPushButton, "Translate")
        self.Translate.clicked.connect(self.cmdTranslate)

        #textbox to be translated
        self.textedit = self.findChild(QTextEdit, "textEdit")

        #paste clipboard to translate
        self.PasteCP = self.findChild(QPushButton, "PasteCP")
        self.PasteCP.clicked.connect(self.cmdPasteCP)

        #show gui
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
    
    @pyqtSlot()
    def cmdDetect(self):
        translator = Translator()
        guess = translator.detect(text=self.textEdit.toPlainText())
        if guess.confidence > 0.5:
            translated=translator.translate(text= self.textEdit.toPlainText() , src = guess.lang, dest = 'swedish')
            self.DestText.setText(translated.text)
            fixfloat = str(guess.confidence)
            self.DetectLang.setText(guess.lang +" with an confidence of : " + fixfloat)
    
    @pyqtSlot()
    def cmdTranslate():
        translator = Translator()
        translated=translator.translate(text= self.textEdit.toPlainText(), src = self.SrcLang.toPlainText(), dest = self.DestLang.toPlainText())
        self.DestText.setText(translated.text)
        self.DetectLang.clear()

app = QApplication(sys.argv)
window = UI()
app.exec_()