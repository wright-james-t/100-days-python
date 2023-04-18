from tkinter import *
from playsound import playsound
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
FONT_NAME = "Comic Sans"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# HOUR = 60
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
HOUR = 1

reps = 0
current_bg_color = BLACK
current_items = []
check_mark_count = []
timer = None
alert_path = Path("alert.wav")
pm_count = 0


def update_bg_colors():
    for item in current_items:
        item.config(bg=current_bg_color)

def alert():
    playsound("alert.wav")


def start_reset():
    if reps != 0:
        reset_timer()
    start_timer()


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_mark_count
    global reps
    global current_bg_color
    window.after_cancel(timer)
    current_bg_color = BLACK
    update_bg_colors()
    check_mark_count = []
    check_mark.grid(column=2, row=3)
    reps = 0
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global current_bg_color
    work_sec = WORK_MIN * HOUR
    short_break_sec = SHORT_BREAK_MIN * HOUR
    long_break_sec = LONG_BREAK_MIN * HOUR

    if reps == 8:
        countdown(long_break_sec)
        timer_label.config(text="Break")
        current_bg_color = RED
        update_bg_colors()
    elif reps % 2:
        countdown(short_break_sec)
        timer_label.config(text="Break")
        current_bg_color = PINK
        update_bg_colors()
    else:
        countdown(work_sec)
        timer_label.config(text="Work")
        check_mark_count.append("✅")
        current_bg_color = BLACK
        update_bg_colors()
    reps += 1
    print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    global check_mark_count
    global timer
    count_min = '{:02d}'.format(int(count / 60))
    count_sec = '{:02d}'.format(count % 60)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    elif count == 0:
        canvas.itemconfig(timer_text, text=f"00:00")
        timer = window.after(1000, countdown, count - 1)
    else:
        alert()
        start_timer()
        if reps % 2 == 0:
            check_mark.config(text=(' '.join(check_mark_count)))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=BLACK)
current_items.append(window)

canvas = Canvas(width=200, height=224, bg=BLACK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
current_items.append(canvas)

timer_label = Label(text="Timer", fg="white", bg=BLACK, font=(FONT_NAME, 35))
timer_label.grid(column=2, row=1)
current_items.append(timer_label)

start_button = Button(text="Start", command=start_reset)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

check_mark = Label(fg=GREEN, bg=BLACK)
check_mark.grid(column=2, row=3)
current_items.append(check_mark)


window.mainloop()