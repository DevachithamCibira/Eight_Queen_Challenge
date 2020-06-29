
import unittest

import Queen_challenge

class TestEightQueens(unittest.TestCase):

    Queen = Queen_challenge.EightQueens()

    def test_possiblemoves(self):
        self.Queen.Queen_moves()
        allmoves = []
        [[allmoves.append((row, col)) for col in range(1, 9)] for row in range(1, 9)]

        self.assertAlmostEqual(self.Queen.moves_possible,allmoves)

    def test_type(self):
        self.Queen.Run()
        self.assertIsInstance(self.Queen.end_result(), str)

    def test_unique_queen(self):
        self.Queen.working()
        for val in self.Queen.final_list:
            self.assertEqual(len(set(val)),len(val))


if __name__ == "__main__":
    unittest.main()





