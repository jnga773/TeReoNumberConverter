import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from converter_function import TeReoNumberConverter

# Define class for main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Title of the window
        self.setWindowTitle("Te Reo Number Converter")
        # Set Icon size
        self.setIconSize(QSize(16,16))
        self.setWindowIcon(QIcon("animal-dog.png"))

        # Menu bar
        MainMenuBar = self.menuBar()
        AboutMenu = MainMenuBar.addMenu('&About')

        # About action
        AboutAction = QAction("&About the App (v1.2)", self)
        AboutAction.setStatusTip("Information about the App")
        AboutAction.triggered.connect(self.AboutWindowPopup)
        # Add action to menu item
        AboutMenu.addAction(AboutAction)

        ##########################
        #    WINDOW WIDGETS      #
        ##########################
        # Text to say what to input
        self.InputLabel = QLabel(self)
        self.InputLabel.setText('Enter whole number (less than 10 billion):')
        # LineEdit number input
        self.InputNumber = QLineEdit(self)
        self.InputNumber.setMaxLength(15)
        self.InputNumber.setPlaceholderText("Number:")
        # Only allow integers
        self.onlyInt = QIntValidator()
        self.InputNumber.setValidator(self.onlyInt)
        # If Enter is pressed, calculate number
        self.InputNumber.returnPressed.connect(self.ConvertNumber)
        # Move input box
        # self.InputNumber.move(80, 20)
        # self.InputNumber.resize(200, 32)
        # self.InputLabel.move(20, 20)
        # Input okay button
        InputButton = QPushButton('Aue', self)
        # If button is clicked, calculate number
        InputButton.clicked.connect(self.ConvertNumber)
        # Move input button
        # InputButton.resize(200,32)
        # InputButton.move(80, 60)

        # Output Print
        self.OutputLabel = QLabel(self)
        self.OutputLabel.setText("In Te Reo Māori, 0 is: kore!")

        #############
        #   LAYOUT  #
        #############
        # Main layout
        MainLayout = QVBoxLayout()
        MainLayout.addWidget(self.InputLabel)
        MainLayout.addWidget(self.InputNumber)
        MainLayout.addWidget(InputButton)
        MainLayout.addWidget(self.OutputLabel)

        # Set MainLayout as main widget
        widget = QWidget()
        widget.setLayout(MainLayout)
        self.setCentralWidget(widget)

    def ConvertNumber(self):
        """
        When triggered, converts input string into Te Reo number and updates
        OutputLabel.
        """
        # print('Input Number: {}'.format(input_str))
        # Update input_str
        input_str = self.InputNumber.text()
        # Convert number to Te Reo Māori
        output_str = TeReoNumberConverter(input_str)
        self.OutputLabel.setText("In Te Reo Māori, {} is: {}!".format(input_str, output_str))

    def AboutWindowPopup(self):
        """
        Opens a popup window with information on the app and my email address
        """
        msg = QMessageBox()
        # Set icon as information
        msg.setIcon(QMessageBox.Information)
        # Set text to be selectable
        msg.setTextInteractionFlags(Qt.TextSelectableByMouse)
        msg.setText("This app was devolped by Jacob Ngaha (j.ngaha@auckland.ac.nz). The source code is available at https://www.github.com/jnga773/TeReoNumberConverter")
        # msg.setInformativeText("The source code is available at https://www.github.com/jnga773/TeReoNumberConverter")
        msg.setDetailedText("v1.0 - Initial Release \n" +\
                            "v1.1 - Changed 'kotahi tekau' to 'tekau' \n" +\
                            "v1.2 - Increased range to 9,999,999,999 (just under 10 billion) \n" +\
                            "v1.2.1 - Fixed Typo")
        msg.setWindowTitle("About Te Reo Number Converter (v1.2)")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(500, 100)
    window.show()
    app.exec_()
