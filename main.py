import pywhatkit
import time
from datetime import datetime, timedelta
import pyautogui

def send_message_interval(phone_number, message, interval_minutes):
    # Send the first message immediately
    pywhatkit.sendwhatmsg_instantly(phone_number, message)
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    print(f"First message sent immediately at {datetime.now().strftime('%H:%M')}")


    while True:
        next_send_time = datetime.now() + timedelta(minutes=interval_minutes)

        send_hour = next_send_time.hour
        send_minute = next_send_time.minute

        # Wait until the next send time
        time.sleep((next_send_time - datetime.now()).total_seconds())

        # Adjust the minute value to stay within 0-59 range
        adjusted_send_minute = (send_minute + 1) % 60
        adjusted_send_hour = send_hour if adjusted_send_minute > send_minute else (send_hour + 1) % 24

        # Send the message
        pywhatkit.sendwhatmsg(phone_number, message, adjusted_send_hour, adjusted_send_minute)
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'w')

        # Confirmation message
        print(f"Message sent at {adjusted_send_hour:02d}:{adjusted_send_minute:02d}")

# Phone number and message

phone_number = "+880**********" #Country Code and number
message = "Testing code."
interval_minutes = 1

# Calling the function
send_message_interval(phone_number, message, interval_minutes)




