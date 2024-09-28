import unittest
from task_16 import solve


class Test(unittest.TestCase):
    def test_ex1(self):
        dist = [[0, 183, 163, 173, 181],
                [183, 0, 165, 172, 171],
                [163, 165, 0, 189, 302],
                [173, 172, 189, 0, 167],
                [181, 171, 302, 167, 0]]
        n = 5
        self.assertEqual((666, [1, 3, 2, 5, 4]), solve(dist, n))

if __name__ == "__main__":
    unittest.main()
