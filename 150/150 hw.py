from tkinter import *
import random

root=Tk()
root.title("Luck friend Wheel")
root.geometry("500x500")

enter_country = Entry(root)
enter_country.place(relx = 0.5, raly = 0.2 , anchor = CENTER)

enter_capital = Entry(root)
enter_capital.place(relx = 0.5, raly = 0.3 , anchor = CENTER)

display_country_list = Label(root)
display_capital_list = Label(root)

display_random_country_list = Label(root)
display_random_capital_list = Label(root)

capital_list = []
country_list = []

def country_city_list():
    country = enter_country.get()
    country_list.append(country)
    display_country_list["text"] = "Country Name :" str(country_list)
    
    capital = enter_capital.get()
    capital_list.append(capital)
    display_capital_list["text"] = "Country Name :" str(capial_list)
    
btn = Button() 
root.mainloop()