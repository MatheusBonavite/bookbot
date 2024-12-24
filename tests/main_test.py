import unittest
import sys
# Importing main functionality
sys.path.append("../")
import main 

class Test(unittest.TestCase):

    def test_word_counter(self):
        self.assertEqual(main.word_counter("Hello World"), 2)


if __name__ == "__main__":
    unittest.main()
