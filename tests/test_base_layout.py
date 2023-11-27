import tkinter as tk
import pytest
from ui_components.base_layout import BaseLayout

@pytest.fixture
def base_layout():
    root = tk.Tk()
    app = MockApplication()
    base_layout = BaseLayout(root, app)
    return base_layout

#WIDGETS:
#Testing the widgets to check if they are created.

# Testing if the view button widget is created
def test_is_view_button_created(base_layout):
    assert isinstance(base_layout.view_button, tk.Button)

# Testing if the back button widget is created
def test_is_back_button_created(base_layout):
    assert isinstance(base_layout.back_button, tk.Button)

# Testing the default text of the view button
def test_view_button_default_text(base_layout):
    assert base_layout.view_button.cget("text") == "Markedsplass"

# Testing the default text of the back button
def test_back_button_default_text(base_layout):
    assert base_layout.back_button.cget("text") == "Tilbake"

# Mocking the application class for testing
class MockApplication:
    def show_user_marketplace(self):
        pass

    def setup_mode_selection(self):
        pass
