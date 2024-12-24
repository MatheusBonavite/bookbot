import unittest
import sys
# Importing main functionality
sys.path.append("../")
import main 

class Test(unittest.TestCase):

    def test_word_counter(self):
        # Test simple scenario
        words = {}
        main.word_counter("Hello World", words)
        self.assertDictEqual(words, {"Hello" : 1, "World" : 1})
        # Test simple scenario with punctuation
        words = {}
        main.word_counter("Hello, World!", words)
        self.assertDictEqual(words, {"Hello" : 1, "World" : 1})
        # Test scenario with word containing '
        words = {}
        main.word_counter("Frank's wife is here! His wife is not nice!", words)
        self.assertDictEqual(words, {"Frank's": 1, "wife" : 2, "is" : 2, "here" : 1, "His" : 1, "not" : 1, "nice" : 1})


if __name__ == "__main__":
    unittest.main()
