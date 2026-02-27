import re

from tkinter import *

class EntryHoursView :
    __regex = re.compile(r'^0[0-9]$|^1\d$|^2[0-3]$')

    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryHoursView.__window = window

    def is_valid ( self ):
        value = EntryHoursView.__entry.get()[:2]
        
        if EntryHoursView.__regex.match(value) != None :
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
        value = EntryHoursView.__entry.get()[:2]

        return value