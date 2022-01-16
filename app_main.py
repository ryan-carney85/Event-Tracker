import tkinter as tk
from tkinter import ttk
from datetime import datetime


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        self.init_widgets()
        self.update_datetime()

    def init_widgets(self):
        self.text_box = ttk.LabelFrame(self, text="Current Date & Time")
        self.text_box.grid(row=0, column=0, padx=20)
        self.text_box.grid_columnconfigure(0, weight=1)
        self.text_box.grid_columnconfigure(2, weight=1)

        self.text1 = ttk.Label(self.text_box, text="Line 1")
        self.text1.grid(row=0, column=1)

        self.text2 = ttk.Label(self.text_box, text="Line 2")
        self.text2.grid(row=1, column=1)

    def update_datetime(self):
        date_str = datetime.strftime(datetime.now(), "%m-%d-%Y")
        time_str = datetime.strftime(datetime.now(), "%I:%M:%S %p")

        self.text1.configure(text=date_str)
        self.text2.configure(text=time_str)

        self.after(1000, self.update_datetime)


def main():
    root = tk.Tk()
    root.title("Event Tracker (v0.0.0)")

    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    root.geometry("350x200")
    app = App(root)
    app.pack(fill="both", expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
