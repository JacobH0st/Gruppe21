import tkinter as tk
import pytest
from ui_components.admin_layout import AdminLayout

@pytest.fixture
def admin_layout():
    root = tk.Tk()
    app = MockApplication()
    admin_layout = AdminLayout(root, app)
    return admin_layout

#WIDGETS:
#Testing the widgets to check if they are created.

# Testing if the delete_guide_button widget is created
def test_is_admin_layout_delete_guide_button_created(admin_layout):
    admin_layout.setup_ui()
    assert isinstance(admin_layout.delete_guide_button, tk.Button)

# Testing the default text of the delete_guide_button
def test_is_admin_layout_delete_guide_button_default_text(admin_layout):
    admin_layout.setup_ui()
    assert admin_layout.delete_guide_button.cget("text") == "Slett guides"

# Mocking the application class for testing
class MockApplication:
    def show_user_marketplace(self):
        pass

    def show_admin_marketplace(self):
        pass

    def setup_mode_selection(self):
        pass
