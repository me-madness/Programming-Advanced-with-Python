from tkinter import Button
from canvas import root, frame


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
    print("Register")    
    
    
def login():
    print("Login")    