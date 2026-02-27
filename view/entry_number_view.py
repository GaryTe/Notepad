import re

from tkinter import *

class EntryNumberView :
    __regex = re.compile(r'^0[1-9]$|^1\d$|^2\d$|^3[0-1]$')

    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryNumberView.__window = window

    def is_valid ( self ):
        value = EntryNumberView.__entry.get()[:2]
        
        if EntryNumberView.__regex.match(value) != None :
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
        value = EntryNumberView.__entry.get()[:2]

        return value
