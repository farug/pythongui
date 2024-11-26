import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QHeaderView

class TableWithSubcolumns(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('Table with Subcolumns Example')

        # Create a QTableWidget
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(6)  # Total of 6 columns (2 subcolumns in the first column)

        # Set the headers
        self.table_widget.setHorizontalHeaderLabels(['Main Col 1', 'Sub Col 1', 'Sub Col 2', 'Column 2', 'Column 3', 'Column 4'])
        self.table_widget.setVerticalHeaderLabels(['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])

        # Merge headers (simulating subcolumns) by adding an additional header row
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Main Col 1"))
        self.table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Sub Col 1"))
        self.table_widget.setHorizontalHeaderItem(2, QTableWidgetItem("Sub Col 2"))
        
        # Fill the table with checkboxes
        for row in range(5):
            # Adding checkboxes in subcolumns
            for column in range(6):  # 6 total columns
                item = QTableWidgetItem()
                item.setCheckState(0)  # Initially unchecked
                self.table_widget.setItem(row, column, item)

        # Resize columns to fit content
        for i in range(6):
            self.table_widget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWithSubcolumns()
    window.resize(600, 300)  # Resize the window
    window.show()
    sys.exit(app.exec_())