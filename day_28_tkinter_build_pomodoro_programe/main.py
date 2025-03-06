from tkinter import *
import os
import time
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
reps = 0
checks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


# functions
# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)


def count_down(count):
    # figure out the minutes and seconds
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


def reset_timer():
    global reps
    window.after_cancel(timer)
    check_marks.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# Layout
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# method to wait before doing something
# window.after(1000, say_something, 3, 4, 5)
# this is how we work with images in tkinter
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# create image variable
tomato_png = PhotoImage(file="./day_28_tkinter_build_pomodoro_programe/tomato.png")
# initialize the image
canvas.create_image(100, 112, image=tomato_png)
# add text
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)

canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=3)
button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=3)
# ✔
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
window.mainloop()
