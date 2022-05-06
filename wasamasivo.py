import os
import sys
import webbrowser 
import pyautogui
import time

from selenium import webdriver 
global direccion_tel 
global driver
global direccion_multimedia

from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
Ui_MainWindow, QtBaseClass = uic.loadUiType('diseno.ui')
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Mensajes de WhatsApp masivos")
        self.botonlista.clicked.connect(self.lista)
        self.botonimagenvideo.clicked.connect(self.imagenvideo)
        self.botonenviar.clicked.connect(self.enviar)
   
    def lista(self):
        global direccion_tel
        self.dir_tel = QFileDialog.getOpenFileName(self,"Seleccione telefonos","c:\\")
        direccion_tel, *_=self.dir_tel
        print(direccion_tel)    

    def imagenvideo(self):
        self.dir_multimedia = QFileDialog.getOpenFileName(self,"Seleccione imagen o video","c:\\")
        direccion_multimedia, *_=self.dir_multimedia
        print(direccion_multimedia) 

    def enviar(self):
              
        mensaje=self.textmensaje.toPlainText()
        mensaje=mensaje.replace(" ","%20")
        mensaje=mensaje.replace("\n","%20")
        
        driver=webdriver.Edge('C:/Users/norma/PythonProjects/wasamasivo/msedgedriver.exe')

        file=open(direccion_tel, 'r')
        data=file.readlines()
        file.close()
        driver.get('https://web.whatsapp.com')
        time.sleep(20)
        for renglon in data:
                for numero in renglon.split(" "):
                    print(numero)
                    #driver.get('https://web.whatsapp.com/send?phone=+57{}&text={}'.format(numero,mensaje))
                    #driver.find_element_by_class_name("_1E0Oz").click()
                    #webbrowser.open(f'https://web.whatsapp.com/send?phone=57{numero}&text={mensaje}')
                    #driver.switch_to.new_window('tab')
                    #self.driver.close() cierra la pestaña actual
                    driver.
                    

                    time.sleep(10)
                    pyautogui.press("enter")
                    
          
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()
