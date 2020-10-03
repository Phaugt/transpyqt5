# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from googletrans import Translator, LANGUAGES 
import sys 

language = LANGCODES = list(LANGUAGES.values())

class Window(QMainWindow): 

	def __init__(self): 
		super().__init__() 

		# setting title 
		self.setWindowTitle("Python ") 

		# setting geometry 
		self.setGeometry(100, 100, 600, 400) 

		# calling method 
		self.UiComponents() 

		# showing all the widgets 
		self.show() 

	# method for widgets 
	def UiComponents(self): 

		# creating a combo box widget 
		combo_box = QComboBox(self) 

		# setting geometry of combo box 
		combo_box.setGeometry(200, 150, 120, 30) 

		# geek list 
		geek_list = ["Geek", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"] 

		# adding list of items to combo box 
		combo_box.addItems(language) 
		

# create pyqt5 app 
App = QApplication(sys.argv) 

# create the instance of our Window 
window = Window() 

# start the app 
sys.exit(App.exec()) 
