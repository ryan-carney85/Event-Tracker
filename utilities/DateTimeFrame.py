from tkinter import ttk
from datetime import datetime


class DateTimeFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.create_widgets()
        self.update_datetime()

    def create_widgets(self):
        label_frame = ttk.LabelFrame(self, text="Current Date & Time")
        label_frame.grid(row=0, column=0, sticky="n")
        label_frame.columnconfigure(0, weight=1)
        label_frame.columnconfigure(1, weight=1)
        label_frame.columnconfigure(2, weight=1)

        self.date_string = ttk.Label(label_frame, text="")
        self.date_string.grid(row=0, column=1)

        self.time_string = ttk.Label(label_frame, text="")
        self.time_string.grid(row=1, column=1)

    def update_datetime(self):
        date_str = datetime.strftime(datetime.now(), "%m-%d-%Y")
        time_str = datetime.strftime(datetime.now(), "%I:%M:%S %p")
        self.date_string.configure(text=date_str)
        self.time_string.configure(text=time_str)
        self.after(1000, self.update_datetime)
