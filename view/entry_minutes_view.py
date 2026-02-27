import re

from tkinter import *

class EntryMinutesView :
    __regex = re.compile(r'^0[0-9]$|^1\d$|^2\d$|^3\d$|^4\d$|^5\d$|^60$')

    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryMinutesView.__window = window

    def is_valid ( self ):
        value = EntryMinutesView.__entry.get()[:2]
        
        if EntryMinutesView.__regex.match(value) != None :
            EntryMinutesView.__entry.configure(background = 'white')
            return True
        else:
            EntryMinutesView.__entry.configure(background = 'red')
            return False

    def create_entry ( self ) :
        EntryMinutesView.__entry = Entry( EntryMinutesView.__window, justify = CENTER, width = 4 )
        EntryMinutesView.__entry.grid( row = 4, column = 1 )

    def clean_field ( self ) :
        EntryMinutesView.__entry.delete(0, END)

    def get_value (self) :
        value = EntryMinutesView.__entry.get()[:2]

        return value
