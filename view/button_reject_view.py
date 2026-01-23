from tkinter import *

class ButtonRejectView :
    __window = None
    __handler_clean_field_form = None
    __button = None

    def __init__ ( self, window, handler_clean_field_form ) :
        ButtonRejectView.__window = window
        ButtonRejectView.__handler_clean_field_form = handler_clean_field_form

    def create_button ( self ) :
        ButtonRejectView.__button = Button( 
            ButtonRejectView.__window, 
            text = 'Отклонить', 
            justify = CENTER,
            command = ButtonRejectView.__handler_clean_field_form
            )
        ButtonRejectView.__button.grid( padx = 4, pady = 4, row = 5, column = 0 )
