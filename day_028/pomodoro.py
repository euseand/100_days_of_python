from tkinter import *
from math import floor
from constants import IMAGE_PATH, FONT, YELLOW, GREEN, RED, PINK, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN

reps = 0
timer = None


def start_timer():
    global timer
    if not timer:
        global reps
        reps += 1

        work_secs = WORK_MIN * 60
        sh_br_secs = SHORT_BREAK_MIN * 60
        l_br_secs = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            countdown(l_br_secs)
            title_label.config(text='Break', fg=PINK)
        elif reps % 2 != 0:
            countdown(work_secs)
            title_label.config(text='Work', fg=GREEN)
        else:
            countdown(sh_br_secs)
            title_label.config(text='Break', fg=RED)


def reset_timer():
    window.after_cancel(timer)
    tomato.itemconfig(timer_text, text='25:00')
    title_label.config(text='Timer')
    checks.config(text='')
    global reps
    reps = 0


def countdown(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    tomato.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(floor(reps / 2)):
            marks += '✔'
        checks.config(text='marks')


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=20, bg=YELLOW)

title_label = Label(text='Timer', font=FONT, fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

tomato = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file=IMAGE_PATH)
tomato.create_image(100, 115, image=tomato_png)
tomato.grid(column=1, row=1)
timer_text = tomato.create_text(100, 135, text='25:00', fill='white', font=FONT)

start_button = Button(text='Start', font=FONT, highlightthickness=0,
                      highlightbackground=YELLOW, foreground=GREEN,
                      background=YELLOW, activeforeground=PINK,
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=FONT, highlightthickness=0,
                      highlightbackground=YELLOW, foreground=GREEN,
                      background=YELLOW, activeforeground=PINK,
                      command=reset_timer)
reset_button.grid(column=2, row=2)

checks = Label(text='️', font=FONT, fg=GREEN, bg=YELLOW)
checks.grid(column=1, row=2)

window.mainloop()
