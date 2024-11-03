import sqlite3
import tkinter as tk
from tkinter import messagebox


def setup_database():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
if __name__ == "__main__":
    setup_database


def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END)

    if name and email and feedback.strip():
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", (name, email, feedback))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Feedback submitted successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_feedback.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")

root = tk.Tk()
root.title("Customer Feedback")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Feedback:").grid(row=2, column=0, padx=10, pady=5)
entry_feedback = tk.Text(root, width=30, height=5)
entry_feedback.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.grid(row=3, column=1, pady=10)

root.mainloop()