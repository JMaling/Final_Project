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
        self.setGeometry(0, 0, 800, 600)

        # Widgets

        self.title = QLabel("Twitter Scraper Rater")
        self.grid.addWidget(self.title, 0, 1, 1, 1)

        self.input_name = QLabel("Enter a name:")
        self.grid.addWidget(self.input_name, 1, 0, 1, 1)
        self.input_name.setObjectName("input_name")

        self.name = QLineEdit(self)
        self.grid.addWidget(self.name, 1, 1, 1, 1)
        self.name.setObjectName("name")

        self.rate_me = QPushButton("Rate them!")
        self.grid.addWidget(self.rate_me, 1, 2, 1, 1)
        self.rate_me.clicked.connect(lambda: self.hit_button())

        self.directions = QLabel("The rating scale is from 1 to 10, 10 being the best rating and 1 being the worst rating.")
        self.grid.addWidget(self.directions, 2, 0, 1, 6)
        self.directions.setObjectName("directions")

        self.rating = QLabel("Rating:")
        self.grid.addWidget(self.rating, 3, 0, 1, 1)
        self.rating.setObjectName("category")

        self.rating_value = QLabel("Rating")
        self.grid.addWidget(self.rating_value, 3, 1, 1, 1)
        self.rating_value.setObjectName("rating_value")

        self.frequent_words = QLabel("Most frequently used words:")
        self.grid.addWidget(self.frequent_words, 4, 0, 1, 1)
        self.frequent_words.setObjectName("category")

        self.f_words = QLabel("")
        self.grid.addWidget(self.f_words, 4, 1, 1, 1)

        self.positive_words = QLabel("Most frequently used positive words:")
        self.grid.addWidget(self.positive_words, 5, 0, 1, 1)
        self.positive_words.setObjectName("category")

        self.pos_words = QLabel("")
        self.grid.addWidget(self.pos_words, 5, 1, 1, 1)

        self.negative_words = QLabel("Most frequently used negative words:")
        self.grid.addWidget(self.negative_words, 6, 0, 1, 1)
        self.negative_words.setObjectName("category")

        self.neg_words = QLabel("")
        self.grid.addWidget(self.neg_words, 6, 1, 1, 1)

        self.percentage_pos = QLabel("Percentage of positive words:")
        self.grid.addWidget(self.percentage_pos, 7, 0, 1, 1)
        self.percentage_pos.setObjectName("category")

        self.per_pos = QLabel("percent")
        self.grid.addWidget(self.per_pos, 7, 1, 1, 1)

        self.percentage_neg = QLabel("Percentage of negative words:")
        self.grid.addWidget(self.percentage_neg, 8, 0, 1, 1)
        self.percentage_neg.setObjectName("category")

        self.per_neg = QLabel("percent")
        self.grid.addWidget(self.per_neg, 8, 1, 1, 1)

        # Set Style
        self.set_style()

        # Draw
        self.show()

    def set_style(self):
        style_sheet = "main_style.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())

    def hit_button(self):
        if self.name.text() == "":
            return
        twitter_words = twitter_scraper(self.name.text())
        print(self.name.text())
        words = frequent_words(twitter_words)
        display = ""
        for word in words:
            display += word + ", "
        self.f_words.setText(display)

        good_word = frequent_words((get_good_list(positive_word_list, twitter_words)))
        display = ""
        for word in good_word:
            display += word + ", "
        self.pos_words.setText(display)

        bad_word = frequent_words((get_good_list(negative_word_list, twitter_words)))
        display = ""
        for word in bad_word:
            display += word + ", "
        self.neg_words.setText(display)


    # def rating

    # def most frequent words

    # def most frequent positive word

    # def most frequent negative word

    # def percentage positive words

    # def percentage negative words


if __name__ == "__main__":
    positive_word_list = []
    negative_word_list = []

    with open("negative-words.txt") as f:
        for line in f:
            negative_word_list.append((line.strip()))

    with open("positive-words.txt") as f:
        for line in f:
            positive_word_list.append((line.strip()))
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())