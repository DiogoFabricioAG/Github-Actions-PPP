def log_current_datetime():
    from datetime import datetime
    current_datetime = datetime.now()
    with open("dia_actual.txt", "w") as file:
        file.write(f"Current date and time: {current_datetime}")

if __name__ == "__main__":
    log_current_datetime()