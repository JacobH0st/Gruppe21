#python -m unittest test_baselayout.py

import sys

from main_application import MainApplication
sys.path.append("..")
import unittest
import tkinter as tk

class TestMainApplication(unittest.TestCase):
    
    def setUp(self):
        self.app = MainApplication()

    def tearDown(self):
        self.app.destroy()
    
    #Testing the title of the application
    def test_window_title_is_correct(self):
        self.assertEqual(self.app.title(), "Turisme marketsplass")
    
    #Testing the size of the application
    def test_geometry_size_is_correct(self):
        self.app.update()
        size = self.app.geometry().split('+')[0]
        self.assertEqual(size, "700x500")

if __name__ == "__main__":
    unittest.main()