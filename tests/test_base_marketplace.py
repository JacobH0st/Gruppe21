

from tkinter import Button, Listbox, Scrollbar
from tkinter.ttk import Treeview

import pytest
from functions import MarketplaceBase
from main_application import MainApplication


@pytest.fixture
def app_and_frame():
    app = MainApplication()
    frame = app.marketplace_frame
    yield app, frame
    app.destroy()
    
#Testing to see if the treeview widget is created
def test_is_base_marketplace_treeview_widget_created(app_and_frame):
    app, frame = app_and_frame
    marketplace_base = MarketplaceBase(app)
    assert isinstance(marketplace_base.tree, Treeview)

#Testing to see if the listbox widget is created
def test_is_base_marketplace_listbox_widget_created(app_and_frame):
    app, frame = app_and_frame
    marketplace_base = MarketplaceBase(app)
    assert isinstance(marketplace_base.listbox, Listbox)

#Testing to see if the back button widget is created
def test_is_base_marketplace_back_button_widget_created(app_and_frame):
    app, frame = app_and_frame
    marketplace_base = MarketplaceBase(app)
    assert isinstance(marketplace_base.back_button, Button)
    
#Testing to see if the listbox treeview widget is created 
def test_is_base_marketplace_listbox_scrollbar_widget_created(app_and_frame):
    app, frame = app_and_frame
    marketplace_base = MarketplaceBase(app)
    assert isinstance(marketplace_base.scrollbar_listbox, Scrollbar)
 
#Testing to see if the treeview scrollbar widget is created   
def test_is_base_marketplace_treeview_scrollbar_widget_created(app_and_frame):
    app, frame = app_and_frame
    marketplace_base = MarketplaceBase(app)
    assert isinstance(marketplace_base.scrollbar_treeview, Scrollbar)