import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Twitter_Scraper import *
from input_functions import *

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
        self.grid.addWidget(self.name, 0, 1, 1, 1)

        self.rate_me = QPushButton("Rate them!")
        self.grid.addWidget(self.rate_me, 0, 2, 1, 1)

        self.directions = QLabel("The rating scale is from 1 to 10, 10 being the best rating and 1 being the worst rating.")
        self.grid.addWidget(self.directions, 1, 0, 1, 6)
        self.directions.setObjectName("directions")

        self.rating = QLabel("Rating:")
        self.grid.addWidget(self.rating, 2, 0, 1, 1)

        self.rating_value = QLabel("Rating")
        self.grid.addWidget(self.rating_value, 2, 1, 1, 1)
        self.rating_value.setObjectName("rating_value")

        self.frequent_words = QLabel("Most frequently used words:")
        self.grid.addWidget(self.frequent_words, 3, 0, 1, 1)

        self.f_words = QLabel("Freq Word")
        self.grid.addWidget(self.f_words, 3, 1, 1, 1)

        self.positive_words = QLabel("Most frequently used positive words:")
        self.grid.addWidget(self.positive_words, 4, 0, 1, 1)

        self.pos_words = QLabel("p word")
        self.grid.addWidget(self.pos_words, 4, 1, 1, 1)

        self.negative_words = QLabel("Most frequently used negative words:")
        self.grid.addWidget(self.negative_words, 5, 0, 1, 1)

        self.neg_words = QLabel("neg word")
        self.grid.addWidget(self.neg_words, 5, 1, 1, 1)

        self.percentage_pos = QLabel("Percentage of positive words:")
        self.grid.addWidget(self.percentage_pos, 6, 0, 1, 1)

        self.per_pos = QLabel("percent")
        self.grid.addWidget(self.per_pos, 6, 1, 1, 1)

        self.percentage_neg = QLabel("Percentage of negative words:")
        self.grid.addWidget(self.percentage_neg, 7, 0, 1, 1)

        self.per_neg = QLabel("percent")
        self.grid.addWidget(self.per_neg, 7, 1, 1, 1)

        # Signals and Slot

        # Set Style
        self.set_style()

        # Draw
        self.show()

    def set_style(self):
        style_sheet = "main_style.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())

    def hit_button(self):
        twitter_words = twitter_scraper(self.name.text())
        self.f_words.setText(frequent_words()[0])


    # def rating

    # def most frequent words

    # def most frequent positive word

    # def most frequent negative word

    # def percentage positive words

    # def percentage negative words


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())