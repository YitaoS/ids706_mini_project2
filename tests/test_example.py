import unittest
import pandas as pd
from io import StringIO
from main import read_dataset, generate_descriptive_stats, generate_visualizations  

class TestPollingPlaceAnalysis(unittest.TestCase):

    def setUp(self):
        """Sets up a mock dataset to use for testing."""
        self.data = """city\tstate\tzip
        New York\tNY\t10001
        Los Angeles\tCA\t90001
        Chicago\tIL\t60601
        Houston\tTX\t77001
        Phoenix\tAZ\t85001
        """
        # Create a DataFrame to simulate data being read from a file
        self.df = pd.read_csv(StringIO(self.data), sep='\t')

    def test_read_dataset(self):
        """Test the read_dataset function."""
        df = read_dataset(StringIO(self.data))  # Simulate reading from a file
        self.assertEqual(len(df), 5)  # Check if the number of rows is correct
        self.assertListEqual(list(df.columns), ['city', 'state', 'zip'])  # Check if column names are correct

    def test_generate_descriptive_stats(self):
        """Test the generate_descriptive_stats function."""
        stats_numeric, stats_categorical = generate_descriptive_stats(self.df)
        
        # Check if categorical data statistics are correctly generated
        self.assertIn('city', stats_categorical.columns)  # 'city' column should exist
        self.assertIn('state', stats_categorical.columns)  # 'state' column should exist

    def test_generate_visualizations(self):
        """Test the generate_visualizations function."""
        # Check if visualizations are generated without errors (no need to check actual plots)
        try:
            generate_visualizations(self.df)
        except Exception as e:
            self.fail(f"generate_visualizations raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
