import tkinter as tk
from tkinter import ttk
import time


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_weight_range(height):
    lower_limit = 18.5 * (height ** 2)
    upper_limit = 24.9 * (height ** 2)
    return lower_limit, upper_limit


def get_height_range(weight):
    lower_limit = (weight / 24.9) ** 0.5
    upper_limit = (weight / 18.5) ** 0.5
    return lower_limit, upper_limit


def animate_label(widget, colors):
    for color in colors:
        widget.config(bg=color)
        root.update()
        time.sleep(0.15)


def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight_unit_var.get() == "lbs":
            weight = weight * 0.453592

        if height_unit_var.get() == "feet":
            height = height * 0.3048

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        bmi_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(text=f"Category: {category}")

        weight_range = get_weight_range(height)
        height_range = get_height_range(weight)

        weight_range_label.config(
            text=f"Suggested Weight Range: {weight_range[0]:.2f} - {weight_range[1]:.2f} kg"
        )

        height_range_label.config(
            text=f"Suggested Height Range: {height_range[0]:.2f} - {height_range[1]:.2f} m"
        )

        animate_label(bmi_label, ["lightgreen", "#f0f0f0"])

    except:
        bmi_label.config(text="Please enter valid numbers")


# MAIN WINDOW
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x350")
root.configure(bg="#f0f0f0")

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(pady=20)

# Weight
tk.Label(main_frame, text="Weight:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=0, column=0)

weight_entry = tk.Entry(main_frame)
weight_entry.grid(row=0, column=1)

weight_unit_var = tk.StringVar(value="kgs")
ttk.Combobox(main_frame, textvariable=weight_unit_var,
             values=("kgs", "lbs"), state="readonly", width=5).grid(row=0, column=2, padx=5)

# Height
tk.Label(main_frame, text="Height:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0)

height_entry = tk.Entry(main_frame)
height_entry.grid(row=1, column=1)

height_unit_var = tk.StringVar(value="meters")
ttk.Combobox(main_frame, textvariable=height_unit_var,
             values=("meters", "feet"), state="readonly", width=5).grid(row=1, column=2, padx=5)

# Button
calculate_button = tk.Button(
    main_frame,
    text="Calculate BMI",
    command=calculate,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 11)
)

calculate_button.grid(row=2, column=0, columnspan=3, pady=15)

# Results
bmi_label = tk.Label(main_frame, text="BMI:", font=("Helvetica", 12), bg="#f0f0f0")
bmi_label.grid(row=3, column=0, columnspan=3)

category_label = tk.Label(main_frame, text="Category:", font=("Helvetica", 12), bg="#f0f0f0")
category_label.grid(row=4, column=0, columnspan=3)

weight_range_label = tk.Label(main_frame, text="Suggested Weight Range:", font=("Helvetica", 12), bg="#f0f0f0")
weight_range_label.grid(row=5, column=0, columnspan=3)

height_range_label = tk.Label(main_frame, text="Suggested Height Range:", font=("Helvetica", 12), bg="#f0f0f0")
height_range_label.grid(row=6, column=0, columnspan=3)

root.mainloop()
