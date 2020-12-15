#gui dep
from PyQt5.QtWidgets import (QPlainTextEdit, QMainWindow, QApplication, QPushButton, QTextEdit, QComboBox, QLineEdit, qApp, QMessageBox)
from PyQt5 import (uic, QtCore, QtGui)
from PyQt5.QtGui import (QIcon, QPalette, QLinearGradient, QColor, QBrush, QImage, QPixmap)
from PyQt5.QtCore import (Qt, QFile)
import sys, os
#function dep
import pyperclip
from googletrans import Translator, LANGUAGES


#icon taskbar
try:
    from PyQt5.QtWinExtras import QtWin
    myappid = 'pythonexplained.python.translate.program'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass
#pyinstaller
def resource_path(relative_path):
    """"for pyinstaller"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)
# variables
language = ["norwegian", "swedish", "english", "polish"]
tr_gui = resource_path("./icons/app_ui.ui")
tr_icon = resource_path("./icons/55translate.png")
tr_bg = resource_path("./icons/appbg.png")
translator = Translator()

# GUI
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        UIFile = QFile(tr_gui)
        UIFile.open(QFile.ReadOnly)
        uic.loadUi(UIFile, self)
        UIFile.close()

        #button to clear all textboxes
        self.ClearBox.clicked.connect(self.cmdClearBox)

        #copy translation
        self.CopyTrans.clicked.connect(self.cmdCopy)

        #Combobox for destination langugage
        self.DestLang.addItems(language)
        self.DestLang.currentText()
        bgimage = QImage(tr_bg)
        self.appbg.setPixmap(QPixmap(bgimage))
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
        self.setWindowFlags(Qt.FramelessWindowHint)

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
        textToDetect = text=self.textEdit.toPlainText()
        try:
            
            if textToDetect == "":
                pass

            else:
                guess = translator.detect(textToDetect)
                self.DestLang.setCurrentText("swedish")
                translated=translator.translate(text= self.textEdit.toPlainText(),dest = 'swedish' , src = guess.lang)
                self.DestText.setText(translated.text)
                self.DetectLang.setText(f"Detected langugage: {guess.lang}")
        except NameError:
            pass
        except AttributeError:
            pass
        finally:
            pass
    
    def cmdTranslate(self):
        SrcLangText = self.SrcLang.currentText()
        DestLangText = self.DestLang.currentText()
        CheckBlank = self.textEdit.toPlainText()
        try:
            if CheckBlank == "":
                QMessageBox.information(self, "ERROR!", "No text to translate, add text and try again!")
        
            else:
                translated=translator.translate(text= CheckBlank, src = SrcLangText, dest = DestLangText)
                self.DestText.setText(translated.text)
                self.DetectLang.clear()
        except NameError:
            pass
        except AttributeError:
            pass
        finally:
            pass

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

style = '''
QPushButton, 
QLineEdit, 
QSpinBox, 
QComboBox, 
QTextEdit {
    background-color: #eeeeee;
    selection-color: #eeeeee;
    border-color: #393E46;
    border: 3px;
    color: #393E46;
}
QComboBox QAbstractItemView {
    selection-color: #FED369;
    selection-background-color: #222831;
    background-color: #eeeeee;

}
QLabel {
    color: #eeeeee;
}
QPushButton:hover,
QTextEdit:hover,
QComboBox:hover {
    color: #000000;
    background-color: #F1F1F1;
    border-color: #393E46;
    border: 3px;
}  
QPushButton:pressed {
    color: #000000;
    background-color: #FFFFFF;
    border-color: #393E46;
    border: 3px;
}  
'''

app = QApplication(sys.argv)
app.setStyleSheet('QMainWindow{border: 1px solid black;}')
app.setWindowIcon(QIcon(tr_icon))
app.setStyleSheet(style) 
window = UI()
window.show()
app.exec_()
