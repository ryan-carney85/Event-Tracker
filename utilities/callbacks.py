from datetime import datetime
import tkinter as tk


def update_event_log(text_box, event_log):
    text_box.configure(state="normal")
    text_box.delete("1.0", "end")

    event_log = dict(
        sorted(
            event_log.items(),
            key=lambda item: datetime.strptime(item[1], "%m-%d-%Y"),
        )
    )

    for event_name, event_date in event_log.items():
        delta_t = datetime.strptime(event_date, "%m-%d-%Y") - datetime.now()
        str_1 = f"{event_name}: ({event_date})"
        str_2 = f"{delta_t.days} days"
        pad_size = 45 - len(str_1 + str_2)
        text_box.insert("end", f"{str_1}{'.'*pad_size}{str_2}\n")

    text_box.configure(state="disabled")
    return text_box


def rebuild_prompt_window(self, title):
    if self.child_window:
        self.win.destroy()
        self.child_window = False
    self.child_window = True
    win = tk.Toplevel(self)
    win.title(title)
    return win


def close_window(win):
    win.destroy()
