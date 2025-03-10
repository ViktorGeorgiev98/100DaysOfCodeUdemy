from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}
data_dict = {}

try:
    # read csv
    data = pandas.read_csv("./day_31_flash_capstone_project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(
        "./day_31_flash_capstone_project/data/french_words.csv"
    )
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


# functions
def pick_random_word():
    global word, flip_timer
    screen.after_cancel(flip_timer)
    word = random.choice(data_dict)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = screen.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


def is_known():
    data_dict.remove(word)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv(
        "./day_31_flash_capstone_project/data/words_to_learn.csv", index=False
    )
    pick_random_word()


# create the screen
screen = Tk()
screen.title("Flashy")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = screen.after(3000, func=flip_card)


# canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./day_31_flash_capstone_project/images/card_front.png")
back_image = PhotoImage(file="./day_31_flash_capstone_project/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
correct_answer_image = PhotoImage(
    file="./day_31_flash_capstone_project/images/right.png"
)
wrong_answer_image = PhotoImage(file="./day_31_flash_capstone_project/images/wrong.png")


# labels


# buttons
unknown_button = Button(
    image=wrong_answer_image, highlightthickness=0, command=pick_random_word
)
unknown_button.grid(row=1, column=0)
known_button = Button(
    image=correct_answer_image, highlightthickness=0, command=is_known
)
known_button.grid(row=1, column=1)


pick_random_word()
screen.mainloop()
