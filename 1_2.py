time_sec = int(input("Enter time in seconds"))
time_hours = time_sec // 3600
time_minutes = (time_sec - time_hours * 3600) // 60
time_seconds = time_sec - (time_hours * 3600 + time_minutes * 60)
print(f"Time format in HH:MM:SS -> {time_hours}:{time_minutes}:{time_seconds}")
