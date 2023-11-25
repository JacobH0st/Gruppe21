from tkinter import Tk, ttk
import pytest

from functions import MarketplaceBase
from main_application import MainApplication


@pytest.fixture
def app():
    root = Tk()
    yield root
    root.destroy()

@pytest.fixture

def main_app(app):
    return MainApplication()
@pytest.fixture
def marketplace_app(main_app):
    return MarketplaceBase(main_app)

#Testing the load data method
def test_load_data(marketplace_app):
    marketplace_app.load_data()
    assert isinstance(marketplace_app.tours_data, list)



