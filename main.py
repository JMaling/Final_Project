import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(0, 0, 400, 600)

        # Widgets
        self.input_name = QLabel("Enter a name:")
        self.grid.addWidget(self.input_name, 0, 0, 1, 2)

        self.name = QLineEdit(self)
        self.grid.addWidget(self.name, 0, 1, 1, 3)

        self.rules = QLabel("The rating scale is from 1 to 10, 10 being the best rating and 1 being the worst rating.")
        self.grid.addWidget(self.rules, 1, 0, 1, 6)

        self.rating = QLabel("Rating:")
        self.grid.addWidget(self.rating, 2, 0, 1, 1)

        self.rating_value = QLineEdit(self)
        self.grid.addWidget(self.rating_value, 2, 1, 1, 1)

        self.frequent_words = QLabel("Most frequently used words:")
        self.grid.addWidget(self.frequent_words, 3, 0, 1, 1)

        self.f_words = QLineEdit(self)
        self.grid.addWidget(self.f_words, 3, 1, 1, 1)

        self.positive_words = QLabel("Most frequently used positive words:")
        self.grid.addWidget(self.positive_words, 4, 0, 1, 1)

        self.pos_words = QLineEdit(self)
        self.grid.addWidget(self.pos_words, 4, 1, 1, 1)

        self.negative_words = QLabel("Most frequently used negative words:")
        self.grid.addWidget(self.negative_words, 5, 0, 1, 1)

        self.neg_words = QLineEdit(self)
        self.grid.addWidget(self.neg_words, 5, 1, 1, 1)

        self.percentage_pos = QLabel("Percentage of positive words:")
        self.grid.addWidget(self.percentage_pos, 6, 0, 1, 1)

        self.per_pos = QLineEdit(self)
        self.grid.addWidget(self.per_pos, 6, 1, 1, 1)

        self.percentage_neg = QLabel("Percentage of negative words:")
        self.grid.addWidget(self.percentage_neg, 7, 0, 1, 1)

        self.per_neg = QLineEdit(self)
        self.grid.addWidget(self.per_neg, 7, 1, 1, 1)

        # Signals and Slot

        # Set Style

        # Draw
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())