import unittest
from task_11 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solve(10, 3, [1, 4, 8]), 9)

    def test_ex2(self):
        self.assertEqual(solve(11, 5, [6, 2, 2, 2, 4]), 10)


if __name__ == "__main__":
    unittest.main()
