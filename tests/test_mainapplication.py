#python -m pytest

from tkinter import Frame
import pytest

from main_application import MainApplication


@pytest.fixture
def app_and_frame():
    app = MainApplication()
    frame = Frame(app)
    yield app, frame
    app.destroy()
    
# Test if clicking user mode button sets the correct mode
def test_user_mode_button(app_and_frame):
    app, frame = app_and_frame
    app.show_buttons("User")
    assert app.current_mode == "User"

# Test if clicking user mode button sets the correct mode
def test_guide_mode_button(app_and_frame):
    app, frame = app_and_frame
    app.show_buttons("Guide")
    assert app.current_mode == "Guide"
    
# Test if clicking admin mode button sets the correct mode
def test_admin_mode_button(app_and_frame):
    app, frame = app_and_frame
    app.show_buttons("Admin")
    assert app.current_mode == "Admin"