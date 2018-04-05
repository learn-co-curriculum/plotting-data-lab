import unittest2 as unittest
from ipynb.fs.full.index import *

class TestPlotlyTraces(unittest.TestCase):
    def test_first_three_pops(self):
        self.assertItemsEqual(trace_first_three_pops['x'], ['Buenos Aires', 'Toronto', 'Pyeongchang'])
        self.assertItemsEqual(trace_first_three_pops['y'], [2891000, 2800000, 2581000])

    def test_bar_chart(self):
        self.assertEqual(bar_trace_first_three_pops['type'], 'bar')

    def test_multiple_traces(self):
        self.assertEqual(bar_trace_first_three_pops['type'], 'bar')
        self.assertEqual(bar_trace_first_three_areas['type'], 'bar')
        self.assertItemsEqual(bar_trace_first_three_pops['y'], [2891000, 2800000, 2581000])
        self.assertItemsEqual(bar_trace_first_three_pops['x'], ['Buenos Aires', 'Toronto', 'Pyeongchang'])
        self.assertItemsEqual(bar_trace_first_three_areas['y'], [4758, 2731571, 3194])
        self.assertItemsEqual(bar_trace_first_three_areas['x'], ['Buenos Aires', 'Toronto', 'Pyeongchang'])
