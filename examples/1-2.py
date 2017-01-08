import unittest

def urlify(string):
    string = string.replace(" ", "%20")
    return string


class Test(unittest.TestCase):

    def setUp(self):
        self.data = [(
            "Test this out wow",
            "Test%20this%20out%20wow"
        )]

    def test_urlify(self):
        for [string, expected] in self.data:
            actual = urlify(string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()