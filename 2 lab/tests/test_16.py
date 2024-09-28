import unittest
from task_16 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        commands = ['+1 5',
                    '+1 3',
                    '+1 7',
                    '0 1',
                    '0 2',
                    '0 3',
                    '-1 5',
                    '+1 10',
                    '0 1',
                    '0 2',
                    '0 3']
        result = [7, 5, 3, 10, 7, 3]
        self.assertEqual(result, solve(commands))


if __name__ == "__main__":
    unittest.main()
