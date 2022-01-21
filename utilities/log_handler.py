def read_event_log():
    event_log = dict()
    try:
        with open("event_log.txt", "r") as file_obj:
            for line in file_obj:
                key, value = [x.strip() for x in line.split(":")]
                event_log[key] = value
    except FileNotFoundError:
        with open("event_log.txt", "w") as file_obj:
            pass

    return event_log


def write_event_log(event_log):
    with open("event_log.txt", "w") as file_obj:
        for event_name, event_date in event_log.items():
            file_obj.write(f"{event_name}:{event_date}\n")
