def latest_valid_time(unknown_time: str) -> str:
    hours, minutes = unknown_time.split(":")

    if hours[0] == "?":
        if hours[1] == "?" or hours[1] <= "3":
            symbol = "2"
        else:
            symbol = "1"
        hours = symbol + hours[1]
    if hours[1] == "?":
        if hours[0] == "2":
            symbol = "3"
        else:
            symbol = "9"
        hours = hours[0] + symbol

    if minutes[0] == "?":
        minutes = "5" + minutes[1]
    if minutes[1] == "?":
        minutes = minutes[0] + "9"

    return f"{hours}:{minutes}"


print(latest_valid_time("1?:3?"))
print(latest_valid_time("?5:?9"))
print(latest_valid_time("??:??"))
