import tkinter as tk
from tkinter import ttk
import random


def animate_meter(target):
    current = cook_meter["value"]

    if current < target:
        cook_meter["value"] = current + 1
        root.after(12, lambda: animate_meter(target))


def calculate_cookedness():
    try:
        days = int(days_entry.get())
        syllabus = int(syllabus_entry.get())
        hours = int(hours_entry.get())

        cooked_score = (
            (100 - syllabus) * 0.5
            + (10 - hours) * 3
            + (7 - days) * 5
        )

        cooked_score = max(0, min(100, cooked_score))
        survival_probability = 100 - int(cooked_score)

        cook_meter["value"] = 0
        animate_meter(int(cooked_score))

        # THEME COLORS
        if cooked_score <= 40:
            bg = "#102010"
        elif cooked_score <= 80:
            bg = "#2B1D00"
        else:
            bg = "#2A0000"

        root.configure(bg=bg)

        for w in widgets_to_theme:
            w.configure(bg=bg)

        # STATUS + ROASTS
        if cooked_score <= 20:
            status = "🟢 NOT COOKED"
            color = "#4CAF50"
            roasts = [
                "Bro is actually prepared.",
                "The exam should be scared of you.",
                "You're chilling."
            ]

        elif cooked_score <= 40:
            status = "🟡 SLIGHTLY COOKED"
            color = "#FFC107"
            roasts = [
                "A little revision wouldn't hurt.",
                "You're walking on thin ice."
            ]

        elif cooked_score <= 60:
            status = "🟠 MEDIUM RARE"
            color = "#FF9800"
            roasts = [
                "The syllabus is starting to notice you.",
                "Maybe stop watching YouTube."
            ]

        elif cooked_score <= 80:
            status = "🔴 WELL DONE"
            color = "#FF5722"
            roasts = [
                "Lock in immediately.",
                "Time is not your friend anymore."
            ]

        else:
            status = "☠️ ABSOLUTELY COOKED ☠️"
            color = "#F44336"
            roasts = [
                "The syllabus can smell your fear.",
                "At this point even the calculator is worried.",
                "Bro is fighting for survival.",
                "The exam hall is waiting for you."
            ]

        if cooked_score >= 95:
            roast = "☠️ EXAM REAPER HAS ARRIVED ☠️\n\n" + random.choice(roasts)
        else:
            roast = random.choice(roasts)

        result_label.config(
            text=(
                f"Cooked Score: {int(cooked_score)}%\n\n"
                f"Survival Probability: {survival_probability}%\n\n"
                f"Status: {status}\n\n"
                f"{roast}"
            ),
            fg=color
        )

    except ValueError:
        result_label.config(
            text="Bro entered something invalid 💀",
            fg="red"
        )


def start_analysis():
    messages = [
        "Analyzing academic situation...",
        "Consulting ancient textbooks...",
        "Scanning brain cells...",
        "Calculating survival odds...",
        "Checking panic levels..."
    ]

    result_label.config(text=random.choice(messages), fg="white")
    root.after(1200, calculate_cookedness)


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("How Cooked Am I? 💀")
root.geometry("650x700")
root.configure(bg="#121212")

# Title
title = tk.Label(root, text="HOW COOKED AM I? 💀",
                 font=("Segoe UI", 24, "bold"),
                 fg="white", bg="#121212")
title.pack(pady=15)

# Inputs
days_label = tk.Label(root, text="Days Until Exam",
                       fg="white", bg="#121212")
days_label.pack()

days_entry = tk.Entry(root, width=25)
days_entry.pack(pady=5)

syllabus_label = tk.Label(root, text="Syllabus Completed (%)",
                           fg="white", bg="#121212")
syllabus_label.pack()

syllabus_entry = tk.Entry(root, width=25)
syllabus_entry.pack(pady=5)

hours_label = tk.Label(root, text="Study Hours Per Day",
                       fg="white", bg="#121212")
hours_label.pack()

hours_entry = tk.Entry(root, width=25)
hours_entry.pack(pady=5)

# Button
analyze_button = tk.Button(root, text="Analyze 💀",
                           command=start_analysis,
                           bg="#1E88E5", fg="white",
                           font=("Segoe UI", 12, "bold"),
                           padx=15, pady=8)
analyze_button.pack(pady=15)

# Meter label
meter_label = tk.Label(root, text="Cooked Meter 🔥",
                       fg="white", bg="#121212",
                       font=("Segoe UI", 12, "bold"))
meter_label.pack()

# Progress bar
cook_meter = ttk.Progressbar(root, length=450, maximum=100)
cook_meter.pack(pady=10)

# Result
result_label = tk.Label(
    root,
    text="Enter your stats and discover your fate.",
    fg="white",
    bg="#121212",
    font=("Segoe UI", 12),
    wraplength=500,
    justify="center"
)
result_label.pack(pady=20)

# Footer
footer = tk.Label(root,
                  text="Powered by questionable life decisions 😭",
                  fg="gray", bg="#121212",
                  font=("Segoe UI", 9))
footer.pack(side="bottom", pady=10)

# Widgets to recolor on theme change
widgets_to_theme = [
    title,
    days_label,
    syllabus_label,
    hours_label,
    meter_label,
    result_label,
    footer
]

root.mainloop()