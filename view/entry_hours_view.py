from tkinter import *

class EntryHoursView :
    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryHoursView.__window = window

    def is_valid ( self ):
        value = EntryHoursView.__entry.get()
        value = int(value)
        
        if value >= 00 and value <= 23 :
            EntryHoursView.__entry.configure(background = 'white')
            return True
        else:
            EntryHoursView.__entry.configure(background = 'red')
            return False

    def create_entry ( self ) :
        EntryHoursView.__entry = Entry( EntryHoursView.__window, justify = CENTER, width = 4 )
        EntryHoursView.__entry.grid( row = 4, column = 0 )

    def clean_field ( self ) :
        EntryHoursView.__entry.delete(0, END)

    def get_value (self) :
        value = EntryHoursView.__entry.get()

        return value