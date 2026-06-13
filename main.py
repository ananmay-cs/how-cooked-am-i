import tkinter as tk

root = tk.Tk()

root.title("How Cooked Am I?")
root.geometry("500x400")

title = tk.Label(
    root,
    text="HOW COOKED AM I? 💀",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)

root.mainloop()