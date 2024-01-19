from tkinter import *

screen = Tk()
screen.title("Mile to Km Converter")
screen.config(padx=20, pady=20)


def calculate():
    n = int(input.get())
    n *= 1.609
    n = round(n)
    label3["text"] = str(n)


# Entry widget

input = Entry(width=7)
input.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)
label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="")
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)




screen.mainloop()