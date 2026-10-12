import customtkinter as ctk
from plyer import notification

timer_running = False
time_left = 25 * 60  # 25 minutes in seconds

def update_timer():
    global time_left, timer_running
    if timer_running and time_left > 0:
        minutes = time_left // 60
        seconds = time_left % 60
        time_label.configure(text=f"{minutes:02d}:{seconds:02d}")
        time_left -= 1
        app.after(1000, update_timer)
        
    elif time_left == 0 and timer_running: # Added 'and timer_running' to prevent spam
        timer_running = False
        time_label.configure(text="00:00")
        
        # Send the native desktop notification
        notification.notify(
            title="Pomodoro Complete!",
            message="Great focus. Time to take a 5-minute break.",
            app_name="Pomodoro Timer",
            timeout=10  # Notification stays for 10 seconds
        )

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        update_timer()

def pause_timer():
    global timer_running
    timer_running = False

def reset_timer():
    global timer_running, time_left
    timer_running = False
    time_left = 25 * 60
    time_label.configure(text="25:00")

# Modern dark mode theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the main window
app = ctk.CTk()
app.geometry("300x350")
app.title("Pomodoro Timer")

# The Clock Display
time_label = ctk.CTkLabel(app, text="25:00", font=("Helvetica", 60, "bold"))
time_label.pack(pady=40)

# The Controls
start_btn = ctk.CTkButton(app, text="Start", command=lambda: start_timer())
start_btn.pack(pady=10)

pause_btn = ctk.CTkButton(app, text="Pause", command=lambda: pause_timer())
pause_btn.pack(pady=10)

reset_btn = ctk.CTkButton(app, text="Reset", command=lambda: reset_timer())
reset_btn.pack(pady=10)

app.mainloop()