import pyperclip
from googletrans import Translator, LANGUAGES 


#combobox srclang
language = LANGCODES = list(LANGUAGES.values())



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


        asdasdasd