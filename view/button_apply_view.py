from tkinter import *
from tkinter.messagebox import showwarning

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
        ButtonApplyView.__button.grid( padx = 10, pady = 4, row = 6, column = 1 )

    def __write_data ( self ) :
        data = ButtonApplyView.__handler_writing_text()

        if not data :
            showwarning('Сообщение', 'Исправьте значение в поле, которое выделено красным цветом.')
            return

        with open('data_note.txt', 'a') as file :
            file.write(data)

        ButtonApplyView.__handler_clean_field_form(data, is_flag = True)
