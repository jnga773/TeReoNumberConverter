import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def TeReoNumberConverter(input_number_str):
    """
    Reads an input integer from the console (less than 10 million) and converts
    the digits into Te Reo Māori.
    """
    # Read numerical input from console
    input_number_int = int(input_number_str)
    input_number_str = str(input_number_int)
    input_number_fill = input_number_str.zfill(7)
    # List of tens
    tens_str = [" miriona", " rau mano", " tekau mano", " mano",
                " rau", " tekau", "mā"]
    # List of numbers from 0-9
    digits_str = ["kore", "kotahi", "rua", "toru", "whā", "rima", "ono",
                  "whitu", "waru", "iwa", "tekau"]

    # If input is less than 10, just print the number. Otherwise, go through
    # the long method
    if input_number_int <= 10:
        # If the ones digit is 1, print "tahi" instead of "kotahi"
        if input_number_int == 1:
            output = "tahi"
        else:
            output = str(digits_str[input_number_int])
    else:
        # Turn input string into list
        input_number_str_list = list(input_number_fill)
        # Create list where each element is int(input_number_str_list[i])
        nums_list = []
        # Create list where each element is the word for int(input_number_str_list[i])
        str_list = []
        for i in input_number_str_list:
            nums_list.append(int(i))
            if int(i) != 0:
                str_list.append(digits_str[int(i)])
            else:
                str_list.append("")
        # Create a list for the placeholders to be printed
        out_tens = []
        # Cycle through elements in nums_list. If element is 0, append "" to out_tens,
        # otherwise, append the tens placeholder
        for element, number in enumerate(nums_list):
            if number == 0:
                out_tens.append("")
            else:
                out_tens.append(tens_str[element])
        # Cycle through str_list to see if commas are needed
        commas = []
        for element, number in enumerate(nums_list[:-1]):
            if number == 0:
                # No number so comma is not needed
                commas.append("")
            else:
                # Cycle through the rest of the list (excluding the ones column)
                # and check if there is any non-zero between current number
                # and the ones column
                check = False
                for i in nums_list[element+1:-1]:
                    if i == 0:
                        # The element is 0 so set check = True. Comma not needed
                        check = True
                    else:
                        check = False
                        break
                if check is True:
                    commas.append("")
                else:
                    commas.append(", ")
        del check
        # Append "" for tens (no comma needed)
        # commas.append("")
        # If the ones column is 0, mā not needed, otherwise append mā
        if nums_list[-1] == 0:
            commas.append("")
        else:
            commas.append(" mā ")
        # Split output_string into different components for each tens
        # Millions
        if nums_list[0] != 0:
            output = "{}{}{}".format(str_list[0], tens_str[0], commas[0])
        else:
            output = ""
        # Hundred thousands
        if nums_list[1] != 0:
            output += "{}{}{}".format(str_list[1], tens_str[1], commas[1])
        else:
            output += ""
        # Ten thousands
        if nums_list[2] != 0:
            output += "{}{}{}".format(str_list[2], tens_str[2], commas[2])
        else:
            output += ""
        # Thousands
        if nums_list[3] != 0:
            output += "{}{}{}".format(str_list[3], tens_str[3], commas[3])
        else:
            output += ""
        # Hundreds
        if nums_list[4] != 0:
            output += "{}{}{}".format(str_list[4], tens_str[4], commas[4])
        else:
            output += ""
        # Tens
        if nums_list[5] != 0:
            output += "{}{}".format(str_list[5], tens_str[5])
        else:
            output += ""
        # Ones
        if nums_list[6] != 0:
            # If the ones digit is 1, print "tahi" instead of "kotahi"
            if nums_list[6] == 1:
                output += "{}tahi".format(commas[6])
            else:
                output += "{}{}".format(commas[6], str_list[6])
    # Return output
    return output

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
        AboutAction = QAction("&About the App (v1.0)", self)
        AboutAction.setStatusTip("Information about the App")
        AboutAction.triggered.connect(self.AboutWindowPopup)
        # Add action to menu item
        AboutMenu.addAction(AboutAction)

        ##########################
        #    WINDOW WIDGETS      #
        ##########################
        # Text to say what to input
        self.InputLabel = QLabel(self)
        self.InputLabel.setText('Enter whole number (less than 10 Million):')
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
        InputButton = QPushButton('OK', self)
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
        msg.setWindowTitle("About Te Reo Number Converter")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(500, 100)
    window.show()
    app.exec_()
