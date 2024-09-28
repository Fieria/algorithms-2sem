import unittest
from task_3 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        array = ["+ 1", "+ 3", "+ 3", "> 1", "> 2", "> 3", "+ 2", "> 1"]
        result = [3, 3, 0, 2]

        self.assertEqual(result, solve(array))

if __name__ == "__main__":
    unittest.main()
