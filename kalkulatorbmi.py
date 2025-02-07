import customtkinter as ctk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  
        bmi = weight / (height ** 2)
        category = bmi_category(bmi)
        result_label.configure(text=f"Your BMI: {bmi:.2f} ({category})")
        print(f"Your BMI: {bmi:.2f} ({category})")
        calculate_calories(weight, height, bmi)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def bmi_category(bmi):
    if bmi < 18.5:
        print("Underweight")
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        print("Overweight")
        return "Overweight"
    else:
        print("Obese")
        return "Obese"

def calculate_calories(weight, height, bmi):
    activity_factor = activity_factors[activity_level.get()]
    
    bmr = 10 * weight + 6.25 * (height * 100) - 5 * 25 + 5 
    maintain_calories = bmr * activity_factor
    lose_weight_calories = maintain_calories - 500
    gain_weight_calories = maintain_calories + 500
    calorie_text = f"Maintain: {maintain_calories:.0f} kcal\nLose Weight: {lose_weight_calories:.0f} kcal\nGain Weight: {gain_weight_calories:.0f} kcal"
    calorie_label.configure(text=calorie_text)
    print(calorie_text)

activity_factors = {
    "Sedentary": 1.2,
    "Lightly active": 1.375,
    "Moderately active": 1.55,
    "Very active": 1.725,
    "Super active": 1.9
}

ctk.set_appearance_mode("dark")  

root = ctk.CTk()
root.title("BMI Calculator")
root.geometry("400x500")

# Widgets
title_label = ctk.CTkLabel(root, text="BMI Calculator", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

weight_label = ctk.CTkLabel(root, text="Enter weight (kg):")
weight_label.pack()
weight_entry = ctk.CTkEntry(root)
weight_entry.pack(pady=5)

height_label = ctk.CTkLabel(root, text="Enter height (cm):")
height_label.pack()
height_entry = ctk.CTkEntry(root)
height_entry.pack(pady=5)

activity_level = ctk.StringVar(value="Sedentary")
activity_dropdown = ctk.CTkOptionMenu(root, variable=activity_level, values=list(activity_factors.keys()))
activity_dropdown.pack(pady=5)

calculate_button = ctk.CTkButton(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

calorie_label = ctk.CTkLabel(root, text="", font=("Arial", 12))
calorie_label.pack(pady=10)

root.mainloop()
