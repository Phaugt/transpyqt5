import os

dir = os.getcwd()

os.system("cd dir")

#os.system("pyuic5 -x translator.ui -o main.py")

os.system("pyrcc5 src/main/resources/images/image.qrc -o src/main/python/image_rc.py")