BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

from tkinter import *
from PIL import ImageTk
import pandas
import random


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records", )
else:
    to_learn = data.to_dict(orient="records")


def random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=image1)
    window.after(5000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=image2)

def is_known():
    to_learn.remove(current_card)
    learn = pandas.DataFrame(to_learn)
    learn.to_csv("data/words_to_learn.csv", index=False)
    random_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#B1DDC6")
flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.grid(column=0, row=0, columnspan=2)
image1 = ImageTk.PhotoImage(file="images/card_front.png")
image2 = ImageTk.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=image1)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# canvas1 = Canvas(width=800, height=526)
# canvas1.grid(column=0, row=0, columnspan=2)
# image2 = ImageTk.PhotoImage(file="images/card_back.png")
# canvas1.create_image(0, 0, image=image2, anchor=NW)

check_image = PhotoImage(file="images/right.png")
right = Button(image=check_image, highlightthickness=0, command=random_word)
right.grid(column=1, row=1)

cross_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=cross_image, highlightthickness=0, command=is_known)
wrong.grid(column=0, row=1)

random_word()
window.mainloop()
