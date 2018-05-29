def get_good_list(sentiment_list, word_list6):
    '''
    :param positive_word_list: uci list of good words or bad words
    :param word_list6: twitter feed list of words
    :return: list of good or bad words found in twitter words
    '''
    total = 0
    words = []

    for word in word_list6:
        if word in sentiment_list:
            total += 1
            words.append(word)

    return words, total





def percentages(good_words, bad_words):
    good = len(good_words)
    bad = len(bad_words)
    positive_percentage = ((good)/(good + bad)) * 100

    negative_percentage = 100 - positive_percentage

    return negative_percentage, positive_percentage

def frequent_words(my_list):

    repeats = [[word, my_list.count(word)] for word in my_list]
    print(repeats)
    repeats.sort(key=lambda x: x[1])
    print(repeats)
    repeats = dict(repeats)
    print(repeats)
    new_repeats = []
    for key, value in repeats.items():
        new_repeats.append([key, value])
    new_repeats = [x[0] for x in new_repeats]
    new_repeats = new_repeats[-3:]
    print(new_repeats)
    return new_repeats

if __name__ == "__main__":
    frequent_words(["j", "j", "j", "d", "d", "m", "m", "m", "z", "z", "z"])

