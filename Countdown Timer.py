import tkinter as tk
from tkinter import messagebox
import time

def countdown(total_seconds):
    while total_seconds >= 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label['text'] = time_format
        root.update()
        time.sleep(1)
        total_seconds -= 1
    messagebox.showinfo("Time's up!", "The countdown has ended!")

def start_timer():
    try:
        # Get the value from the entry widget, convert to seconds and start the countdown
        total_seconds = int(entry.get()) * 60
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a number")

# Initialize the main window
root = tk.Tk()
root.title("Countdown Timer by karthik")
root.geometry("300x200")

# Create a label to display the countdown
label = tk.Label(root, font=('Helvetica', 48))
label.pack(pady=20)

# Create an entry widget to enter the countdown time in minutes
entry = tk.Entry(root, justify='center', font=('Helvetica', 24))
entry.pack(pady=20)
entry.focus()

# Create a button to start the countdown
start_button = tk.Button (root, text="START", command=start_timer)
start_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()


