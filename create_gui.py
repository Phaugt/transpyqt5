import os

dir = os.getcwd()

os.system("cd dir")

os.system("pyuic5 -x translator.ui -o main.py")

os.system("pyrcc5 sources/image.qrc -o image_rc.py")