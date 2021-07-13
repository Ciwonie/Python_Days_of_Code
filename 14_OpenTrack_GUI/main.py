import socket
import threading
from tkinter import *
import opentrack_request

# ------------------------- Constants -------------------------
BACKGROUND_COLOR = "#B1DDC6"


# ------------------------- Functionality -------------------------
def view_control_screen():
    if opentrack_request.connect_ot():
        canvas.itemconfig(card_title, text="CONNECTED", fill="white")
        canvas.delete(card_port)
        canvas.itemconfig(card_background, image=main_screen)
        exit_button.grid(row=1, column=1)
        connect_button.destroy()


# ------------------------- User Interface -------------------------
window = Tk()
window.title("OpenTrack Interface")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
start_screen = PhotoImage(file="images/card_front.png")
main_screen = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=start_screen)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

card_title = canvas.create_text(400, 150, text="Connect to OpenTrack", font=("Ariel", 40, "italic"))
card_port = canvas.create_text(400, 263, text=f"PORT: {opentrack_request.PORT}", font=("Ariel", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
exit_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=window.destroy)
exit_button.grid(row=1, column=0)
check_image = PhotoImage(file="images/right.png")
connect_button = Button(image=check_image, highlightthickness=0, borderwidth=0, command=view_control_screen)
connect_button.grid(row=1, column=2)

window.mainloop()
