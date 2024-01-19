from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

def button_click():
    my_label["text"] = input.get()


# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0, pady=50, padx=50)


new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

button = Button(text="Click me", command=button_click)
button.grid(column=1, row=1)

#Entry

input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()