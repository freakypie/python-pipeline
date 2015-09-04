from django.test.testcases import TestCase
from .main import Pipeline
from .test_helpers import A, B, C, D


class PiplineTest(TestCase):

    def test_processing(self):
        pipe = Pipeline([A])
        self.assertEqual(pipe.process(), {"A": 1})
        pipe = Pipeline([A, B])
        self.assertEqual(pipe.process(), {"A": 2, "B": True})
        pipe = Pipeline([A, B, C])
        self.assertEqual(pipe.process(), {"C": "masterful"})

    def test_stop(self):
        pipe = Pipeline([A, D, B, C])
        self.assertEqual(pipe.process(), {"A": 1})

    def test_load(self):
        pipe = Pipeline()
        pipe.load([
            "pipeline.test_helpers.A",
            "pipeline.test_helpers.B"
        ])
        self.assertEqual(pipe.process(), {"A": 2, "B": True})
