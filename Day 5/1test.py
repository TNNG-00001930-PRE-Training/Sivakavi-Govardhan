import unittest
def concatenate_strings(s1, s2):
    return s1 + s2
def slice_string(s, start, end):
    return s[start:end]
def format_string(name, age):
    return "My name is {} and I am {} years old".format(name, age)
def manipulate_string(s):
    return s.upper(), s.lower(), s.strip(), s.replace("World", "Universe")
class TestStringOperations(unittest.TestCase):
    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello", "World"), "HelloWorld")
    def test_slice_string(self):
        self.assertEqual(slice_string("Hello World", 6, None), "World")
    def test_format_string(self):
        self.assertEqual(format_string("Alice", 30), "My name is Alice and I am 30 years old")
    def test_manipulate_string(self):
        self.assertEqual(manipulate_string("Hello World"), ("HELLO WORLD", "hello world", "Hello World", "Hello Universe"))

if __name__ == '__main__':
    unittest.main()
