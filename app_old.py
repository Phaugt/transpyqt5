#import UI
from main import Ui_Dialog
#import commands
from command import *
#import dep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class Main(Ui_Dialog):

    def __init__(self, Dialog):
        super(Main, self).__init__()
        self.setupUi(self)

    def setupUi(self):

        self.SrcLang.addItems(language)

        #destlang
        self.DestLang.addItems(language)

        self.Translate.clicked.connect(self.on_click)

        self.CopyTrans.click(pyperclip.copy(self.DestText.toPlainText()))

        self.DetectLang_2.click(self.DetectLang_command)
        self.show()

    @pyqtSlot()
    def Translate_command(self):
        translator = Translator()
        translated=translator.translate(text= self.textEdit.toPlainText() , src = self.SrcLang.toPlainText(), dest = self.DestLang.toPlainText())
        self.DestText.setText(translated.text)
        
    @pyqtSlot()
    def DetectLang_command(self):
        translator = Translator()
        guess = translator.detect(text=self.textEdit.toPlainText())
        if guess.confidence > 0.5:
            translated=translator.translate(text= self.textEdit.toPlainText() , src = guess.lang, dest = 'swedish')
            self.DestText.setText(translated.text)
            self.DetectLang.setText(guess)
    
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
