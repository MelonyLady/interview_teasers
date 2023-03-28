def is_anagram(first_word, second_word):
    return sorted(first_word.casefold()) == sorted(second_word.casefold())

