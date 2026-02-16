import threading

from time import time, localtime, strftime, sleep
import time as t
from datetime import datetime
from tkinter.messagebox import showinfo

class EventNotificationModel :
    __tasks_list = []
    is_start_notification = False


    def __call_task (self, tasks_list) :
        EventNotificationModel.is_start_notification = True

        while len(tasks_list) >= 1 :
        
            date_time_list = datetime.today()
            time_sleep = 60 - date_time_list.second

            sleep(time_sleep)
            struct_time = localtime(t.time())
            time = f'{strftime('%H', struct_time)}:{strftime('%M', struct_time)}'

            for task in tasks_list :
                date_time = task.split('/')[0].split(' ')[1]

                if date_time == time :
                    threading.Thread(
                        target=showinfo, 
                        args=('Сообщение', task),  
                        name=f'EventNotificationModel_showinfo_{date_time}'
                        ).start()
                    tasks_list.remove(task)

        EventNotificationModel.is_start_notification = False
 
    def __get_task (self, date, time) :
        try:
            with open('data_note.txt', 'r') as data_tasts_list :
                for task in data_tasts_list :
                    data_task = task.split('/')[0]

                    date_task = data_task.split(' ')[0]
                    time_task = data_task.split(' ')[1]

                    if date == date_task and time_task >= time :
                        EventNotificationModel.__tasks_list.append(task)
        except FileNotFoundError :
            return
        else:
            if len(EventNotificationModel.__tasks_list) > 0 :
                self.__call_task(EventNotificationModel.__tasks_list)

    def __get_date_time (self) :
        struct_time = localtime(time())
        date_task = f'{strftime('%Y', struct_time)}.{strftime('%m', struct_time)}.{strftime('%d', struct_time)}'
        time_task = f'{strftime('%H', struct_time)}:{strftime('%M', struct_time)}'

        self.__get_task(date_task, time_task)

    def start_notification (self, text = None) :
        if not EventNotificationModel.is_start_notification :
            threading.Thread( 
            target = self.__get_date_time,  
            name = 'EventNotificationModel_start_notification' 
            ).start()
        else:
            EventNotificationModel.__tasks_list.append(text)