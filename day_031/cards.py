import tkinter as tk
from random import choice


FONT = ('Roboto', 20, 'bold')
WORDS = []
curr_word = None


def init():
    global WORDS
    with open('french_words.csv', 'r') as f:
        WORDS += [{'fr': word.strip().split(',')[0], 'eng': word.strip().split(',')[1]} for word in f.readlines()]


def next_card():
    if len(WORDS) > 0:
        global curr_word
        curr_word = choice(WORDS)
        canv.itemconfig(lang_label, text='English')
        canv.itemconfig(word_label, text=f'{curr_word["eng"]}')
        screen.after(3000, func=flip_card)
    else:
        print('You have done it!')


def flip_card():
    canv.itemconfig(lang_label, text='French')
    canv.itemconfig(word_label, text=f'{curr_word["fr"]}')


def correct():
    WORDS.remove(curr_word)
    next_card()


screen = tk.Tk()
screen.title('Flashy')
screen.config(padx=20, pady=20)

canv = tk.Canvas(width=300, height=200, bg='green')
lang_label = canv.create_text(150, 50, text='English', font=FONT)
word_label = canv.create_text(150, 120, text='to put', font=FONT)
canv.grid(row=0, column=1)

no_button = tk.Button(text='❌', font=FONT, command=next_card)
no_button.grid(row=1, column=0)

yes_button = tk.Button(text='✔', font=FONT, fg='green', command=correct)
yes_button.grid(row=1, column=2)

init()
next_card()

screen.mainloop()
