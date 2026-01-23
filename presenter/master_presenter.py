from tkinter import *

from view.label_year_view import *
from view.label_month_view import *
from view.label_number_view import *
from view.entry_year_view import *
from view.entry_month_view import *
from view.entry_number_view import *
from view.label_hours_view import *
from view.label_minutes_view import *
from view.entry_hours_view import *
from view.entry_minutes_view import *
from view.text_view import *
from view.button_reject_view import *
from view.button_apply_view import *

class MasterPresenter :
    __window = Tk()
    __label_year_view = LabelYearView( __window )
    __label_month_view = LabelMonthView( __window )
    __label_number_view = LabelNumberView( __window )
    __entry_year_view = EntryYearView( __window )
    __entry_month_view = EntryMonthView( __window )
    __entry_number_view = EntryNumberView( __window )
    __label_hours_view = LabelHoursView( __window )
    __label_minutes_view = LabelMinutesView( __window )
    __entry_hours_view = EntryHoursView( __window )
    __entry_minutes_view = EntryMinutesView( __window )
    __text_view = TextView()
    __button_reject_view = None
    __button_apply_view = ButtonApplyView( __window )

    def __init__( self ):
        MasterPresenter.__button_reject_view = ButtonRejectView( 
            MasterPresenter.__window,
            self.handler_clean_field_form
            )

    def initialization ( self ) :
        MasterPresenter.__window.title( 'Блокнот' )
        MasterPresenter.__window.resizable( 0, 0 )

        MasterPresenter.__label_year_view.create_label()
        MasterPresenter.__label_month_view.create_label()
        MasterPresenter.__label_number_view.create_label()

        MasterPresenter.__entry_year_view.create_entry()
        MasterPresenter.__entry_month_view.create_entry()
        MasterPresenter.__entry_number_view.create_entry()

        MasterPresenter.__label_hours_view.create_label()
        MasterPresenter.__label_minutes_view.create_label()

        MasterPresenter.__entry_hours_view.create_entry()
        MasterPresenter.__entry_minutes_view.create_entry()

        MasterPresenter.__text_view.create_text()

        MasterPresenter.__button_reject_view.create_button()
        MasterPresenter.__button_apply_view.create_button()
        
        MasterPresenter.__window.mainloop()

    def handler_clean_field_form ( self ) :
        MasterPresenter.__entry_year_view.clean_field()
        MasterPresenter.__entry_month_view.clean_field()
        MasterPresenter.__entry_number_view.clean_field()

        MasterPresenter.__entry_hours_view.clean_field()
        MasterPresenter.__entry_minutes_view.clean_field()

        MasterPresenter.__text_view.clean_field()