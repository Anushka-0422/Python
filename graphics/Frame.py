#working with container
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Create a Frame (container)
frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame.pack(pady=20)

# Add widgets inside the frame
label = tk.Label(frame, text="Inside Frame", fg="blue")
label.pack()

button = tk.Button(frame, text="Click Me")
button.pack()

root.mainloop()
