from tkinter import *

class ButtonApplyView :
    __window = None
    __button = None

    def __init__ ( self, window ) :
        ButtonApplyView.__window = window

    def create_button ( self ) :
        ButtonApplyView.__button = Button( ButtonApplyView.__window, text = 'Применить', justify = CENTER )
        ButtonApplyView.__button.grid( padx = 10, pady = 4, row = 5, column = 1 )
