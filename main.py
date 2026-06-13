import tkinter as tk


def calculate_cookedness():
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

    if cooked_score <= 20:
        status = "NOT COOKED 😎"
        advice = "You're chilling bro."

    elif cooked_score <= 40:
        status = "SLIGHTLY COOKED 🙂"
        advice = "A little revision wouldn't hurt."

    elif cooked_score <= 60:
        status = "MEDIUM RARE 😬"
        advice = "Maybe stop watching YouTube for a bit."

    elif cooked_score <= 80:
        status = "WELL DONE 🔥"
        advice = "Lock in immediately."

    else:
        status = "ABSOLUTELY COOKED 💀"
        advice = "The syllabus can smell your fear."

    result_label.config(
    text=
    f"Cooked Score: {int(cooked_score)}%\n\n"
    f"Survival Probability: {survival_probability}%\n\n"
    f"Status: {status}\n\n"
    f"{advice}"
    )

root = tk.Tk()

root.title("How Cooked Am I?")
root.geometry("500x450")

title = tk.Label(
    root,
    text="HOW COOKED AM I? 💀",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# Days until exam
days_label = tk.Label(root, text="Days Until Exam:")
days_label.pack()

days_entry = tk.Entry(root)
days_entry.pack(pady=5)

# Syllabus completed
syllabus_label = tk.Label(root, text="Syllabus Completed (%):")
syllabus_label.pack()

syllabus_entry = tk.Entry(root)
syllabus_entry.pack(pady=5)

# Study hours
hours_label = tk.Label(root, text="Study Hours Per Day:")
hours_label.pack()

hours_entry = tk.Entry(root)
hours_entry.pack(pady=5)

# Result label
result_label = tk.Label(
    root,
    text="Enter your stats and click Analyze",
    font=("Arial", 12)
)
result_label.pack(pady=20)

# Analyze button
analyze_button = tk.Button(
    root,
    text="Analyze 💀",
    command=calculate_cookedness
)
analyze_button.pack()

root.mainloop()