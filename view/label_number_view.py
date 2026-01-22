from tkinter import *

class LabelNumberView :
    __window = None
    __label = None

    def __init__ ( self, window ) :
        LabelNumberView.__window = window

    def create_label ( self ) :
        LabelNumberView.__label = Label( LabelNumberView.__window, text = 'число', padx = 20, pady = 4 )
        LabelNumberView.__label.grid( row = 0, column = 2 )
