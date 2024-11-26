import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class NestedTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setRowCount(2)  # Set rows for the nested table
        self.setColumnCount(2)  # Set columns for the nested table

        # Fill the nested table with labels
        for nested_row in range(2):
            for nested_column in range(2):
                nested_item = QTableWidgetItem(f'Nested Item {nested_row + 1}, {nested_column + 1}')
                self.setItem(nested_row, nested_column, nested_item)

        # Set size policy to ensure it resizes with the parent
        self.setSizePolicy(QTableWidget.AdjustToContents, QTableWidget.AdjustToContents)


class MainTable(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('Main Table with Resizable Nested Tables Example')

        # Create the main table
        self.main_table = QTableWidget()
        self.main_table.setRowCount(3)
        self.main_table.setColumnCount(3)


        # Fill the main table with item labels and nested tables in specific cells
        for row in range(3):
            for column in range(3):
                item = QTableWidgetItem(f'Main Item {row + 1}, {column + 1}')
                self.main_table.setItem(row, column, item)

                # Add NestedTable widget in specific cells
                if row == 0 and column == 0:  # Adjust this condition for placement
                    nested_table = NestedTable()
                    self.main_table.setCellWidget(row, column, nested_table)

                if row == 1 and column == 1:  # Example for another nested table
                    nested_table = NestedTable()
                    self.main_table.setCellWidget(row, column, nested_table)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.main_table)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainTable()
    window.resize(600, 400)  # Resize the window
    window.show()
    sys.exit(app.exec_())


        def resizeEvent(self, event):
        # Resize the nested table to fit within its parent cell
        super().resizeEvent(event)
        parent = self.parent()
        if parent and isinstance(parent, QTableWidget):
            self.setFixedSize(parent.sizeHint())
            self.resize(parent.sizeHint())
        # Optionally, you can standardize the size of the nested table
        # self.setMaximumSize(parent.width(), parent.height())