import tkinter as tk
import tool_tip
from tkinter import ttk
from datetime import datetime

from utilities import log_handler as logger
from utilities import callbacks

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.child_window = False
        self.init_widgets()
        self.update_datetime()
        self.event_log = logger.read_event_log()
        self.event_log_text = callbacks.update_event_log(self.event_log_text, self.event_log)

    def init_widgets(self):
        self.dt_label_frame = ttk.LabelFrame(self, text="Current Date & Time")
        self.dt_label_frame.grid(row=0, column=0, padx=20, sticky="n")
        self.dt_label_frame.grid_columnconfigure(0, weight=1)
        self.dt_label_frame.grid_columnconfigure(2, weight=1)

        self.date_label = ttk.Label(self.dt_label_frame, text="date string")
        self.date_label.grid(row=0, column=1)

        self.time_label = ttk.Label(self.dt_label_frame, text="time string")
        self.time_label.grid(row=1, column=1)

        self.menu_frame = ttk.LabelFrame(self, text="Menu")
        self.menu_frame.grid(row=1, column=0)

        self.new_event_button = ttk.Button(
            self.menu_frame, text="New Event", command=self.add_event
        )
        self.new_event_button.grid(row=1, column=0, padx=2.5, pady=2.5)

        self.edit_event_button = ttk.Button(
            self.menu_frame, text="Edit Event", command=self.edit_event
        )
        self.edit_event_button.grid(row=2, column=0, padx=2.5, pady=2.5)

        self.delete_event_button = ttk.Button(
            self.menu_frame, text="Delete Event", command=self.delete_event
        )
        self.delete_event_button.grid(row=3, column=0, padx=2.5, pady=2.5)

        self.event_log_frame = ttk.LabelFrame(self, text="Event Log")
        self.event_log_frame.grid(row=0, column=1, rowspan=4, sticky="n")

        self.event_log_text = tk.Text(self.event_log_frame, height=15, width=45, font =("Courier", 10))
        self.event_log_text.configure(state="disabled")
        self.event_log_text.grid(row=0, column=0, padx=3, pady=3)

    def update_datetime(self):
        date_str = datetime.strftime(datetime.now(), "%m-%d-%Y")
        time_str = datetime.strftime(datetime.now(), "%I:%M:%S %p")
        self.date_label.configure(text=date_str)
        self.time_label.configure(text=time_str)
        self.after(1000, self.update_datetime)


    def add_event(self):        
        win = callbacks.rebuild_prompt_window(self, "Enter Event Info")
        ttk.Label(win, text="Enter Event Name:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        ttk.Label(win, text="Enter Event Date:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        self.win = win
        self.event_name = ttk.Entry(win)
        self.event_name.grid(row=0, column=1, padx=5, pady=5)

        self.event_date = ttk.Entry(win)
        tool_tip.create(self.event_date, "mm-dd-yyyy")
        self.event_date.grid(row=1, column=1, padx=5, pady=5)

        self.button = ttk.Button(
            win,
            text="Ok",
            style="Accent.TButton",
            command=lambda: self.manage_event_callback(win, mode='new'),
        )
        self.button.grid(row=2, column=0, pady=5, sticky="e")

        self.cancel = ttk.Button(
            win, text="Cancel", command=lambda: callbacks.close_window(win)
        )
        self.cancel.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    def edit_event(self):
        win = callbacks.rebuild_prompt_window(self, "Enter Event Info")        

        self.event_picker = ttk.Combobox(
            win, state="readonly", values=[key for key in self.event_log.keys()]
        )
        self.event_picker.current(0)
        self.event_picker.bind("<<ComboboxSelected>>", self.get_event_info)
        self.event_picker.grid(row=0, column=0, padx=5, pady=5)

        ttk.Label(win, text="Enter Event Name:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        ttk.Label(win, text="Enter Event Date:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e"
        )
        self.win = win
        self.event_name = ttk.Entry(win)
        self.event_name.grid(row=1, column=1, padx=5, pady=5)

        self.event_date = ttk.Entry(win)
        self.event_date.grid(row=2, column=1, padx=5, pady=5)

        self.button = ttk.Button(
            win,
            text="Ok",
            style="Accent.TButton",
            command=lambda: self.manage_event_callback(win, newkey=self.event_picker.get(), mode='edit'),
        )
        self.button.grid(row=3, column=0, pady=5, sticky="e")

        self.cancel = ttk.Button(
            win, text="Cancel", command=lambda: callbacks.close_window(win)
        )
        self.cancel.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.get_event_info(0)


    def delete_event(self):
        win = callbacks.rebuild_prompt_window(self, "Enter Event Info")       

        self.event_picker = ttk.Combobox(
            win, state="readonly", values=[key for key in self.event_log.keys()]
        )
        self.event_picker.current(0)
        self.event_picker.grid(
            row=0, column=0, columnspan=2, padx=2.5, pady=2.5, sticky="we"
        )
        self.win = win
        self.button = ttk.Button(
            win,
            text="Delete",
            style="Accent.TButton",
            command=lambda: self.manage_event_callback(
                win, newkey=self.event_picker.get(), mode='delete'
            ),
        )
        self.button.grid(row=1, column=0, padx=5, pady=5, sticky="")

        self.cancel = ttk.Button(
            win, text="Cancel", command=lambda: callbacks.close_window(win)
        )
        self.cancel.grid(row=1, column=1, padx=5, pady=5)

    def get_event_info(self, event):
        self.event_name.delete(0, "end")
        self.event_date.delete(0, "end")
        self.event_name.insert(0, self.event_picker.get())
        self.event_date.insert(0, self.event_log[self.event_picker.get()])

    def validate_date_string(self, date_string):
        new_date_string = ""
        try:
           new_date_string = datetime.strptime(date_string, "%m-%d-%Y")
        except:
            print("bad date string format \nShould be 'mm-dd-yy'")
            new_date_string = "01-01-0001"
        return new_date_string

    def manage_event_callback(self, win, newkey=None, mode=None):
        match mode:
            case 'new':
                event_name_str = self.event_name.get()
                event_date_str = self.event_date.get()
                # event_date_str = self.validate_date_string(event_date_str)
                self.event_log[event_name_str] = event_date_str
            case 'edit':
                self.event_log.pop(newkey)
                event_name_str = self.event_name.get()
                event_date_str = self.event_date.get()
                # event_date_str = self.validate_date_string(event_date_str)
                self.event_log[event_name_str] = event_date_str
            case 'delete':
                self.event_log.pop(newkey)
            case _:
                pass
        logger.write_event_log(self.event_log)
        self.event_log_text = callbacks.update_event_log(self.event_log_text, self.event_log)
        callbacks.close_window(win)