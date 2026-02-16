from tkinter import *

class EntryMonthView :
    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryMonthView.__window = window

    def is_valid ( self ):
        value = EntryMonthView.__entry.get()
        value = int(value)
        
        if value >= 0o1 and value <= 12 :
            EntryMonthView.__entry.configure(background = 'white')
            return True
        else:
            EntryMonthView.__entry.configure(background = 'red')
            return False

    def create_entry ( self ) :
        EntryMonthView.__entry = Entry( EntryMonthView.__window, justify = CENTER, width = 4 )
        EntryMonthView.__entry.grid( row = 2, column = 1 )

    def clean_field ( self ) :
        EntryMonthView.__entry.delete(0, END)

    def get_value (self) :
        value = EntryMonthView.__entry.get()

        return value
