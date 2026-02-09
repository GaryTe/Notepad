from tkinter import *

class ButtonApplyView :
    __window = None
    __handler_writing_text = None
    __handler_clean_field_form = None
    __button = None

    def __init__ ( self, window, handler_writing_text, handler_clean_field_form ) :
        ButtonApplyView.__window = window
        ButtonApplyView.__handler_writing_text = handler_writing_text
        ButtonApplyView.__handler_clean_field_form = handler_clean_field_form

    def create_button ( self ) :
        ButtonApplyView.__button = Button( 
            ButtonApplyView.__window, 
            text = 'Применить', 
            justify = CENTER,
            command = self.__write_data
            )
        ButtonApplyView.__button.grid( padx = 10, pady = 4, row = 5, column = 1 )

    def __write_data ( self ) :
        data = ButtonApplyView.__handler_writing_text()

        with open('data_note.txt', 'a') as file :
            file.write(data)

        ButtonApplyView.__handler_clean_field_form(data, is_flag = True)
