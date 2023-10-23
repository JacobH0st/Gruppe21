#python -m unittest test_baselayout.py

import sys
sys.path.append("..")
import unittest
import tkinter as tk
from base_layout import BaseLayout, home

class TestBaseLayout(unittest.TestCase):
    
    def setUp(self):
        self.app = BaseLayout()

    def tearDown(self):
        self.app.destroy()
    
    #Testing the title of the application
    def test_window_title_is_correct(self):
        self.assertEqual(self.app.title(), "Turisme marketsplass")
    
    #Testing the size of the application
    def test_geometry_size_is_correct(self):
        self.app.update()
        size = self.app.geometry().split('+')[0]
        self.assertEqual(size, "500x500")

if __name__ == "__main__":
    unittest.main()