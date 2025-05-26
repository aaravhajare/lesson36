import tkinter
from datetime import datetime
today = datetime.now()

w = tkinter.Tk()
w.title("Getting started with widgets")
w.geometry("500x700")

lbl = tkinter.Label(w, text="Hello World!" , font=("poppins" , 20 ) , fg = "black" , bg = "cyan")

n_lbl = tkinter.Label(w, text="Enter Full name")
n_inp = tkinter.Entry(w, width=30)

def display ():
    name = n_inp.get()

    global message
    message = "Welcome to app"
    greet = "Hello " + name

    Text_box.insert(tkinter.END,message + "\n")
    Text_box.insert(tkinter.END,greet + "\n")
    Text_box.insert(tkinter.END,today.time())


Text_box = tkinter.Text(w, height=3)

btn = tkinter.Button(w,text= "Submit" , command=display , bg="blue")

lbl.pack()
n_lbl.pack()
n_inp.pack()
Text_box.pack()
btn.pack()  

w.mainloop()