import re

from tkinter import *

class EntryMonthView :
    __regex = re.compile(r'^0[1-9]$|10|11|12')

    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryMonthView.__window = window

    def is_valid ( self ):
        value = EntryMonthView.__entry.get()[:2]
        
        if EntryMonthView.__regex.match(value) != None :
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
        value = EntryMonthView.__entry.get()[:2]

        return value
