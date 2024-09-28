import unittest
from task_7 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        n = 3
        array = [[2, 1, 2],
                 [1, -1, -1],
                 [3, -1, -1]]
        result = "CORRECT"

        self.assertEqual(result, solve(n, array))

    def test_ex2(self):
        n = 3
        array = [[1, 1, 2],
                 [2, -1, -1],
                 [3, -1, -1]]
        result = "INCORRECT"

        self.assertEqual(result, solve(n, array))

    def test_ex3(self):
        n = 3
        array = [[2, 1, 2],
                 [1, -1, -1],
                 [2, -1, -1]]
        result = "CORRECT"

        self.assertEqual(result, solve(n, array))

    def test_ex4(self):
        n = 3
        array = [[2, 1, 2],
                 [2, -1, -1],
                 [3, -1, -1]]
        result = "INCORRECT"

        self.assertEqual(result, solve(n, array))

    def test_ex5(self):
        n = 5
        array = [[1, -1, 1],
                 [2, -1, 2],
                 [3, -1, 3],
                 [4, -1, 4],
                 [5, -1, -1]]
        result = "CORRECT"

        self.assertEqual(result, solve(n, array))

    def test_ex6(self):
        n = 7
        array = [[4, 1, 2],
                 [2, 3, 4],
                 [6, 5, 6],
                 [1, -1, -1],
                 [3, -1, -1],
                 [5, -1, -1],
                 [7, -1, -1]]
        result = "CORRECT"

        self.assertEqual(result, solve(n, array))

    def test_ex7(self):
        n = 1
        array = [[2147483647, -1, -1]]
        result = "CORRECT"

        self.assertEqual(result, solve(n, array))

    def test_my_test1(self):
        n = 5
        array = [[5, 1, 2],
                 [4, 3, 4],
                 [6, -1, -1],
                 [1, -1, -1],
                 [5, -1, -1]]
        result = "INCORRECT"

        self.assertEqual(result, solve(n, array))

    def test_my_test2(self):
        n = 5
        array = [[5, 1, 2],
                 [4, 3, 4],
                 [5, -1, -1],
                 [1, -1, -1],
                 [4, -1, -1]]
        result = "CORRECT"

        self.assertEqual(result, solve(n, array))

    def test_my_test3(self):
        n = 0
        array = []
        result = "CORRECT"

        self.assertEqual(result, solve(n, array))


if __name__ == "__main__":
    unittest.main()
