from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("500x500")

label1 = Label(root)
label2 = Label(root)

List1 = ["Bottle","Tiffin","ID Card","Chocolates","Chips","Tickets","Hanky"]
label1["text"] = "Listed_items :  " + str(List1)

def bag_contents():
   
    random_list = random.sample(range(0,7),1)
    label2["text"] = "Put Item no  " + str(random_list) + "  In bag"
   
     
label1.place(relx=0.5,rely = 0.4, anchor = CENTER)

btn = Button(root, text="Which item to put in bag?",command = bag_contents,bg="orange",fg="white")
btn.place(relx=0.5,rely = 0.5, anchor = CENTER)
   

label2.place(relx=0.5,rely = 0.6, anchor = CENTER)


root.mainloop()