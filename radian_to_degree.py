import tkinter as tk


def radToDeg():
    rad = float(entry.get())
    deg = rad * 180 / 3.14159265
    result_label.config(text=f"Radian: {rad} = {deg:.2f} degrees")


# Create a tkinter window
window = tk.Tk()
window.title("Radian to Degree Converter")

# Create and pack widgets
label = tk.Label(window, text="Enter Radian:")
label.pack()

# Set the window's geometry to 200x200
window.geometry("200x200")

entry = tk.Entry(window)
entry.pack()

convert_button = tk.Button(window, text="Convert", command=radToDeg)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the tkinter main loop
window.mainloop()

# original code without tkinter
# def radToDeg():
#     rad = float(input("Radian: "))
#     deg = rad * 180 / 3.14159265
#     print(f"Radian: {rad} = {deg}")


# radToDeg()
