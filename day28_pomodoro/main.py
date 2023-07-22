import datetime
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
timer  = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer) # its used to cancel timer
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global  reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    '''
    change data type of variable by just assigning diff data type to variable its called dynamic data type
    min = 10 its integer
    hour = "09" + min  // it will give error coz both are diff data type
    min = '08' // now min type is string now 
    '''
    if count_seconds == 0:
        count_seconds == '00'

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    # use to update canvas value
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    # method that takes an amount of time it should wait and then call particular function, passing *kargs
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark +="✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=180, pady=50, bg=YELLOW)



timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=2, row=0)

# canva widget bg use as background color
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# below line used to add image / create image
photo_image = PhotoImage(file="tomato.png")
# add image to canvas with given width and height
canvas.create_image(100, 112, image= photo_image)
canvas.grid(column=2, row=1)
# to create text on canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=2)


reset_button = Button(text="Restart", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=2)

check_marks = Label( highlightthickness=0, fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=3)
#

window.mainloop()