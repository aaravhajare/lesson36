import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("500x700")

lbl = tk.Label(window, text="Simple calculator" , font= ("Arial" , 30) , fg = "black" , bg = "white")

lbl_1 = tk.Label(window, text="Enter first number")
num_1 = tk.Entry(window, width=30)
lbl_2 = tk.Label(window, text="Enter second number")
num_2 = tk.Entry(window, width=30)


def Add():
    try:
        first_num = float(num_1.get())
        second_num = float(num_2.get())
        result = first_num + second_num
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

def Subtract():
    try:
        first_num = float(num_1.get())
        second_num = float(num_2.get())
        result = first_num - second_num
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

def Multiply():
    try:
        first_num = float(num_1.get())
        second_num = float(num_2.get())
        result = first_num * second_num
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

def Divide():
    try:
        first_num = float(num_1.get())
        second_num = float(num_2.get())
        result = first_num / second_num
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")
    except ZeroDivisionError:
        result_label.config(text="Division by zero error")

btn_add = tk.Button(window, text="Add" , command=Add )
btn_sub = tk.Button(window, text="Subtract" , command=Subtract)
btn_mul = tk.Button(window, text="Multiply" , command=Multiply)
btn_div = tk.Button(window, text="Divide" , command=Divide)
result_label = tk.Label(window, text="Result: ", font=("Arial", 20))


lbl.pack()
lbl_1.pack()        
num_1.pack()
lbl_2.pack()
num_2.pack()
btn_add.pack()
btn_sub.pack()
btn_mul.pack()
btn_div.pack()
result_label.pack()
window.mainloop()