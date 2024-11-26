import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QHeaderView, QCheckBox, QLabel, QPushButton
import functions

class Checkboxes(QWidget):
    def __init__(self):
        super().__init__()

        # Creating checkboxes for logs
        self.Application = QCheckBox('Application Logs')
        self.CoreDumps = QCheckBox('Core Dumps')
        self.GeniewareLogs = QCheckBox('Genieware Logs')
        self.OSLogs = QCheckBox('OS Logs')
        self.SystemLogs = QCheckBox('System Logs')

        self.boxlayout = QVBoxLayout()
        self.boxlayout.addWidget(self.Application)
        self.boxlayout.addWidget(self.CoreDumps)
        self.boxlayout.addWidget(self.GeniewareLogs)
        self.boxlayout.addWidget(self.OSLogs)
        self.boxlayout.addWidget(self.SystemLogs)
        self.setLayout(self.boxlayout)  # Set the initial layout

    def DateListCB(self, node):
        # Clear existing checkboxes from boxlayout
        for checkbox in self.boxlayout.findChildren(QCheckBox):
            self.boxlayout.removeWidget(checkbox)
            checkbox.deleteLater()  # Remove from memory
        
        # Creating checkboxes for dates
        dateslist = functions.ListDates(node)
        self.cbs = []  # Stand for checkboxes

        for date in dateslist:
            checkbox = QCheckBox(date)
            self.cbs.append(checkbox)
            self.boxlayout.addWidget(checkbox)  # Add checkbox to the existing layout


class Table(QWidget):
    def __init__(self):
        super().__init__()

        # Setting window title
        self.setWindowTitle('Log Management')

        # Setting Row Names
        nodes = functions.ListNodes()

        # Create a QTableWidget
        self.LogCopy = QTableWidget()
        self.LogCopy.setColumnCount(3)
        self.LogCopy.setRowCount(len(nodes))

        self.LogCopy.setVerticalHeaderLabels(nodes)

        # Setting Column Names
        self.LogCopy.setHorizontalHeaderLabels(['Nodes', 'Dates', 'Types'])

        # Creating Log Types Checkboxes
        for row in range(len(nodes)):
            column = 2  # Types column
            types_table = Checkboxes()  # Create a new instance for checkboxes
            self.LogCopy.setCellWidget(row, column, types_table)

            # Add dates checkboxes dynamically
            column = 1  # Dates column
            datesboxes=types_table.DateListCB(nodes[row])  # Populate the dates for the specific node
            self.LogCopy.setCellWidget(row, column, datesboxes)

        # Making rows large enough to fit everything in
        for i in range(len(nodes)):
            self.LogCopy.setRowHeight(i, 200)
        self.LogCopy.setColumnWidth(2, 270)

        download = QPushButton('Download', self)

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