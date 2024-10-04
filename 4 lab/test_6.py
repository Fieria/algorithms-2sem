import unittest
from task_6 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        s = "aaaAAA"
        result = "2 1 0 0 0"

        self.assertEqual(result, solve(s))

    def test_ex2(self):
        s = "abacaba"
        result = "0 1 0 3 0 1"

        self.assertEqual(result, solve(s))

if __name__ == "__main__":
    unittest.main()
