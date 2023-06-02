def seconds_to_hour_minute_second(seconds):
    # Convert seconds to hours, minutes and remaining seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format as a string
    if hours > 0:
        return f"{int(hours)}小时{int(minutes)}分钟"
    elif minutes > 0:
        return f"{int(minutes)}分钟"
    else:
        return f"{int(seconds)}秒"
