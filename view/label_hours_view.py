from tkinter import *

class LabelHoursView :
    __window = None
    __label = None

    def __init__ ( self, window ) :
        LabelHoursView.__window = window

    def create_label ( self ) :
        LabelHoursView.__label = Label( LabelHoursView.__window, text = 'часы', padx = 20, pady = 4 )
        LabelHoursView.__label.grid( row = 3, column = 0 )
