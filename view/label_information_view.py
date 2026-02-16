from tkinter import *

text_label = '''
В поле «год» введите четырехзначное число, например, 2026.
В поле «месяц» укажите двухзначное число от 01 до 12.
В поле «число» введите двузначное число от 01 до 31.
В поле «часы» введите двузначное число от 00 до 23.
В поле «минуты» введите двузначное число от 01 до 59.
'''

class LabelInformationView :
    __window = None
    __label = None

    def __init__ ( self, window ) :
        LabelInformationView.__window = window

    def create_label ( self ) :
        LabelInformationView.__label = Label( 
            LabelInformationView.__window, 
            text = text_label, 
            font=(None, 7), 
            foreground = 'red' 
            )
        LabelInformationView.__label.grid( row = 0, columnspan = 3 )
