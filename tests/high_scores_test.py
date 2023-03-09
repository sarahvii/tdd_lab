import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        scores = [100, 0, 90, 30]
        expected = 30
        self.assertEqual(expected, latest(scores))

    # Test personal best (the highest score in the list)

    def test_personal_best(self):
        scores = [100, 0, 90, 30]
        expected = 100
        self.assertEqual(expected, personal_best(scores))

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
