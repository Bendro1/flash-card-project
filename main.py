from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")

window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="/Users/jozef/Desktop/flash-card-project/images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


check_image = PhotoImage(file="/Users/jozef/Desktop/flash-card-project/images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)
#
unknown_image = PhotoImage(file="/Users/jozef/Desktop/flash-card-project/images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)


window.mainloop()