from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
wait_period = True


file = pandas.read_csv("./data/french_words.csv")
language_file = file.to_dict()
print(language_file)
eng = (language_file["English"])
print(language_file["French"])
pr
random_word_range = random.randint(0, 101)

french_word = language_file["French"][random_word_range]
english_word = language_file["English"][random_word_range]

def move():
    global english_word, timer
    window.after_cancel(timer)
    random_word_range = random.randint(0, 100)

    french_word = language_file["French"][random_word_range]
    english_word = language_file["English"][random_word_range]
    canvas.itemconfig(title_canvas, text="French", fill="black")
    window.config(bg=BACKGROUND_COLOR)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(french_canvas, text=french_word, fill="black")
    timer = window.after(3000, flip)



def flip():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title_canvas, text="English", fill="white")
    canvas.itemconfig(french_canvas, text=english_word, fill="white")
    window.config(bg="white")



window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title("FlashCard")
timer = window.after(3000, flip)
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
title_canvas = canvas.create_text(400, 150, text="french", fill="black", font=("Courier", 35, "bold"))
french_canvas = canvas.create_text(400, 263, text=french_word, fill="black", font=("Courier", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

know_button = Button(width=10)
right_image = PhotoImage(file="./images/right.png")
know_button.config(image=right_image, highlightthickness=0, width=50, height=50, command=move)
know_button.grid(row=1, column=0)

unknown_button = Button()
wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button.config(image=wrong_image, highlightthickness=0, width=50, height=50, command=move)
unknown_button.grid(row=1, column=1)





window.mainloop()