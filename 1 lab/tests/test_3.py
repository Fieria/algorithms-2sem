import unittest
from task_3 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solve([23], [39], 1), 897)

    def test_ex2(self):
        self.assertEqual(solve([1, 3, -5], [-2, 4, 1], 3), 23)


if __name__ == "__main__":
    unittest.main()
