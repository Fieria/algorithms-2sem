import unittest
from task_6 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(solve(['21', '2']), '221')

    def test_ex2(self):
        self.assertEqual(solve(['23', '39', '92']), '923923')


if __name__ == "__main__":
    unittest.main()
