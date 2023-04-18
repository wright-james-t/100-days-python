from tkinter import *
import pandas
import random

# Constants and globals
BACKGROUND_COLOR = "#B1DDC6"  # Light green
FONT_TYPE = "Comic Sans"
random_word = ""
base_word = ""
translated_word = ""

# ---------- LANGUAGES SET UP ---------- #


def convert_csv_to_dict(csv_file):
    """Returns record oriented dict based on provided /path/to/csv_file"""
    csv_data = pandas.read_csv(csv_file)
    return csv_data.to_dict(orient="records")


# Validation to see if it's first run/no words to learn were added previously
try:
    french_dict = convert_csv_to_dict("data/words_to_learn.csv")
except FileNotFoundError:
    french_dict = convert_csv_to_dict("data/french_words.csv")

current_lang_data = french_dict
current_lang = "French"


# ---------- FLASHCARD FUNCTIONALITY ---------- #


def choose_random_word():
    """Sets the global variables random_word, base_word, and translated_word to a random set from provided dictionary"""
    global random_word
    global base_word
    global translated_word
    random_word = random.choice(current_lang_data)
    base_word = random_word[current_lang]
    translated_word = random_word['English']


def new_word():
    """Flips card, updates global vars for random words"""
    global flip_timer
    window.after_cancel(flip_timer)
    choose_random_word()
    canvas.itemconfig(canvas_title, text=current_lang, fill="Black")
    canvas.itemconfig(canvas_word, text=base_word, fill="Black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    """Call to flip card"""
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=translated_word, fill="white")
    canvas.itemconfig(card_bg, image=card_back)


def known_word():
    """Adds the current word to a 'known' list, it is no longer shown in future runs of the game"""
    global current_lang_data
    current_lang_data.remove(random_word)
    print(len(current_lang_data))
    new_data = pandas.DataFrame(current_lang_data)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    new_word()


# ---------- UI SETUP ---------- #

# Window
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=flip_card)

# Images
correct_img = PhotoImage(file="images/right.png")
incorrect_img = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

# Canvas
canvas = Canvas(width=800, height=526)
card_bg = canvas.create_image(400, 263, image=card_front)
canvas_title = canvas.create_text(400, 200, text=current_lang, font=(FONT_TYPE, 25, "italic"))
canvas_word = canvas.create_text(400, 275, text="Word", font=(FONT_TYPE, 35, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1, columnspan=2)

# Buttons
button_correct = Button(image=correct_img, highlightthickness=0, borderwidth=0, command=known_word)
button_correct.grid(column=1, row=2)

button_incorrect = Button(image=incorrect_img, highlightthickness=0, borderwidth=0, command=new_word)
button_incorrect.grid(column=2, row=2)

new_word()

window.mainloop()
