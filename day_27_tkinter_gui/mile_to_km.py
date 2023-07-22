from tkinter import  *

window = Tk()

window.title('Miles to KM Program')
window.minsize(width=500, height=300)
# ADD padding into window
window.config(padx=20, pady=20)


def convert_to_km() :
    miles = int(entry.get())
    print(miles)
    km = miles + round(miles/2)
    km_number_label.config(text=km)


entry = Entry()
entry.grid(column=1, row= 0)

miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_number_label = Label(text=0)
km_number_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text='Calculate', command=convert_to_km)
button.grid(column=1,row=2)









window.mainloop()