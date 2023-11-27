import tkinter as tk
import pytest
from ui_components.user_layout import UserLayout

@pytest.fixture
def user_layout():
    root = tk.Tk()
    app = MockApplication()
    layout = UserLayout(root, app)
    layout.setup_ui()
    return layout

#WIDGETS:
#Testing the widgets to check if they are created.

# Testing if the view_button widget is created
def test_is_user_layout_view_button_created(user_layout):
    assert hasattr(user_layout, "view_button")
    assert isinstance(user_layout.view_button, tk.Button)

# Testing if the back_button widget is created
def test_is_user_layout_back_button_created(user_layout):
    assert hasattr(user_layout, "back_button")
    assert isinstance(user_layout.back_button, tk.Button)

# Mocking the application class for testing
class MockApplication:
    def show_user_marketplace(self):
        pass

    def setup_mode_selection(self):
        pass

