import math
from tkinter import *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps

    reps = 0
    title_label.config(text="Timer")
    canvas.itemconfig(timer_title, text="00:00")
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_time = WORK_MIN * 60
    shortbreak_time = SHORT_BREAK_MIN * 60
    longbreak_time = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(longbreak_time)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(shortbreak_time)
        title_label.config(text="Break", fg=PINK)
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown(work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    completed = math.floor(reps / 2)
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"


    canvas.itemconfig(timer_title, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()

        checkmark.config(text=f"{'✔ '* completed}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)



tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112 , image=tomato, )
timer_title = canvas.create_text(103, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1)


start_button = Button(text="start", command=start_timer)
reset_button = Button(text="reset", command=reset)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

checkmark = Label( fg=GREEN, bg=YELLOW, font=(FONT_NAME, 13, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()