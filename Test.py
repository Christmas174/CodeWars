def format_duration(seconds):
    date = {"year": 31536000, "day": 86400, "hour": 3600, "minute": 60, "second": 1}
    matter_of_seconds = []

    if not seconds:
        return ("now")

    for key, value in date.items():
        whole = seconds // value
        if whole > 1:
            matter_of_seconds.append(f'{whole} {key}s')
        elif whole == 1:
            matter_of_seconds.append(f'{whole} {key}')
        seconds -= whole * value
    if len(matter_of_seconds) > 1:
      matter_of_seconds = ", ".join(matter_of_seconds[:-1]) + " and " + matter_of_seconds[-1]
    else:
        matter_of_seconds = matter_of_seconds[0].split(' ')

    return matter_of_seconds

