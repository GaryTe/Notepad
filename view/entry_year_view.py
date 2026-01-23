from tkinter import *

class EntryYearView :
    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryYearView.__window = window

    def create_entry ( self ) :
        EntryYearView.__entry = Entry( EntryYearView.__window, justify = CENTER, width = 4 )
        EntryYearView.__entry.grid( row = 1, column = 0 )

    def clean_field ( self ) :
        EntryYearView.__entry.delete(0, END)
