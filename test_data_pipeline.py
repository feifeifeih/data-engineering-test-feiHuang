import unittest
import pandas as pd
from data_pipeline import validata_data, transform_data

class TestDataPipeline(unittest.TestCase):
    def setUp(self):
        # no missing values
        self.df_valid = pd.DataFrame({
            "ITEM TYPE": ["Clothing", "Electronics", "Clothing"],
            "RETAIL SALES": [1000, 2000, 500]
        })

        # with missing values
        self.df_missing = pd.DataFrame({
            "ITEM TYPE": ["Clothing", None, "Electronics"],
            "RETAIL SALES": [1000, 2000, None]
        })

    def test_validata_data_no_missing(self):
        """
        if the DataFrame has no missing values, it should remain unchanged.
        """

        df_result = validata_data(self.df_valid.copy())
        self.assertTrue(df_result.equals(self.df_valid), 
                        "no missing values, remain the same.")

    def test_validata_data_missing(self):
        """
        Missing values in critical columns (ITEM TYPE, RETAIL SALES) should be filled with 0.
        """

        df_result = validata_data(self.df_missing.copy())
        self.assertFalse(df_result.isnull().values.any(), 
                         "missing values, filled with 0.")

    def test_transform_data(self):
        """
        transform_data should group "RETAIL SALES" by "ITEM TYPE"
        and rename the column to "Total_SALES".
        """

        df_transformed = transform_data(self.df_valid.copy())

        # check if the output DataFrame has the correct columns
        self.assertIn("ITEM TYPE", df_transformed.columns)
        self.assertIn("Total_SALES", df_transformed.columns)

        # check row count: we expect 2 unique ITEM TYPEs: Clothing, Electronics
        self.assertEqual(len(df_transformed), 2, "should have 2 rows after grouping by ITEM TYPE.")

        # validate aggregated
        clothing_sales = df_transformed.loc[df_transformed["ITEM TYPE"] == "Clothing", "Total_SALES"].iloc[0]
        electronics_sales = df_transformed.loc[df_transformed["ITEM TYPE"] == "Electronics", "Total_SALES"].iloc[0]
        self.assertEqual(clothing_sales, 1500, "Clothing should be 1500.")
        self.assertEqual(electronics_sales, 2000, "Electronics should be 2000.")

if __name__ == "__main__":
    unittest.main()
