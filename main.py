from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
num_of_ticks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global repetitions, num_of_ticks
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Zegar", fg=GREEN)
    tick.config(text="")
    repetitions = 0
    num_of_ticks = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetitions
    repetitions += 1
    if repetitions % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text=f"Przerwa", fg=RED, font=(FONT_NAME, 28, "bold"))
    elif repetitions % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text=f"Przerwa", fg=PINK, font=(FONT_NAME, 28, "bold"))
    else:
        count_down(WORK_MIN * 60)
        title.config(text=f"Praca", fg=GREEN, font=(FONT_NAME, 32, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global num_of_ticks
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if repetitions % 2 == 0:
            num_of_ticks += "✔️"
            tick.config(text=num_of_ticks)
        if repetitions % 8 == 0:
            num_of_ticks = ""
            tick.config(text=num_of_ticks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomidorek")
tomato_bg = PhotoImage(file="./tomato.png")
window.config(padx=100, pady=50, bg=YELLOW)
window.iconphoto(False, tomato_bg)
window.resizable(False, False)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_bg)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Label timer
title = Label()
title.config(padx=50, pady=10, fg=GREEN, text="Zegar", bg=YELLOW, font=(FONT_NAME, 32, "bold"))
title.grid(column=1, row=0)

# Button start
start = Button()
start.config(text="Start", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# Button reset
reset = Button()
reset.config(text="Reset", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

# Label ✔️
tick = Label()
tick.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
tick.grid(column=1, row=3)
window.mainloop()
