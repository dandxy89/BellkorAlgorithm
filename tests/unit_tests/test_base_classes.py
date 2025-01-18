import unittest
from pathlib import Path

from bellkor.base.base_object import Model


class TestAllBaseObjects(unittest.TestCase):
    """Testing all the Classes located in the Base sub-directory"""

    def setUp(self):
        self.base_methods_and_attributes = {
            "PARAMS",
            "get_params",
            "load_parameters",
            "pickle_parameters",
            "predict",
            "train",
        }

    def test_base_model_init(self):
        base_model = Model()

        # Assertions
        self.assertEqual(len(self.base_methods_and_attributes), 6)
        self.assertEqual(
            len(set(base_model.__dir__()).intersection(self.base_methods_and_attributes)),
            6,
        )

    def test_loading_pickle(self):
        base_model3 = Model()

        file_path = Path(__file__).parent.parent
        base_model3.load_parameters(file_path=file_path / "test_data/LOADING_PICKLE.pickle")

        self.assertEqual(base_model3.PARAMS, {"Test": 1})


if __name__ == "__main__":
    unittest.main()
