from tkinter import *

class LabelMonthView :
    __window = None
    __label = None

    def __init__ ( self, window ) :
        LabelMonthView.__window = window

    def create_label ( self ) :
        LabelMonthView.__label = Label( LabelMonthView.__window, text = 'месяц', padx = 20, pady = 4 )
        LabelMonthView.__label.grid( row = 0, column = 1 )
