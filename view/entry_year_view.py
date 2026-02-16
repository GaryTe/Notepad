from tkinter import *

class EntryYearView :
    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryYearView.__window = window

    def is_valid ( self ):
        value = EntryYearView.__entry.get()
        
        if len(value) == 4:
            EntryYearView.__entry.configure(background = 'white')
            return True
        else:
            EntryYearView.__entry.configure(background = 'red')
            return False

    def create_entry ( self ) :
        EntryYearView.__entry = Entry( EntryYearView.__window, justify = CENTER, width = 4)
        EntryYearView.__entry.grid( row = 2, column = 0 )

    def clean_field ( self ) :
        EntryYearView.__entry.delete(0, END)

    def get_value ( self ) :
        value = EntryYearView.__entry.get()
        
        return value
