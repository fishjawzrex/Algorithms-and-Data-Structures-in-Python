import unittest

from root import root


class TestRoot(unittest.TestCase):
    def test_root(self):
        self.assertAlmostEqual(root(4),2)
    
#if __name__ == '__main__':
unittest.main()