import unittest
from task_1 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        t = "aba"
        p = "abaCaba"
        n = 2
        indexes = [1, 5]

        self.assertEqual((n, indexes), solve(t, p))

if __name__ == "__main__":
    unittest.main()
