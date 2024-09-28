import unittest
from task_9 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        n = 6
        array = [[-2, 0, 2],
                 [8, 4, 3],
                 [9, 0, 0],
                 [3, 6, 5],
                 [6, 0, 0],
                 [0, 0, 0]]
        m = 4
        requests = [6, 9, 7, 8]
        result = [5, 4, 4, 1]

        self.assertEqual(result, solve(n, array, m, requests))


if __name__ == "__main__":
    unittest.main()
