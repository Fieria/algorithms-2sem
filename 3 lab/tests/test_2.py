import unittest
from task_2 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        n = 4
        edges = ["1 2", "3 2"]
        result = 2

        self.assertEqual(result, solve(n, edges))

if __name__ == "__main__":
    unittest.main()
