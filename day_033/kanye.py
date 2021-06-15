from tkinter import *
import requests

URL = "https://api.kanye.rest/"


def get_quote():
    response = requests.get(URL)
    if response:
        quote = response.json().get("quote")
        canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=500)
background_img = PhotoImage(file="background.png")
canvas.create_image(200, 250, image=background_img)
quote_text = canvas.create_text(200, 250, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
