from unittest import TestCase, main


def is_anagram(first_word, second_word):
    return sorted(first_word.casefold()) == sorted(second_word.casefold())


# manual testing
print(is_anagram("leap", "pale"))  # Should output True
print(is_anagram("frog", "fog"))  # Should output False
print(is_anagram("Iamlordvoldemort", "TomMarvoloRiddle"))  # Should output True
