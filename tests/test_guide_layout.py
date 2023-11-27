import tkinter as tk
import pytest
from ui_components.guide_layout import GuideLayout

@pytest.fixture
def guide_layout():
    root = tk.Tk()
    app = MockApplication()
    guide_layout = GuideLayout(root, app)
    return guide_layout

#WIDGETS:
#Testing the widgets to check if they are created.

# Testing if the change_guide_info_button widget is created
def test_is_guide_layout_change_guide_info_button_created(guide_layout):
    guide_layout.setup_ui()
    assert isinstance(guide_layout.change_guide_info_button, tk.Button)

# Testing the default text of the change_guide_info_button
def test_is_guide_layout_change_guide_info_button_default_text(guide_layout):
    guide_layout.setup_ui()
    assert guide_layout.change_guide_info_button.cget("text") == "Endre guide info"

# Testing if the add_guide_button widget is created
def test_is_guide_layout_add_guide_button_created(guide_layout):
    guide_layout.setup_ui()
    assert isinstance(guide_layout.add_guide_button, tk.Button)

# Testing the default text of the add_guide_button
def test_is_guide_layout_add_guide_button_default_text(guide_layout):
    guide_layout.setup_ui()
    assert guide_layout.add_guide_button.cget("text") == "Legg til guide"

# Mocking the application class for testing
class MockApplication:
    def show_guide_marketplace(self):
        pass

    def show_create_data_entry_form(self):
        pass

    def show_user_marketplace(self):
        pass

    def setup_mode_selection(self):
        pass
