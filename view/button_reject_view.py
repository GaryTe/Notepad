from tkinter import *

class ButtonRejectView :
    __window = None
    __button = None

    def __init__ ( self, window ) :
        ButtonRejectView.__window = window

    def create_button ( self ) :
        ButtonRejectView.__button = Button( ButtonRejectView.__window, text = 'Отклонить', justify = CENTER )
        ButtonRejectView.__button.grid( padx = 4, pady = 4, row = 5, column = 0 )
