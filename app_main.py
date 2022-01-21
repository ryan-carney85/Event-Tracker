import tkinter as tk
from utilities.App import App


def main():
    root = tk.Tk()
    root.geometry("550x280")
    root.resizable(False, False)
    root.title("Event Tracker (v0.0.0)")
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    app = App(root)
    app.pack(fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
