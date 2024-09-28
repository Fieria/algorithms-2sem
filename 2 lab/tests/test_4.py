import unittest
from task_4 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        array = ["+ 1", "+ 4", "+ 3", "+ 3", "? 1", "? 2", "? 3", "+ 2", "? 3"]
        result = [1, 3, 4, 3]

        self.assertEqual(result, solve(array))

if __name__ == "__main__":
    unittest.main()
