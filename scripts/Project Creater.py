import os
from extras import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    """Init for the Main Window and all static Widgets"""
    def __init__(self):
        super().__init__()

        """Clickstate for later Config checking"""
        self.clickState = 0

        """Main WIndow Widget & Layout Setup"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Project Creater by FzudemAA")
        MainWindow.resize(650, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(50, -1, 50, -1)
        self.gridLayout.setObjectName("gridLayout")

        """Font for fieldLabel"""
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        """Project Name Label and Textbox for User Input """
        self.fieldLabel = QtWidgets.QLabel(self.frame)
        self.fieldLabel.setFont(font)
        self.fieldLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fieldLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fieldLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fieldLabel.setObjectName("fieldLabel")
        self.fieldLabel.setText("Project Name")
        self.gridLayout.addWidget(self.fieldLabel, 0, 0, 1, 1)

        self.mName = QtWidgets.QLineEdit(self.frame)
        self.mName.setObjectName("mName")
        self.gridLayout.addWidget(self.mName, 0, 1, 1, 3)

        """Pushbutton for Folder selection, Textbox for Folder output"""
        self.button = QtWidgets.QPushButton(self.frame)
        self.button.setObjectName("button")
        self.button.setText("Choose a Folder")
        self.button.clicked.connect(self.pick_folder)
        self.gridLayout.addWidget(self.button, 1, 0, 1, 1)

        self.userInput = QtWidgets.QLineEdit(self.frame)
        self.userInput.setObjectName("userInput")
        self.gridLayout.addWidget(self.userInput, 1, 1, 1, 3)

        """3 Buttons for the Folder Structures, all Linked to there Config Function"""
        self.choiceBTN3 = QtWidgets.QPushButton(self.frame)
        self.choiceBTN3.setObjectName("choiceBTN3")
        self.choiceBTN3.setText("Custom")
        self.choiceBTN3.clicked.connect(self.cConfig)
        self.gridLayout.addWidget(self.choiceBTN3, 2, 2, 1, 1)

        self.choiceBTN2 = QtWidgets.QPushButton(self.frame)
        self.choiceBTN2.setObjectName("choiceBTN2")
        self.choiceBTN2.setText("Houdini")
        self.choiceBTN2.clicked.connect(self.hConfig)
        self.gridLayout.addWidget(self.choiceBTN2, 2, 1, 1, 1)

        self.choiceBTN1 = QtWidgets.QPushButton(self.frame)
        self.choiceBTN1.setObjectName("choiceBTN1")
        self.choiceBTN1.setText("Maya")
        self.choiceBTN1.clicked.connect(self.mConfig)
        self.gridLayout.addWidget(self.choiceBTN1, 2, 0, 1, 1)

        """Font for outTitle Label"""
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        """Label & Textbox for Folder Config show off"""
        self.outTitle = QtWidgets.QLabel(self.frame)
        self.outTitle.setFont(font)
        self.outTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.outTitle.setObjectName("outTitle")
        self.outTitle.setText("Folder Structure")
        self.gridLayout.addWidget(self.outTitle, 3, 0, 1, 1)

        self.outBox = QtWidgets.QTextEdit(self.frame)
        self.outBox.setReadOnly(True)
        self.outBox.setObjectName("outBox")
        self.gridLayout.addWidget(self.outBox, 5, 0, 1, 3)

        """Frame for Execute Button Positioning (dont touch)"""
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(-1, 313, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")

        """Font for exeBtn"""
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)

        """Pushbutton for Application executing"""
        self.exeBtn = QtWidgets.QPushButton(self.frame_2)
        self.exeBtn.setFont(font)
        self.exeBtn.setObjectName("exeBtn")
        self.exeBtn.setText("Execute")
        self.exeBtn.clicked.connect(self.execute)
        self.gridLayout_3.addWidget(self.exeBtn, 0, 0, 1, 1)

        """Frame gets added to Layout (dont touch)"""
        self.gridLayout.addWidget(self.frame_2, 5, 3, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

    """This Function opens a File Dialog for choosing are Path, it writes the Path into userInput Textbox"""
    def pick_folder(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select Folder")
        self.userInput.setText(str(folder_path))

    """This Function is called when the Maya Config Button is clicked
    It writes a list with all Folder Names into the OutBox TextBox
    It has to repaint the Textbox else it will not show the Updated list
    The lists (Mprocess5/Hprocess5) are loaded from the "Extras" Module"""
    def mConfig(self):
        self.clickState = 1
        self.outBox.setReadOnly(True)
        self.outBox.setText(Mprocess5)
        self.outBox.repaint()

    """This Function does the same as the last one when the Houdini Button is pressed"""
    def hConfig(self):
        self.clickState = -1
        self.outBox.setReadOnly(True)
        self.outBox.setText(Hprocess5)
        self.outBox.repaint()

    def cConfig(self):
        self.clickState = -2
        self.outBox.setText("")
        self.outBox.setReadOnly(False)
        self.outBox.setPlaceholderText("Enter Folder line by line.\n"
                                       "Generate Subfolder with the TAB Key.\n"
                                       "\n"
                                       "e.g.\n"
                                       "Folder1 TAB SubFolder1 TAB SubFolder3\n"
                                       "Folder2\n"
                                       "Folder3 TAB SubFolder1")
        self.outBox.repaint()

    """This Function will evaluate some variables and create the Folders"""
    def execute(self):
        ProjectName = self.mName.text()
        lineTxt = self.userInput.text()
        print("line Len " + str(len(lineTxt)))

        if len(ProjectName) == 0:
            self.projectNameDialog = self.dialog1()
            return self.execute()
        else:
            pass

        if len(lineTxt) == 0:
            self.dialog2()
            return self.execute()
        else:
            pass

        root_path = str(lineTxt)
        print("root " + str(len(root_path)))

        if root_path[-1] == "/":
            pass
        else:
            root_path = root_path + "/"
            pass

        if self.clickState == 1:
            folders = detailedListM
        elif self.clickState == -1:
            folders = detailedListH
        elif self.clickState == -2:
            plain = self.outBox.toPlainText()
            plain_list = list(plain.splitlines())
            new_l = [i.replace('\t', '/') for i in plain_list]
            folders = new_l

        else:
            self.configDialog = self.dialog3()
            return self.execute()

        path_check = os.path.isdir(str(root_path + ProjectName))
        if path_check:
            self.dialog4()
            return self.execute()
        else:
            pass

        try:
            for folder in folders:
                os.makedirs(str(root_path + ProjectName + "/" + folder))
            self.sucess()

        except Exception as e:
            self.dialog5()

    def dialog1(self):
        self.projectNameDialog, result = QInputDialog.getText(MainWindow, "No Project Name", "Enter a Project Name",
                                                              QLineEdit.Normal)
        if len(self.projectNameDialog) == 0:
            return self.dialog1()
        else:
            print(self.projectNameDialog + " Dialog Text funzt")
            self.mName.setText(self.projectNameDialog)
            return self.projectNameDialog

    def dialog2(self):
        msgBox = QMessageBox()
        msgBox.information(MainWindow, "", "Please Select a Folder", QMessageBox.Open)

        dialog = QFileDialog()
        folder_path2 = dialog.getExistingDirectory(None, "Select Folder")
        self.userInput.setText(str(folder_path2))

    def dialog3(self):
        configs = ("Maya", "Houdini", "Custom")
        self.configDialog, result = QInputDialog.getItem(MainWindow, "No Config Selected",
                                                         "Select Config", configs, 0, False)

        if self.configDialog == "Maya":
            self.choiceBTN1.click()
        elif self.configDialog == "Houdini":
            self.choiceBTN2.click()
        else:
            self.choiceBTN3.click()

    def dialog4(self):
        msgBox2 = QMessageBox()
        msgBox2.warning(MainWindow, "", "The Path you chose already exists. Please chose another one.")
        return self.dialog2()

    def dialog5(self):
        msgBox3 = QMessageBox()
        msgBox3.warning(MainWindow, "", "Uff, something went wrong. We will stop now.")
        sys.exit()

    def sucess(self):
        msgbox4 = QMessageBox()
        msgbox4.information(MainWindow, "", "Sucess. Folders were created.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

