import re
import collections
import pymorphy2


def filter_words_in_title(raw_title, min_word_len=3, only_letters=True):
    ban_words = ['для', 'без', 'нам', 'как', 'что',
                 'или', 'все', 'под', 'над', 'кто',
                 'часть', 'при', 'про', 'который']
    words_in_string = raw_title.lower().strip()
    if only_letters:
        lower_letters_regex = re.compile('[^a-zа-я]')
        words_in_string = lower_letters_regex.sub(
            ' ',
            words_in_string
        )
    current_words = words_in_string.split()
    return [w.strip() for w in current_words if w not in ban_words and len(w) >= min_word_len]


def make_word_of_normal_form(word):
    morph = pymorphy2.MorphAnalyzer()
    return morph.parse(word)[0].normal_form


def calculate_normal_form_word_frequency(words_list):
    normal_forms = []
    for word in words_list:
        normal_forms.append(make_word_of_normal_form(word))
    return collections.Counter(normal_forms).most_common()
