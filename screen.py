import ctypes
import datetime
import tkinter as tk

# Set the desired brightness levels for different times of day
brightness_levels = {
    "morning": 80,
    "afternoon": 100,
    "evening": 60,
    "night": 30
}

# Set the time range for reducing screen time activity at night
night_start_time = datetime.time(22, 0)  # 10:00 PM
night_end_time = datetime.time(6, 0)  # 6:00 AM

# Get the current time
current_time = datetime.datetime.now().time()

# Define the necessary Windows API constants and functions
MONITOR_BRIGHTNESS = 0x00000002
HWND_BROADCAST = 0xFFFF

SendMessageTimeout = ctypes.windll.user32.SendMessageTimeoutW
SendMessageTimeout.restype = ctypes.c_uint
SendMessageTimeout.argtypes = [
    ctypes.c_ulong, ctypes.c_uint, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_uint,
    ctypes.c_uint, ctypes.POINTER(ctypes.c_ulong)
]

# Function to adjust screen brightness using the Windows API
def set_brightness(brightness):
    # Adjust brightness using the Windows API
    SendMessageTimeout(
        HWND_BROADCAST, 0x0112, MONITOR_BRIGHTNESS, brightness, 2, 5000, None
    )

# Function to cancel the brightness adjustment
def cancel_adjustment():
    root.destroy()

# Create a GUI window
root = tk.Tk()
root.title("Brightness Adjustment")

# Create a label with the notification message
notification_label = tk.Label(root, text="Screen brightness is being adjusted.")
notification_label.pack(pady=20)

# Create a cancel button
cancel_button = tk.Button(root, text="Cancel", command=cancel_adjustment)
cancel_button.pack()

# Get the current brightness level based on the time of day
if current_time < night_start_time or current_time > night_end_time:
    # Adjust brightness based on the time of day
    if current_time < datetime.time(10, 0):  # Morning
        brightness_level = brightness_levels["morning"]
    elif current_time < datetime.time(16, 0):  # Afternoon
        brightness_level = brightness_levels["afternoon"]
    elif current_time < datetime.time(20, 0):  # Evening
        brightness_level = brightness_levels["evening"]
    else:  # Night
        brightness_level = brightness_levels["night"]

    # Calculate the new brightness value
    new_brightness = int(brightness_level * 65535 / 100)

    # Set the new brightness level
    set_brightness(new_brightness)
else:
    # Reduce screen time activity at night
    # Add code to perform actions to reduce screen time activity, such as displaying a warning message, enabling night mode, etc.
    notification_label.config(text="It's late at night. Consider reducing your screen time activity.")

# Start the GUI event loop
root.mainloop()
