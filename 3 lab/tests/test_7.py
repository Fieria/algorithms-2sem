import unittest
from task_7 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        n = 4
        edges = ["1 2", "4 1", "2 3", "3 1"]
        result = 0

        self.assertEqual(result, solve(n, edges))

    def test_ex2(self):
        n = 5
        edges = ["5 2", "4 2", "3 4", "1 4"]
        result = 1

        self.assertEqual(result, solve(n, edges))

if __name__ == "__main__":
    unittest.main()
