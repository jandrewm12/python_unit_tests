# Python Unit Tests
# Written for INFOTC4320 Module 13
# Written by: Jacob McIntosh jam6m4
# ---------------------------------------------


# imports
import unittest
import inputs
from datetime import date


class InputTest(unittest.TestCase):

    def setUp(self):
        self.symbol = "AAPL"
        self.chart_type = "1"
        self.time_series = "2"
        self.start_date = "2020-3-20"
        self.end_date = "2021-10-18"

    def test_symbol(self):
        print("Checking symbol...")
        self.assertEqual(inputs.symbol(self.symbol), self.symbol)

    def test_chart_type(self):
        print("Checking chart type...")

        if self.chart_type == "1":
            self.assertEqual(inputs.chart_type(self.chart_type), "Line")
        elif self.chart_type == "2":
            self.assertEqual(inputs.chart_type(self.chart_type), "Bar")

    def test_time_series(self):
        print("Checking time series")

        if self.time_series == "1":
            self.assertEqual(inputs.time_series(self.time_series), "Intraday")
        elif self.time_series == "2":
            self.assertEqual(inputs.time_series(self.time_series), "Daily")
        elif self.time_series == "3":
            self.assertEqual(inputs.time_series(self.time_series), "Weekly")
        elif self.time_series == "4":
            self.assertEqual(inputs.time_series(self.time_series), "Monthly")
        
    def test_start_date(self):
        print("Checking start date...")

        y = int(self.start_date.split("-")[0])
        m = int(self.start_date.split("-")[1])
        d = int(self.start_date.split("-")[2])

        s_date = date(y, m, d)
        s_date = s_date.strftime('%Y-%m-%d')

        self.assertEqual(inputs.start_date(self.start_date), s_date)

    def test_start_date(self):
        print("Checking end date...")

        y = int(self.end_date.split("-")[0])
        m = int(self.end_date.split("-")[1])
        d = int(self.end_date.split("-")[2])

        e_date = date(y, m, d)
        e_date = e_date.strftime('%Y-%m-%d')

        self.assertEqual(inputs.end_date(self.end_date), e_date)



if __name__ == "__main__":
    unittest.main()

