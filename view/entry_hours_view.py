from tkinter import *

class EntryHoursView :
    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryHoursView.__window = window

    def create_entry ( self ) :
        EntryHoursView.__entry = Entry( EntryHoursView.__window, justify = CENTER, width = 4 )
        EntryHoursView.__entry.grid( row = 3, column = 0 )

    def clean_field ( self ) :
        EntryHoursView.__entry.delete(0, END)

    def get_value (self) :
        value = EntryHoursView.__entry.get()

        return value