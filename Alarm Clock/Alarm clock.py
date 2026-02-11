import time
import time
import datetime
import winsound

print("===== ALARM CLOCK =====")

alarm_time = input("Enter alarm time (HH:MM:SS): ")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)

    if current_time == alarm_time:
        print("⏰ WAKE UP!")
        winsound.Beep(1000, 3000) 
        break

    time.sleep(1)
