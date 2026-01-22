from tkinter import *

class LabelMinutesView :
    __window = None
    __label = None

    def __init__ ( self, window ) :
        LabelMinutesView.__window = window

    def create_label ( self ) :
        LabelMinutesView.__label = Label( LabelMinutesView.__window, text = 'минуты', padx = 20, pady = 4 )
        LabelMinutesView.__label.grid( row = 2, column = 1 )
