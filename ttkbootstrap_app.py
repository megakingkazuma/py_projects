import tkinter as tk
from tkinter import messagebox

# Function to validate login credentials


def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace this with your authentication logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create the main window
root = tk.Tk()
root.title("Login Window")
root.geometry("300x150")

# Create and place labels and entry fields for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack()

# Run the tkinter main loop
root.mainloop()
