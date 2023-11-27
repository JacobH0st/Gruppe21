from tkinter import Button, Listbox, Scrollbar
from tkinter.ttk import Treeview
import pytest

from functions import AdminMarketplace
from main_application import MainApplication

@pytest.fixture
def app_and_frame():
    app = MainApplication()
    frame = app.marketplace_frame
    yield app, frame
    app.destroy()
    
#Testing the base widget

#Testing to see if the treeview widget is created
def test_is_admin_marketplace_treeview_widget_created(app_and_frame):
    app, frame = app_and_frame
    admin_marketplace = AdminMarketplace(app)
    assert isinstance(admin_marketplace.tree, Treeview)

#Testing to see if the listbox widget is created
def test_is_admin_marketplace_listbox_widget_created(app_and_frame):
    app, frame = app_and_frame
    admin_marketplace = AdminMarketplace(app)
    assert isinstance(admin_marketplace.listbox, Listbox)

#Testing to see if the back button widget is created
def test_is_admin_marketplace_back_button_widget_created(app_and_frame):
    app, frame = app_and_frame
    admin_marketplace = AdminMarketplace(app)
    assert isinstance(admin_marketplace.back_button, Button)
    
#Testing to see if the listbox treeview widget is created 
def test_is_admin_marketplace_listbox_scrollbar_widget_created(app_and_frame):
    app, frame = app_and_frame
    admin_marketplace = AdminMarketplace(app)
    assert isinstance(admin_marketplace.scrollbar_listbox, Scrollbar)
 
#Testing to see if the treeview scrollbar widget is created   
def test_is_admin_marketplace_treeview_scrollbar_widget_created(app_and_frame):
    app, frame = app_and_frame
    admin_marketplace = AdminMarketplace(app)
    assert isinstance(admin_marketplace.scrollbar_treeview, Scrollbar)   
    
#Testing to see if the delete button widget is created
def test_is_admin_marketplace_delete_button_widget_created(app_and_frame):
    app, frame = app_and_frame
    admin_marketplace = AdminMarketplace(app)
    assert isinstance(admin_marketplace.delete_button, Button)
    