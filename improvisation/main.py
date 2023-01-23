import tkinter
import customtkinter
from customtkinter import set_widget_scaling

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x600")


def button_function():
    print("Button pressed")



button = customtkinter.CTkButton(master=app, text="Hello World", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
