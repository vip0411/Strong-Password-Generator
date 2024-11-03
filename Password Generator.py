import random
import string
import tkinter as tk

def generate_password(length):
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

def generate_password_click():
    length = int(length_entry.get())
    password = generate_password(length)
    password_var.set(password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x150")  # Set window size

# Create the label and entry for password length
length_label = tk.Label(window, text="Enter desired password length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

# Create the button to trigger password generation
generate_button = tk.Button(window, text="Generate Password", command=generate_password_click)
generate_button.pack()

# Create a StringVar to hold the password
password_var = tk.StringVar()

# Create the text box to display the generated password
password_textbox = tk.Entry(window, textvariable=password_var)
password_textbox.pack()

window.mainloop()