#Drawing on canvas
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

canvas = tk.Canvas(root, bg="white", height=200, width=300)
canvas.pack()

# Draw shapes
canvas.create_rectangle(50, 50, 150, 100, fill="skyblue")
canvas.create_oval(160, 60, 220, 120, fill="red")
canvas.create_text(150, 150, text="Canvas Drawing", fill="green")

root.mainloop()
