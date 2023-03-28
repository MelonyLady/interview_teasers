from unittest import TestCase, main


def is_anagram(first_word, second_word):
    return sorted(first_word.casefold()) == sorted(second_word.casefold())


# manual testing
print(is_anagram("leap", "pale"))  # Should output True
print(is_anagram("frog", "fog"))  # Should output False
print(is_anagram("Iamlordvoldemort", "TomMarvoloRiddle"))  # Should output True


class TestAnagrams(TestCase):

    def test_is_anagram_true(self):
        self.assertTrue(is_anagram("dog", "god"))
        self.assertTrue(is_anagram("angel", "glean"))

    def test_is_anagram_false(self):
        self.assertFalse(is_anagram("turtle", "fish"))
        self.assertFalse(is_anagram("bog", "dog"))

