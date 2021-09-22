import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, uic
import mysql.connector
import function as f
import cv2


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('home.ui', self) # Load the .ui file
        self.show() 
        #If button is clicked
        
        self.btnFaceRecog.clicked.connect(self.startCamera)
        self.btnGenerate.clicked.connect(self.gotoGenerate)
        
    def startCamera(self):
        start = f.face_reco()
        start.startRecog()    

    def gotoGenerate(self):
        generate = GenerateDataset()
        widget.addWidget(generate)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class GenerateDataset(QDialog):
    def __init__(self):
        super(GenerateDataset, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('generate.ui', self) # Load the .ui file
        self.btnReturn.clicked.connect(self.returnMain)
        self.btnRegister.clicked.connect(self.registerUser)
        self.btnTrain.clicked.connect(self.trainClassifier)

    def registerUser(self):
        name = self.fieldname.text()
        birthdate = self.birthdate.text()
        gender =  str(self.gender.currentText())
        course =  str(self.course.currentText())
        userType = str(self.type.currentText())

        if len(name)==0:
            self.errorlabel.setText("Error: Please fill-up all the required field")

        else:
            register = f.face_reco()
            register.generateDataset(name,course,birthdate,gender,userType)






    def trainClassifier(self):
        train = f.face_reco()
        train.startTraining()

    
    def returnMain(self):
        returnUi = Ui()
        widget.addWidget(returnUi)
        widget.setCurrentIndex(widget.currentIndex() + 1)
   
# def loginFucntion(self): 
    #     user = self.username.text()
    #     passw = self.password.text()

    #     if len(user)==0 or len(passw)==0:
    #         self.error.setText("Please input all fields.")
        
        
        # # Show the GUI
        # self.tableWidget.setColumnWidth(0,250)
        # self.tableWidget.setColumnWidth(1,100)
        # self.tableWidget.setColumnWidth(2,200)
    # def loaddata(self):
    #     mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="",
    #     database="face_attendancesystem" )

    #     cursor = mydb.cursor()
    #     cursor.execute("SELECT * from known_faces")
    #     myresult = cursor.fetchall()
    #     tablerow=0
    #     self.tableWidget.setRowCount(40)


    #     for row in myresult:
    #         self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
    #         self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
    #         self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
    #         tablerow+=1




# main
app = QApplication(sys.argv)
welcome = Ui()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")