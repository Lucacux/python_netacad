# Main function is defined
def main():
    ret_hours = define_hours()
    ret_minutes = define_minutes()
    ret_event_duration = event_duration()

    total_min = total_minutes(ret_minutes, ret_event_duration)
    extra_hr = extra_hours(total_min)

    final_hour = final_estimation_hour(ret_hours, extra_hr)
    final_minute = final_estimation_minute(total_min)

    print_all_data(final_hour, final_minute)

# Functions are defined.
def define_hours():
    print("Please enter a start time (24 hours format).")
    hour = int(input())
    return hour

def define_minutes():
    print("Now enter a start time (minutes).")
    minutes = int(input())  
    return minutes

def event_duration():
    print("Finally, enter the event duration (in minutes).")
    event = int(input())  
    return event

def total_minutes(minutes, event):
    total_minutes = minutes + event
    return total_minutes

def extra_hours(total_minutes):
    extra_hours = total_minutes // 60
    return extra_hours

def final_estimation_minute(total_minutes):
    final_minutes = total_minutes % 60
    return final_minutes

def final_estimation_hour(hour, extra_hours):
    final_hour = (hour + extra_hours) % 24
    return final_hour

def print_all_data(final_hour, final_minute):
    print("The event will end at:",final_hour, "hours and", final_minute, "minutes.")
    print("24h FORMAT:",final_hour,":",final_minute)

if __name__ == "__main__":
    main()
