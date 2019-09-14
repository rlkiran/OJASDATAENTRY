import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

import FireTest


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('sideWindow.ui', self)
        self.eTestName = self.findChild(QtWidgets.QLineEdit, 'eTestName')
        self.eParamName = self.findChild(QtWidgets.QLineEdit, 'eParamName')
        self.eUnitName = self.findChild(QtWidgets.QLineEdit, 'eUnitName')
        self.eRefName = self.findChild(QtWidgets.QLineEdit, 'eRefName')
        self.technologyName = self.findChild(QtWidgets.QLineEdit, 'technologyName')

        self.dTestName = self.findChild(QtWidgets.QLineEdit, 'dTestName')

        self.AddDataButton = self.findChild(QtWidgets.QPushButton, 'AddDataButton')
        self.DeleteDataButton = self.findChild(QtWidgets.QPushButton, 'DeleteDataButton')
        self.AddDataButton.clicked.connect(self.AddDataToCloud)
        self.DeleteDataButton.clicked.connect(self.DelDataFromCloud)

        self.AddTechButton = self.findChild(QtWidgets.QPushButton, 'addTechnology')
        self.DeleteTechButton = self.findChild(QtWidgets.QPushButton, 'deleteTechnology')
        self.AddTechButton.clicked.connect(self.AddTechToCloud)
        self.DeleteTechButton.clicked.connect(self.DelTechFromCloud)

        self.show()

    def AddDataToCloud(self):
        AddData = {}
        testName = self.eTestName.text().strip()
        paramName = self.eParamName.text().strip()
        unitName = self.eUnitName.text().strip()
        refName = self.eRefName.text().strip()
        AddData['TestName'] = testName
        AddData['Parameter'] = paramName
        AddData['Units'] = unitName
        AddData['RefRange'] = refName
        FireTest.addTestDataToCloud(**AddData.copy())
        AddData.clear()
        QMessageBox.about(self, "Done", "Data added Successfully")

    def DelDataFromCloud(self):
        testName = self.dTestName.text().strip()
        if testName != "":
            FireTest.delTestDataFromCloud(testName)
            QMessageBox.about(self, "Done", "Data Deleted Successfully")
        else:
            QMessageBox.about(self, "Failed", "Task Failed")

    def AddTechToCloud(self):
        techname = self.technologyName.text().strip()
        if techname != "":
            FireTest.addTechName(techname)
            QMessageBox.about(self, "Done", "Data Added Successfully")
        else:
            QMessageBox.about(self, "Failed", "Task Failed")

    def DelTechFromCloud(self):
        techname = self.technologyName.text().strip()
        if techname != "":
            FireTest.deltechnologyName(techname)
            QMessageBox.about(self, "Done", "Data Deleted Successfully")
        else:
            QMessageBox.about(self, "Failed", "Task Failed")

#    def quitApp(self):
#        sys.exit(0)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
