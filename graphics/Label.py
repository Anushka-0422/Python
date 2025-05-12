import tkinter as tk

# Create the root window
root = tk.Tk()

# Set the title of the window
root.title("My GUI Window")

# Set the size of the window (width x height)
root.geometry("400x300")

# Set background color of the window
root.configure(bg='lightblue')

# Create a label with specific foreground (text) and background colors
label = tk.Label(root, text="Welcome to Tkinter GUI!",
                 fg='darkblue',     # Foreground/Text color
                 bg='lightblue',    # Background color
                 font=("Helvetica", 16))

# Pack the label into the window
label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
