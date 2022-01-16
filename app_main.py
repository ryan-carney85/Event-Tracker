import tkinter as tk
from tkinter import ttk
from datetime import datetime


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        self.init_widgets()
        self.update_datetime()

    def init_widgets(self):
        self.dt_label_frame = ttk.LabelFrame(self, text="Current Date & Time")
        self.dt_label_frame.grid(row=0, column=0, padx=20, sticky="n")
        self.dt_label_frame.grid_columnconfigure(0, weight=1)
        self.dt_label_frame.grid_columnconfigure(2, weight=1)

        self.date_label = ttk.Label(self.dt_label_frame, text="date string")
        self.date_label.grid(row=0, column=1)

        self.time_label = ttk.Label(self.dt_label_frame, text="time string")
        self.time_label.grid(row=1, column=1)

        self.new_event_button = ttk.Button(self, text="New Event")
        self.new_event_button.grid(row=1, column=0, pady=2.5)

        self.edit_event_button = ttk.Button(self, text="Edit Event")
        self.edit_event_button.grid(row=2, column=0, pady=2.5)

        self.delete_event_button = ttk.Button(self, text="Delete Event")
        self.delete_event_button.grid(row=3, column=0, pady=2.5)

        self.event_log_frame = ttk.LabelFrame(self, text="Event Log")
        self.event_log_frame.grid(row=0, column=1, rowspan=4, sticky="n")

        self.event_log_text = tk.Text(self.event_log_frame, height=15, width=50)
        self.event_log_text.configure(state="disabled")
        self.event_log_text.grid(row=0, column=0, padx=3, pady=3)

    def update_datetime(self):
        date_str = datetime.strftime(datetime.now(), "%m-%d-%Y")
        time_str = datetime.strftime(datetime.now(), "%I:%M:%S %p")
        self.date_label.configure(text=date_str)
        self.time_label.configure(text=time_str)
        self.after(1000, self.update_datetime)


def main():
    root = tk.Tk()
    root.geometry("550x300")
    root.title("Event Tracker (v0.0.0)")
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    app = App(root)
    app.pack(fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
