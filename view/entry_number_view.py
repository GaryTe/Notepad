from tkinter import *

class EntryNumberView :
    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryNumberView.__window = window

    def create_entry ( self ) :
        EntryNumberView.__entry = Entry( EntryNumberView.__window, justify = CENTER, width = 4 )
        EntryNumberView.__entry.grid( row = 1, column = 2 )

    def clean_field ( self ) :
        EntryNumberView.__entry.delete(0, END)
