import tkinter as tk
import random as random

comp = ["rock", "paper", "scizors"]
result = ''

def rock():
    comp_choice = comp[random.randint(0, 2)]
    if comp_choice == "scizors":
        print(f"computer chose {comp_choice}, you win.")
    elif comp_choice == "rock":
        print(f"computer chose {comp_choice}, its a draw.")
    else:
        print(f"computer chose {comp_choice}, you loose.")

def paper():
    comp_choice = comp[random.randint(0, 2)]
    if comp_choice == "scizors":
        print(f"computer chose {comp_choice}, you lose.")
    elif comp_choice == "rock":
        print(f"computer chose {comp_choice}, you win.")
    else:
        print(f"computer chose {comp_choice}, its a draw.")

def szrs():
    comp_choice = comp[random.randint(0, 2)]
    if comp_choice == "scizors":
        print(f"computer chose {comp_choice}, its a draw.")
    elif comp_choice == "rock":
        print(f"computer chose {comp_choice}, you loose.")
    else:
        print(f"computer chose {comp_choice}, you win.")

root = tk.Tk()
root.geometry("300x150")
root.title("Rock Paper Scizors Game")

label = tk.Label(root, text="Choose an option:")
label.pack()

btn_rock = tk.Button(root, text="Rock!", command=rock)
btn_rock.pack(padx=5, pady=5)
btn_paper = tk.Button(root, text="Paper!", command=paper)
btn_paper.pack(padx=5, pady=5)
btn_szrs = tk.Button(root, text="scizors!", command=szrs)
btn_szrs.pack(padx=5, pady=5)


root.mainloop()