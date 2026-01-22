from tkinter import *

class LabelYearView :
    __window = None
    __label = None

    def __init__ ( self, window ) :
        LabelYearView.__window = window

    def create_label ( self ) :
        LabelYearView.__label = Label( LabelYearView.__window, text = 'год', padx = 20, pady = 4 )
        LabelYearView.__label.grid( row = 0, column = 0 )
