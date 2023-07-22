from tkinter import *

window = Tk()

window.title('First GUI Program')
window.minsize(width=500, height=300)
# ADD padding into window
window.config(padx=20, pady=20)


# label
my_label = Label(text="I am a label", font=("Arial", 24))


# advance python arguements

'''
keyword arguments
def my_function(a, b, c):
    do with a
    do with b
    do with c
    
arguments with default values
def my_function(a=1, b=2, c=3):
    do with a
    do with b
    do with c    


'''
# this method to set this object into screen / set center of the screen (top center)
my_label.pack()
# to update properties
my_label['text'] = 'change text'
my_label.config(text='Change text 2')
my_label.grid(column=0, row=0)

def button_clicked():
    # to get input text value
    enter_data = input.get()
    print(enter_data)
    my_label.config(text=enter_data)
    print('on button click')

# command is use to register function with button click
button = Button(text='click me', command=button_clicked)
button.grid(column=1, row=1)


button = Button(text='click me 2', command=button_clicked)
button.grid(column=3, row=0)

# button.pack()
# Entry
input = Entry()
input.grid(column=4, row=4)


# we can't use pack and grid together use either grid or pack
# input.pack()

# my_label.pack(side='left')
# place is used to allocate field into x, y coordinate into screen
# my_label.place(x=0,y=0)
# button.pack()
# button.place(x= 20, y = 100)
# input.pack()

# grid is used to align fields into grid format

# my_label.grid(column=0, row=0)
# button.grid(column=1, row=1)
# my_label.pack()
# button.pack()
# it keep window on the screen
window.mainloop()

'''
add unlimited arguments
* this tell this function add can accept any number of arguments , args its just a name , it can be anything
def add(*args):
    for n in args:
        print(n)
'''