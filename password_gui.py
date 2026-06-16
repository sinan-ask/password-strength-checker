import re
import tkinter as tk
from tkinter import ttk  # Imported ttk for the Progressbar widget

def check_password_strength(password):
    score = 0
    feedback = []

    if not password:
        return 0, "", "gray"

    # Rule checks
    if len(password) >= 8: score += 1
    else: feedback.append("• At least 8 characters")

    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("• Add an uppercase letter")

    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("• Add a lowercase letter")

    if re.search(r"\d", password): score += 1
    else: feedback.append("• Include a number")

    if re.search(r"[@$!%*?&#]", password): score += 1
    else: feedback.append("• Include a special character")

    # Dynamic styling values based on score
    if score == 5:
        return score, "Strong: Excellent security!", "green"
    elif score >= 3:
        return score, "Medium:\n" + "\n".join(feedback), "orange"
    else:
        return score, "Weak:\n" + "\n".join(feedback), "red"

def on_key_release(event):
    """Triggers automatically every time a user types a letter"""
    password = password_entry.get()
    
    score, tips, color = check_password_strength(password)
    
    # Update progress bar value (maps score 0-5 to 0-100%)
    strength_bar["value"] = score * 20
    
    # Update labels and colors
    result_label.config(text=tips, fg=color)
    
    # Simple trick to change the progress bar color feel
    if score == 5:
        style.configure("TProgressbar", foreground="green", background="green")
    elif score >= 3:
        style.configure("TProgressbar", foreground="orange", background="orange")
    else:
        style.configure("TProgressbar", foreground="red", background="red")

# --- UI Layout Setup ---
root = tk.Tk()
root.title("Live Password Guard")
root.geometry("450x400")
root.config(padx=25, pady=25)

# Configure ttk style for the progress bar color changes
style = ttk.Style()
style.theme_use('clam')

# UI Widgets
title_label = tk.Label(root, text="Type a password to test live:", font=("Helvetica", 12))
title_label.pack(pady=5)

password_entry = tk.Entry(root, font=("Helvetica", 14), show="*", width=24)
password_entry.pack(pady=10)

# Bind the key release event to our function (Removes the need for a button!)
password_entry.bind("<KeyRelease>", on_key_release)

# Progress Bar (max value 100 for 5 rules)
strength_bar = ttk.Progressbar(root, orient="horizontal", length=280, mode="determinate", maximum=100)
strength_bar.pack(pady=15)

# Combined Result & Tips Display
result_label = tk.Label(root, text="Start typing...", font=("Helvetica", 11), justify="left", wraplength=400, fg="gray")
result_label.pack(pady=15)
root.mainloop()