def word_process(positive_word_list, word_list6):
    good = 0
    good_words = []

    for word in word_list6:
        if word in positive_word_list:
            good += 1
            good_words.append(word)

    return good_words

    bad = 0
    bad_words = []

    for word in word_list6:
        if word in negative_word_list:
            bad += 1
            bad_words.append(word)

    return bad_words

    positive_percentage = ((good)/(good + bad)) * 100

    negative_percentage = 100 - positive_percentage

    return negative_percentage, positive_percentage


def frequent_words(word_list6):

    repeats = [[word, word_list6.count(word)] for word in word_list6]
    print(repeats.sort(key=lambda x: x[1]))
    repeats = dict(repeats)
    repeats = list(repeats)
    repeats = repeats[-3:]
    print(repeats)

def frequent_positive(good_words):
    good_repeats = [[word, good_words.count(word)] for word in good_words]
    print(good_repeats.sort(key=lambda x: x[1]))
    good_repeats = dict(good_repeats)
    good_repeats = list(good_repeats)
    good_repeats = good_repeats[-3:]
    print(good_repeats)

def frequent_negative(bad_words):
    bad_repeats = [[word, bad_words.count(word)] for word in bad_words]
    print(bad_repeats.sort(key=lambda x: x[1]))
    bad_repeats = dict(bad_repeats)
    bad_repeats = list(bad_repeats)
    bad_repeats = bad_repeats[-3:]
    print(bad_repeats)