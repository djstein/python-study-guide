# O(N)
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
import unittest

def unqiue_chars(string):
    # If greater than ASCII total
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    # check if int value is in 
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


class Test(unittest.TestCase):
    
    def test_unqiue_chars(self):
        test_string = "a really good test string"
        test_string_two = "two bigpears"

        self.assertFalse(unqiue_chars(test_string))
        self.assertTrue(unqiue_chars(test_string_two))

if __name__ == "__main__":
    unittest.main()