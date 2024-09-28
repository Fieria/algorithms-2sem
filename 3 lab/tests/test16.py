import unittest
from task_16 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        n = 3
        array = [["p1", "p1", "p2"], ["p2", "p1"], ["p3", "p1"]]
        result = ["YES", "YES", "NO"]

        self.assertEqual(result, solve(n, array))

if __name__ == "__main__":
    unittest.main()
