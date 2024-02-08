from tkinter import Button
from canvas import root, frame


def render_entry():
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white", 
        bd=0,
        width=90,
        height=40,
    )
    
    frame.create_window(350, 260, window=register_button)