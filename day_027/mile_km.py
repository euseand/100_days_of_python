import tkinter as tk


window = tk.Tk()
window.title("Convert Miles to Km's")
window.minsize(width=900, height=400)

label = tk.Label(text="Enter values to be converted", font=('Roboto', 20, 'bold'))
label.pack()

label_miles = tk.Label(text="Miles: ", font=('Roboto', 20, 'bold'))

label_kms = tk.Label(text="Kilometers: ", font=('Roboto', 20, 'bold'))

input_miles = tk.Entry(text="Miles: ")
input_miles.pack()

input_kms = tk.Entry(text="Km's: ")
input_kms.pack()


def clck():
    if input_miles.get():
        label_kms.pack()
        label_kms['text'] = "Km's: " + str(float(input_miles.get()) * 2.7)
    else:
        label_kms['text'] = ''

    if input_kms.get():
        label_miles.pack()
        label_miles['text'] = "Miles: " + str(float(input_kms.get()) / 2.7)
    else:
        label_miles['text'] = ''


button = tk.Button(text="Convert", command=clck)
button.pack()


window.mainloop()
