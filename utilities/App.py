import tkinter as tk
from tkinter import ttk
from utilities.DateTimeFrame import DateTimeFrame
from utilities.MenuFrame import MenuFrame
from utilities.EventFrame import EventFrame


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("550x210")
        self.resizable(True, True)
        self.title("Event Tracker (v0.0.0)")
        self.tk.call("source", "azure.tcl")
        self.tk.call("set_theme", "dark")

        self.frame_1 = DateTimeFrame(self)
        self.frame_2 = MenuFrame(self)
        self.frame_3 = EventFrame(self)

        self.frame_1.grid(row=0, column=0, sticky="n")
        self.frame_2.grid(row=1, column=0)
        self.frame_3.grid(row=0, column=1, rowspan=2, sticky="ns")

        self.frame_2.add_button.config(command=self.add_button_callback)
        self.frame_2.edit_button.config(command=self.edit_button_callback)
        self.frame_2.delete_button.config(command=self.delete_button_callback)

    def add_button_callback(self):
        win = tk.Toplevel(self)
        win.title("Add New Event")

        ttk.Label(win, text="Enter Event Name:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        ttk.Label(win, text="Enter Event Date:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )

        self.event_name = ttk.Entry(win)
        self.event_name.grid(row=0, column=1, padx=5, pady=5)

        self.event_date = ttk.Entry(win)
        self.event_date.grid(row=1, column=1, padx=5, pady=5)

        button_1 = ttk.Button(
            win,
            text="Ok",
            style="Accent.TButton",
            command=self.get_event,
        )
        button_1.grid(row=2, column=0, pady=5, sticky="e")

        button_2 = ttk.Button(
            win,
            text="Cancel",
            command=win.destroy,
        )
        button_2.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    def get_event(self):
        event_name_str = self.event_name.get()
        event_date_str = self.event_date.get()
        self.frame_3.event_log[event_name_str] = event_date_str
        self.frame_3.update_event_log()

    def edit_button_callback(self):
        win = tk.Toplevel(self)
        win.title("Edit Event")

        self.event_picker = ttk.Combobox(
            win, state="readonly", values=[key for key in self.frame_3.event_log.keys()]
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
            command=lambda: self.edit_event(win, self.event_picker.get()),
        )
        self.button.grid(row=3, column=0, pady=5, sticky="e")

        self.cancel = ttk.Button(win, text="Cancel", command=win.destroy)
        self.cancel.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.get_event_info(0)

    def get_event_info(self, event):
        self.event_name.delete(0, "end")
        self.event_date.delete(0, "end")
        self.event_name.insert(0, self.event_picker.get())
        self.event_date.insert(0, self.frame_3.event_log[self.event_picker.get()])

    def edit_event(self, win, event):
        self.frame_3.event_log.pop(event)
        event_name_str = self.event_name.get()
        event_date_str = self.event_date.get()
        self.frame_3.event_log[event_name_str] = event_date_str
        self.frame_3.update_event_log()
        win.destroy()

    def delete_button_callback(self):
        win = tk.Toplevel(self)
        win.title("Delete Event")

        self.event_picker = ttk.Combobox(
            win, state="readonly", values=[key for key in self.frame_3.event_log.keys()]
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
            command=lambda: self.delete_event(win, self.event_picker.get()),
        )

        self.button.grid(row=1, column=0, padx=5, pady=5, sticky="")

        self.cancel = ttk.Button(win, text="Cancel", command=win.destroy)
        self.cancel.grid(row=1, column=1, padx=5, pady=5)

    def delete_event(self, win, event):
        self.frame_3.event_log.pop(event)
        self.frame_3.update_event_log()
        win.destroy()
