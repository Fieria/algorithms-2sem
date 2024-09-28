import unittest
from task_14 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solve('1+5'), 6)

    def test_ex2(self):
        self.assertEqual(solve('5-8+7*4-8+9'), 200)

if __name__ == "__main__":
    unittest.main()
