from tkinter import *

class EntryMonthView :
    __window = None
    __entry = None

    def __init__ ( self, window ) :
        EntryMonthView.__window = window

    def create_entry ( self ) :
        EntryMonthView.__entry = Entry( EntryMonthView.__window, justify = CENTER, width = 4 )
        EntryMonthView.__entry.grid( row = 1, column = 1 )

    def clean_field ( self ) :
        EntryMonthView.__entry.delete(0, END)

    def get_value (self) :
        value = EntryMonthView.__entry.get()

        return value
