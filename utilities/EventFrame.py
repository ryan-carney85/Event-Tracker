import tkinter as tk
from tkinter import ttk
from datetime import datetime
from utilities import log_handler as logger
from utilities.DateTimeFrame import DateTimeFrame


class EventFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.create_widgets()
        self.event_log = logger.read_event_log()
        self.update_event_log()

    def create_widgets(self):
        label_frame = ttk.LabelFrame(self, text="Event Log")
        label_frame.grid(row=0, column=1, rowspan=2)

        self.text_box = tk.Text(label_frame, height=10, width=45)
        self.text_box.grid(row=0, column=0, padx=3, pady=3)

    def update_event_log(self):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", "end")

        event_log = dict(
            sorted(
                self.event_log.items(),
                key=lambda item: datetime.strptime(item[1], "%m-%d-%Y"),
            )
        )

        for event_name, event_date in event_log.items():
            delta_t = datetime.strptime(event_date, "%m-%d-%Y") - datetime.now()
            str_1 = f"{event_name}: ({event_date})"
            str_2 = f"{delta_t.days} days"
            pad_size = 45 - len(str_1 + str_2)
            self.text_box.insert("end", f"{str_1}{'.'*pad_size}{str_2}\n")

        self.text_box.configure(state="disabled", font=("Courier", 10))
        logger.write_event_log(event_log)
