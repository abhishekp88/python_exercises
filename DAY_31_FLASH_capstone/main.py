from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    origional_data = pandas.read_csv("data/french_words.csv")
    # make object which diff key and associate data
    to_learn = origional_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global  current_card, flip_timer, to_learn
    # canceling timer every time click on button
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # updating card title with color
    canvas.itemconfig(card_title, text="French", fill="black")
    # updating card value with color
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    # updating card image
    canvas.itemconfig(card_bg, image=card_front_img)
    # initialize again
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    # updating card title with color and text
    canvas.itemconfig(card_title, text="English", fill="white")
    # updating card word with value and color
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    # updating card background
    canvas.itemconfig(card_bg, image= card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    # index false dont create index property in list
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# 3 seconds timers
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
# card front
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 260, text="word", font=("Ariel", 60, "bold"))






canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
