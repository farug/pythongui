import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView

class TableWithCheckboxes(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('5x5 Table with Checkboxes Example')

        # Create a QTableWidget with 5 rows and 5 columns
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(5)

        # Set the headers (optional)
        self.table_widget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5'])
        self.table_widget.setVerticalHeaderLabels(['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])

        # Fill the table with checkboxes
        for row in range(5):
            for column in range(5):
                item = QTableWidgetItem()
                item.setCheckState(0)  # 0 means unchecked, 2 means checked
                self.table_widget.setItem(row, column, item)

        # Resize columns to fit content
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWithCheckboxes()
    window.resize(400, 300)  # Resize the window
    window.show()
    sys.exit(app.exec_())