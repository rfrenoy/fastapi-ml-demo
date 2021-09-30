import unittest
from divide import divide
from hypothesis import given, strategies as st


class TestDivide(unittest.TestCase):
    @given(st.integers(), st.integers())
    def test_divide(self, a, b):
        divide(a, b)
