from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    if reps % 8 == 0:
        # if it's the 8th rep, take a long break
        title.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
        count_down(long_break_secs)
    elif reps % 2 == 0:
        # if its 2nd, 4th, 6th break
        title.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
        count_down(short_break_secs)
    else:
        # if it's the 1st, 3rd, 5th, 7th rep:
        title.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    minutes = math.floor(count / 60)
    seconds = "00" if count % 60 == 0 else count % 60
    if type(seconds) == int and seconds < 10:
        seconds = f"0{seconds}"

    time = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += CHECK_MARK
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(450, 450)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
