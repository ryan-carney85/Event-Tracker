import tkinter as tk
from tkinter import ttk


class MenuFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.create_widgets()

    def create_widgets(self):
        label_frame = ttk.LabelFrame(self, text="Menu")
        label_frame.grid(row=0, column=0, padx=2.5, pady=2.5, sticky="n")

        self.add_button = ttk.Button(
            label_frame,
            text="Add Event",
        )
        self.add_button.grid(row=0, column=0, padx=2.5, pady=2.5)

        self.edit_button = ttk.Button(label_frame, text="Edit Event")
        self.edit_button.grid(row=1, column=0, padx=2.5, pady=2.5)

        self.delete_button = ttk.Button(label_frame, text="Delete Event")
        self.delete_button.grid(row=2, column=0, padx=2.5, pady=2.5)
