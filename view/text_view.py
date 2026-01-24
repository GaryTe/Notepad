from tkinter import *
from tkinter import ttk

class TextView :
    __text = None

    def create_text ( self ) :
        TextView.__text = Text( bd = 3, height = 4, width = 24, wrap = 'word' )
        TextView.__text.grid( row = 4, columnspan = 3, pady = 4 )

        ys = ttk.Scrollbar( orient = "vertical", command = TextView.__text.yview )
        ys.place( height = 70, x = 225, y = 95 )

        TextView.__text["yscrollcommand"] = ys.set

    def clean_field ( self ) :
        TextView.__text.delete("1.0", END)

    def get_text (self) :
        text = TextView.__text.get("1.0", "end")
        
        return text
