# tests/test_disk_analyzer.py
import unittest
from src.disk_analyzer import get_disk_usage, list_partitions, analyze_disk

class TestDiskAnalyzer(unittest.TestCase):
    def test_get_disk_usage(self):
        usage = get_disk_usage()
        self.assertIsInstance(usage, dict)
        self.assertIn('total', usage)
        self.assertIn('used', usage)
        self.assertIn('free', usage)

    def test_list_partitions(self):
        partitions = list_partitions()
        self.assertIsInstance(partitions, list)
        self.assertTrue(len(partitions) > 0)

    def test_analyze_disk(self):
        analysis = analyze_disk()
        self.assertIsInstance(analysis, str)
        self.assertIn('Total', analysis)
        self.assertIn('Used', analysis)
        self.assertIn('Free', analysis)

if __name__ == '__main__':
    unittest.main()