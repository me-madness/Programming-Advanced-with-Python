from tkinter import Tk, Canvas

def create_root():
    root = Tk()
    
    root.title("GUI Shop")
    root.geometry("700x600")
    root.resizable(width:False, height:False)
    
    return root


def crete_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)
    
    return frame

root = create_root
frame = crete_frame