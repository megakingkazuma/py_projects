# my_dictionary = {1,2,3}
# my_touple = (1,2,3)
# my_list = [1, 2, 3]
# my_word = "Alphabet"

# print(type(my_dictionary))
# print(my_dictionary)
# print(type(my_touple))
# print(my_touple)
# print(type(my_list))
# print(my_list)

# user_inputs = []

# for i in range(4):
#     user_input = input("Enter a value: ")
#     user_inputs.append(user_input)
# sorted = sorted(user_inputs, reverse = True)
# for i in sorted:
#     print(i)

# def OddOrEven():
#     number = float(input("Enter a number: "))
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")

# OddOrEven()

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def OutPut():
    name = entry.get()
    print(f"Hi {name}")
    display_out.config(text=f"Hi {name}")

root = ttk.Window(themename="superhero")
# root = tk.Tk()
root.geometry("500x350")
root.title("Application")

label = ttk.Label(text="Log in Form", font=("impact", 20), bootstyle="light")
label.pack(padx=3, pady=5)

entry = ttk.Entry(root)
entry.pack()

btn2 = ttk.Button(text="Click me!", command=OutPut, bootstyle="danger, outline")
btn2.pack(padx=3, pady=5)

display_out = ttk.Label(root, text='' ,font=("impact", 20))
display_out.pack()

root.mainloop()