from tkinter import *

window = Tk()
window.title("Mile to Kilometer Project")
window.minsize(width=300, height=200)
window.config(padx = 20,pady=20)

label1 = Label(text="Miles")


miles_input = Entry(width=7)
miles_input.place(x= 100 ,y = 20)

miles_label = Label(text= "Miles")
miles_label.place(x= 160 ,y = 20)

equal_to_label = Label(text= "Is equal To :")
equal_to_label.place(x= 10 ,y = 50)

km_label = Label(text= "KM")
km_label.place(x= 160 ,y = 50)

km_answer_label = Label(text= "0")
km_answer_label.place(x= 100 ,y = 50)

def action():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_answer_label.config(text=f"{km}")    

#calls action() when pressed
button = Button(text="Click To Convert", command=action)
button.place(x= 70 ,y = 80)

window.mainloop()
