positive_word_list = []
negative_word_list = []

with open("negative-words.txt") as f:
    for line in f:
        negative_word_list.append((line.strip()))

with open("positive-words.txt") as f:
    for line in f:
        positive_word_list.append((line.strip()))


