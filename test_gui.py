import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QHeaderView, QCheckBox, QLabel
import functions

class  subTableLogs(QWidget):
    def __init__(self):
        super().__init__()
        #Creating subtable
        self.nested = QTableWidget()
        self.nested.setColumnCount(1)
        self.nested.setRowCount(5)

        #Setting row names
        self.nested.setVerticalHeaderLabels(["Application Logs","Core Dumps", "Genieware Logs","OS Logs","System Logs"])
        
        #Setting column name
        self.nested.setHorizontalHeaderLabels(["Check Box"])

        #Creating checkboxes
        self.Application = QCheckBox('Application Logs')
        self.CoreDumps = QCheckBox('Core Dumps')
        self.GeniewareLogs = QCheckBox('Genieware Logs')
        self.OSLogs = QCheckBox('OS Logs')
        self.SystemLogs = QCheckBox('System Logs')
        #
        layout = QVBoxLayout()
        #self.checkbox.stateChanged.connect(self.show_selection)
        layout.addWidget(self.Application)
        layout.addWidget(self.CoreDumps)
        layout.addWidget(self.GeniewareLogs)
        layout.addWidget(self.OSLogs)
        layout.addWidget(self.SystemLogs)

        #Setting table size
        self.nested.setFixedHeight(250)
        #self.nested.setFixedWidth(100)
        # Set layout
        
        layout.addWidget(self.nested)
        self.setLayout(layout)

        #self.setSizePolicy(QTableWidget.AdjustToContents, QTableWidget.AdjustToContents)
        #self.nested.setSizeAdjustPolicy(
        #QWidget.QAbstractScrollArea.AdjustToContents)


class Checkboxes(QWidget):
    def __init__(self):
        super().__init__()

        #Creating checkboxes
        self.Application = QCheckBox('Application Logs')
        self.CoreDumps = QCheckBox('Core Dumps')
        self.GeniewareLogs = QCheckBox('Genieware Logs')
        self.OSLogs = QCheckBox('OS Logs')
        self.SystemLogs = QCheckBox('System Logs')

        layout = QVBoxLayout()
        layout.addWidget(self.Application)
        layout.addWidget(self.CoreDumps)
        layout.addWidget(self.GeniewareLogs)
        layout.addWidget(self.OSLogs)
        layout.addWidget(self.SystemLogs)
        self.setLayout(layout)

class Table(QWidget):
    def __init__(self):
        super().__init__()

        #Setting window title
        self.setWindowTitle('Log Management')

        #Taking Nodes list
        nodes=functions.ListNodes()

        #Create a QTableWidget
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(len(nodes)) # This part will be dynamic # use len function to make it dynamic


        
        #Setting Row Names
        for i in range(len(nodes)):
            print(nodes)
            #self.table_widget.setVerticalHeaderItem(i,"a") # Later this will brought by a function

        # Setting Column Names
        self.table_widget.setHorizontalHeaderLabels(['Nodes','Dates','Types']) # Inside Types there willbe subrows for os,gw ...

        #Making subrows in Type column
        for row  in range(3):
            column=2
            
            types_table = Checkboxes()
            self.table_widget.setCellWidget(row,column,types_table)
        #Making rows large enough to  fit everything in
        for i in range(3):
            self.table_widget.setRowHeight(i,200)
        self.table_widget.setColumnWidth(2,270)

         

        # Set layout
        layout = QVBoxLayout()
        #layout.addWidget(self.Application)
        #layout.addWidget(self.CoreDumps)
        #layout.addWidget(self.GeniewareLogs)
        #layout.addWidget(self.OSLogs)
        #layout.addWidget(self.SystemLogs)
        #layout.addWidget(self.table_widget)
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Table()
    window.resize(600, 300)  # Resize the window
    window.show()
    sys.exit(app.exec_())


    """ 
    # Set the headers using setHorizontalHeaderItem
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Main Header 1"))
        self.table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Header 2"))
        self.table_widget.setHorizontalHeaderItem(2, QTableWidgetItem("Header 3"))
        self.table_widget.setHorizontalHeaderItem(3, QTableWidgetItem("Header 4"))
        self.table_widget.setHorizontalHeaderItem(4, QTableWidgetItem("Header 5"))

        # Setting vertical headers (optional)
        self.table_widget.setVerticalHeaderLabels(['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])

        # Fill the table with example data
        for row in range(5):
            for column in range(5):
                item = QTableWidgetItem(f'Item {row + 1}, {column + 1}')
                self.table_widget.setItem(row, column, item)
    
    """

    """

    # Fill the table with checkboxes
        for row in range(5):
            for column in range(5):
                item = QTableWidgetItem()
                item.setCheckState(0)  # 0 means unchecked, 2 means checked
                self.table_widget.setItem(row, column, item)
"""