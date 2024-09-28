import unittest
from task_1 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        n = 5
        array = [[4, 1, 2],
                 [2, 3, 4],
                 [5, -1, -1],
                 [1, -1, -1],
                 [3, -1, -1]]
        result = ("1 2 3 4 5", "4 2 1 3 5", "1 3 2 5 4")

        self.assertEqual(result, solve(n, array))

    def test_ex2(self):
        n = 10
        array = [[0, 7, 2],
                 [10, -1, -1],
                 [20, -1, 6],
                 [30, 8, 9],
                 [40, 3, -1],
                 [50, -1, -1],
                 [60, 1, -1],
                 [70, 5, 4],
                 [80, -1, -1],
                 [90, -1, -1]]
        result = ("50 70 80 30 90 40 0 20 10 60", "0 70 50 40 30 80 90 20 60 10", "50 80 90 30 40 70 10 60 20 0")

        self.assertEqual(result, solve(n, array))


if __name__ == "__main__":
    unittest.main()
