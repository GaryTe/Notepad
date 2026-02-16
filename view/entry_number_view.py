from tkinter import *

class EntryNumberView :
    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryNumberView.__window = window

    def is_valid ( self ):
        value = EntryNumberView.__entry.get()
        value = int(value)
        
        if value >= 0o1 and value <= 31 :
            EntryNumberView.__entry.configure(background = 'white')
            return True
        else:
            EntryNumberView.__entry.configure(background = 'red')
            return False

    def create_entry ( self ) :
        EntryNumberView.__entry = Entry( EntryNumberView.__window, justify = CENTER, width = 4 )
        EntryNumberView.__entry.grid( row = 2, column = 2 )

    def clean_field ( self ) :
        EntryNumberView.__entry.delete(0, END)

    def get_value (self) :
        value = EntryNumberView.__entry.get()

        return value
