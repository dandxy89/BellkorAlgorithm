import pickle
import unittest
from pathlib import Path

from bellkor.algorithm import BellkorAlgorithm


class TestBellkorAlgorithm(unittest.TestCase):
    """Testing the Bellkor Algorithm"""

    def setUp(self):
        file_path = Path(__file__).parent.parent
        with open(file_path / "test_data/INIT_PARAMETERS.pickle", "rb") as handle:
            self.LOAD_INIT = pickle.load(handle)

    def test_bellkor_initialisation(self):
        # Initialise the Algorithm
        bk1 = BellkorAlgorithm(**self.LOAD_INIT)

        self.assertEqual(bk1.START_TIME, 789609600)
        self.assertEqual(bk1.END_TIME, 1427842800)
        self.assertEqual(len(bk1.PARAMS.p), 138493)


if __name__ == "__main__":
    unittest.main()
