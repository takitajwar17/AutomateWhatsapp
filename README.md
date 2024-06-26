## Automated WhatsApp Message Sender

### Overview

This script allows you to send WhatsApp messages at regular intervals using the `pywhatkit` library and `pyautogui`. It sends the first message immediately and then continues to send messages at specified time intervals.

### Requirements

Before running the script, ensure you have the following packages installed:

- `pywhatkit`
- `pyautogui`
- `datetime`
- `time`

You can install the necessary packages using `pip`:

```bash
pip install pywhatkit pyautogui
```

### Instructions

1. **Phone Number and Message Setup:**
   Replace the placeholder phone number and message with your desired values. The phone number should include the country code.

   ```python
   phone_number = "+880**********"  # Replace with the actual country code and phone number
   message = "Testing code."  # Replace with your desired message
   interval_minutes = 1  # Replace with your desired interval in minutes
   ```

2. **Keeping WhatsApp Web Logged In:**
   Ensure that you are logged into WhatsApp Web on your browser. The script relies on the WhatsApp Web interface to send messages.

3. **Running the Script:**
   Save the script to a Python file, e.g., `whatsapp_message_sender.py`. Open a terminal and navigate to the directory where the script is saved. Run the script using:

   ```bash
   python whatsapp_message_sender.py
   ```
