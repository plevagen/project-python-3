# Test Results:
# test_analyse_twice (tests.test_analyser.TestAnalyser.test_analyse_twice) ... ok
# test_result_has_required_keys (tests.test_analyser.TestAnalyser.test_result_has_required_keys) ... ok
# test_result_is_not_empty (tests.test_analyser.TestAnalyser.test_result_is_not_empty) ... ok
# test_total_students (tests.test_analyser.TestAnalyser.test_total_students) ... ok

# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s

# OK

import unittest
from analytics.analyser import GpaAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.sample = [
            {"GPA": "3.8", "sleep_hours": "7", "country": "USA",
            "final_exam_score": "95", "study_hours_per_day": "4"},
            {"GPA": "2.5", "sleep_hours": "5", "country": "India",
            "final_exam_score": "72", "study_hours_per_day": "2"},
            {"GPA": "3.9", "sleep_hours": "8", "country": "USA",
            "final_exam_score": "98", "study_hours_per_day": "5"},
            {"GPA": "1.8", "sleep_hours": "4", "country": "Canada",
            "final_exam_score": "55", "study_hours_per_day": "1"},
            {"GPA": "3.5", "sleep_hours": "6", "country": "India",
            "final_exam_score": "88", "study_hours_per_day": "3"},
        ]

    def test_result_is_not_empty(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("average_gpa", analyser.result)
        self.assertIn("max_gpa", analyser.result)
        self.assertIn("min_gpa", analyser.result)
        self.assertIn("high_performers", analyser.result)

    def test_analyse_twice(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, result1)

if __name__ == '__main__':
    unittest.main()