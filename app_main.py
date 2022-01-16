import tkinter as tk
from tkinter import ttk
from datetime import datetime


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.event_log = dict()
        self.init_widgets()
        self.update_datetime()
        self.read_event_log()
        self.update_event_log()

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

        self.delete_event_button = ttk.Button(self.menu_frame, text="Delete Event")
        self.delete_event_button.grid(row=3, column=0, padx=2.5, pady=2.5)

        self.event_log_frame = ttk.LabelFrame(self, text="Event Log")
        self.event_log_frame.grid(row=0, column=1, rowspan=4, sticky="n")

        self.event_log_text = tk.Text(self.event_log_frame, height=15, width=40)
        self.event_log_text.configure(state="disabled")
        self.event_log_text.grid(row=0, column=0, padx=3, pady=3)

    def update_datetime(self):
        date_str = datetime.strftime(datetime.now(), "%m-%d-%Y")
        time_str = datetime.strftime(datetime.now(), "%I:%M:%S %p")
        self.date_label.configure(text=date_str)
        self.time_label.configure(text=time_str)
        self.after(1000, self.update_datetime)

    def add_event(self):
        win = tk.Toplevel(self)
        win.title("Enter Event Info")
        ttk.Label(win, text="Enter Event Name:").grid(
            row=0, column=0, pady=5, sticky="w"
        )
        ttk.Label(win, text="Enter Event Date:").grid(
            row=1, column=0, pady=5, sticky="w"
        )

        self.event_name = ttk.Entry(win)
        self.event_name.grid(row=0, column=1, padx=5, pady=5)

        self.event_date = ttk.Entry(win)
        self.event_date.grid(row=1, column=1, padx=5, pady=5)

        self.button = ttk.Button(
            win, text="Ok", command=lambda: self.get_new_event(win)
        )
        self.button.grid(row=2, column=1, pady=5, sticky="")

    def get_new_event(self, win):
        event_name_str = self.event_name.get()
        event_date_str = self.event_date.get()
        if event_date_str:
            self.write_to_file(event_name_str, event_date_str)
            self.event_log[event_name_str] = event_date_str
            self.update_event_log()
        win.destroy()

    def edit_event(self):
        pass

    def update_event_log(self):
        self.event_log_text.configure(state="normal")
        self.event_log_text.delete("1.0", "end")

        self.event_log = dict(
            sorted(
                self.event_log.items(),
                key=lambda item: datetime.strptime(item[1], "%m-%d-%Y"),
            )
        )

        for event_name, event_date in self.event_log.items():
            delta_t = datetime.strptime(event_date, "%m-%d-%Y") - datetime.now()
            str_1 = f"{event_name}: ({event_date})"
            str_2 = f"{delta_t.days} days"
            pad_size = 50 - len(str_1 + str_2)
            self.event_log_text.insert("end", f"{str_1}{'.'*pad_size}{str_2}\n")

        self.event_log_text.configure(state="disabled")

    def write_to_file(self, event_name, event_date):
        with open("event_log.txt", "a+") as file_obj:
            file_obj.write(f"{event_name}:{event_date}\n")

    def read_event_log(self):
        event_log = dict()
        try:
            with open("event_log.txt", "r") as file_obj:
                for line in file_obj:
                    key, value = [x.strip() for x in line.split(":")]
                    event_log[key] = value
        except FileNotFoundError:
            with open("event_log.txt", "w") as file_obj:
                pass

        self.event_log = event_log


def main():
    root = tk.Tk()
    root.geometry("500x280")
    root.resizable(False, False)
    root.title("Event Tracker (v0.0.0)")
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    app = App(root)
    app.pack(fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
