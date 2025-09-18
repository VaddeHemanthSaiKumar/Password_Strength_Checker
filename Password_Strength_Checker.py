import re
import tkinter as tk
from tkinter import messagebox

def evaluate_password(password):
    """Return strength score and missing rules."""
    score = 0
    errors = []

    if len(password) >= 8:
        score += 1
    else:
        errors.append("• At least 8 characters long")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        errors.append("• At least one number")

    if any(char.isupper() for char in password):
        score += 1
    else:
        errors.append("• At least one uppercase letter")

    if any(char.islower() for char in password):
        score += 1
    else:
        errors.append("• At least one lowercase letter")

    if re.search(r'[!@#$%^&*()]', password):
        score += 1
    else:
        errors.append("• At least one special character (!@#$%^&*())")

    return score, errors

def update_strength(event=None):
    password = entry.get()
    score, errors = evaluate_password(password)

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score in (3, 4):
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    strength_label.config(text=f"Strength: {strength}", fg=color)

def check_password():
    password = entry.get()
    score, errors = evaluate_password(password)

    if errors:
        msg = "Missing requirements:\n" + "\n".join(errors)
    else:
        msg = "✅ Your password meets all requirements!"
    messagebox.showinfo("Password Check Result", msg)

def toggle_password():
    global show_password
    show_password = not show_password
    if show_password:
        entry.config(show="")
        toggle_button.config(text="🙈 Hide")
    else:
        entry.config(show="*")
        toggle_button.config(text="👁 Show")

# GUI Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x280")
root.resizable(False, False)

title_label = tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter Password:")
entry_label.pack()

frame = tk.Frame(root)
frame.pack(pady=5)

entry = tk.Entry(frame, show="*", width=25, font=("Arial", 11))
entry.pack(side="left", padx=5)
entry.bind("<KeyRelease>", update_strength)

show_password = False
toggle_button = tk.Button(frame, text="👁 Show", command=toggle_password, width=8)
toggle_button.pack(side="left")

check_button = tk.Button(root, text="Check Strength", command=check_password, bg="#4CAF50", fg="white", width=20)
check_button.pack(pady=10)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12))
strength_label.pack(pady=5)

root.mainloop()