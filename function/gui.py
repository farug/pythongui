import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QHeaderView, QCheckBox, QLabel, QPushButton

class Checkboxes(QWidget):
    def __init__(self):
        super().__init__()

        #Creating checkboxes
        self.Application = QCheckBox('Application Logs')
        self.CoreDumps = QCheckBox('Core Dumps')
        self.GeniewareLogs = QCheckBox('Genieware Logs')
        self.OSLogs = QCheckBox('OS Logs')
        self.SystemLogs = QCheckBox('System Logs')

        boxlayout = QVBoxLayout()
        boxlayout.addWidget(self.Application)
        boxlayout.addWidget(self.CoreDumps)
        boxlayout.addWidget(self.GeniewareLogs)
        boxlayout.addWidget(self.OSLogs)
        boxlayout.addWidget(self.SystemLogs)
        self.setLayout(boxlayout)

class Table(QWidget):
    def __init__(self):
        super().__init__()

        #Setting window title
        self.setWindowTitle('Log Management')

        #Create a QTableWidget
        self.LogCopy = QTableWidget()
        self.LogCopy.setColumnCount(3)
        self.LogCopy.setRowCount(3) # This part will be dynamic # use len function to make it dynamic

        #Setting Row Names
        self.LogCopy.setVerticalHeaderLabels(["a","b","c"]) # Later this will brought by a function

        # Setting Column Names
        self.LogCopy.setHorizontalHeaderLabels(['Nodes','Dates','Types']) # Inside Types there willbe subrows for os,gw ...

        #Making subrows in Type column
        for row  in range(3):
            column=2
            types_table = Checkboxes()
            self.LogCopy.setCellWidget(row,column,types_table)
        #Making rows large enough to  fit everything in
        for i in range(3):
            self.LogCopy.setRowHeight(i,200)
        self.LogCopy.setColumnWidth(2,270)

        download = QPushButton('Download',self)
        #download.clicked.connect("give the class and function here")
        
         

        # Set layout
        layout = QVBoxLayout()    
        layout.addWidget(self.LogCopy)
        layout.addWidget(download)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Table()
    window.resize(600, 300)  # Resize the window
    window.show()
    sys.exit(app.exec_())