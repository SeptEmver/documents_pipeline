from unittest import TestCase
from doc_resolve import Area

class TestArea(TestCase):

    """
------   ------
- lt -   - rt -
------   ------

------   ------
- lb -   - rb -
------   ------
    """
    lt = Area(100, 50, 40, 10)
    rt = Area(300, 50, 40, 10)
    lb = Area(100, 100, 40, 10)
    rb = Area(300, 100, 40, 10)

    def test_concatenation_lt_to_rb(self):
        self.assertEqual(TestArea.lt + TestArea.rb, Area(100, 50, 240, 60))

    def test_concatenation_lt_to_rt(self):
        self.assertEqual(TestArea.lt + TestArea.rt, Area(100, 50, 240, 10))

    def test_concatenation_lt_to_lb(self):
        self.assertEqual(TestArea.lt + TestArea.lb, Area(100, 50, 40, 60))

    def test_concatenation_rt_to_lb(self):
        self.assertEqual(TestArea.rt + TestArea.lb, Area(100, 50, 240, 60))

    def test_concatenation_lb_to_rt(self):
        self.assertEqual(TestArea.lb + TestArea.rt, Area(100, 50, 240, 60))

    def test_concatenation_rb_to_lt(self):
        self.assertEqual(TestArea.rb + TestArea.lt, Area(100, 50, 240, 60))

    def test_concatenation_rb_to_lb(self):
        self.assertEqual(TestArea.rb + TestArea.lb, Area(100, 100, 240, 10))

    def test_concatenation_rb_to_rt(self):
        self.assertEqual(TestArea.rb + TestArea.rt, Area(300, 50, 40, 60))


