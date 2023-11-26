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
    
#Testing if clicking user mode button sets the correct mode
def test_user_mode_button(app_and_frame):
    app, frame = app_and_frame
    app.show_buttons("User")
    assert app.current_mode == "User"

#Testing if clicking user mode button sets the correct mode
def test_guide_mode_button(app_and_frame):
    app, frame = app_and_frame
    app.show_buttons("Guide")
    assert app.current_mode == "Guide"
    
#Testing if clicking admin mode button sets the correct mode
def test_admin_mode_button(app_and_frame):
    app, frame = app_and_frame
    app.show_buttons("Admin")
    assert app.current_mode == "Admin"

#Testing if the setup_mode_selection method correctly clears the main frame
def test_setup_mode_selection_clears_frame(app_and_frame):
    app, frame = app_and_frame
    app.show_buttons("User")
    app.setup_mode_selection()
    assert not frame.winfo_children()
    
#Testing if the default mode is none when starting the application
def test_is_main_application_current_mode_none_on_initialization(app_and_frame):
    app = MainApplication()
    assert app.current_mode is None