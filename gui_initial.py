import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QCheckBox


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

class TableExample(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('5x5 Table Example')

        # Create a QTableWidget with 5 rows and 5 columns
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(5)

        # Set the headers (optional)
        self.table_widget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5'])
        self.table_widget.setVerticalHeaderLabels(['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])

        # Fill the table with sample data
        box = Checkboxes()
        for row in range(5):
            column = 2
            self.table_widget.setCellWidget(row, column, box)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableExample()
    window.resize(400, 300)  # Resize the window
    window.show()
    sys.exit(app.exec_())


    