# from tkinter import Entry
from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen

def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",        #background color
        fg="white",        #color
        bd=0,              #border
        width=90,
        height=40,
        command=register
        
    )
    

    login_button = Button(
        root,
        text="Login",
        bg="green",
        fg="white", 
        bd=0,
        width=90,
        height=40,
        command=login 
        
    )
    
    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 310, window=login_button)
    
    
def register():
    clean_screen()
    
        
    frame.create_text(100, 50, text="First Name:")
    frame.create_text(100, 100, text="Last Name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")
    
    
    frame.create_window(230, 50, window=first_name_box)
    frame.create_window(230, 100, window=last_name_box)
    frame.create_window(230, 150, window=username_box)
    frame.create_window(230, 200, window=password_box)
    
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white", 
        bd=0,
        width=80,
        height=40,
        command=registration   
        
    )
    
    frame.create_window(315, 250, window=register_button)
    
    
def registration():
    print("Register")    
    
    
def login():
    clean_screen()
    print("Login")  
    
    
first_name_box = Entry(root, bd=0)    
last_name_box = Entry(root, bd=0)    
username_box = Entry(root, bd=0)    
password_box = Entry(root, bd=0)    
      