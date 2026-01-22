from tkinter import *

class EntryMinutesView :
    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryMinutesView.__window = window

    def create_entry ( self ) :
        EntryMinutesView.__entry = Entry( EntryMinutesView.__window, justify = CENTER, width = 4 )
        EntryMinutesView.__entry.grid( row = 3, column = 1 )
