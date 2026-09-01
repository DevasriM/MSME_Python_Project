import tkinter as tk
import secrets
import string
from tkinter import messagebox


# -----------------------------
# Global variables
# -----------------------------
generated_otp = ""
short_url = ""


# -----------------------------
# Generate OTP
# -----------------------------
def generate_otp():
    global generated_otp

    generated_otp = str(secrets.randbelow(900000) + 100000)

    otp_label.config(
        text="OTP generated. Enter the OTP below."
    )

    # For learning/testing purposes
    print("Generated OTP:", generated_otp)


# -----------------------------
# Create random short code
# -----------------------------
def create_short_code():
    characters = string.ascii_letters + string.digits

    short_code = "".join(
        secrets.choice(characters)
        for _ in range(6)
    )

    return short_code


# -----------------------------
# Shorten URL
# -----------------------------
def shorten_url():
    global short_url

    long_url = url_entry.get().strip()

    if long_url == "":
        url_result.config(
            text="Please enter a URL."
        )
        return

    if not (
        long_url.startswith("http://")
        or long_url.startswith("https://")
    ):
        url_result.config(
            text="Enter a valid URL starting with http:// or https://"
        )
        return

    short_code = create_short_code()

    short_url = "ShortIt/" + short_code

    url_result.config(
        text="Short URL: " + short_url
    )


# -----------------------------
# Copy short URL
# -----------------------------
def copy_url():
    if short_url == "":
        url_result.config(
            text="Generate a short URL first."
        )
        return

    window.clipboard_clear()
    window.clipboard_append(short_url)
    window.update()

    url_result.config(
        text="Short URL copied to clipboard!"
    )


# -----------------------------
# Open URL shortener screen
# -----------------------------
def open_url_shortener():

    global url_entry
    global url_result

    # Hide login screen
    title_label.pack_forget()
    subtitle_label.pack_forget()
    username_label.pack_forget()
    username_entry.pack_forget()
    otp_button.pack_forget()
    otp_label.pack_forget()
    otp_entry.pack_forget()
    verify_button.pack_forget()
    result_label.pack_forget()

    # URL title
    url_title = tk.Label(
        window,
        text="SHORTIT URL",
        font=("Arial", 24, "bold")
    )
    url_title.pack(pady=(40, 10))

    # Subtitle
    url_subtitle = tk.Label(
        window,
        text="Secure URL Shortener",
        font=("Arial", 11)
    )
    url_subtitle.pack(pady=5)

    # URL label
    url_label = tk.Label(
        window,
        text="Enter Long URL",
        font=("Arial", 12)
    )
    url_label.pack(pady=(30, 5))

    # URL entry
    url_entry = tk.Entry(
        window,
        width=50,
        font=("Arial", 11)
    )
    url_entry.pack(pady=10)

    # Shorten button
    shorten_button = tk.Button(
        window,
        text="Shorten URL",
        font=("Arial", 11, "bold"),
        width=18,
        command=shorten_url
    )
    shorten_button.pack(pady=20)

    # Result label
    url_result = tk.Label(
        window,
        text="",
        font=("Arial", 11)
    )
    url_result.pack(pady=10)

    # Copy button
    copy_button = tk.Button(
        window,
        text="COPY URL",
        font=("Arial", 11, "bold"),
        width=18,
        command=copy_url
    )
    copy_button.pack(pady=5)


# -----------------------------
# Verify OTP
# -----------------------------
def verify_otp():

    entered_otp = otp_entry.get().strip()

    if entered_otp == "":
        result_label.config(
            text="Please enter the OTP."
        )
        return

    if entered_otp == generated_otp:
        open_url_shortener()
    else:
        result_label.config(
            text="Invalid OTP. Try again."
        )


# -----------------------------
# Main Window
# -----------------------------
window = tk.Tk()

window.title("Secure URL Shortener")
window.geometry("500x500")
window.resizable(False, False)


# -----------------------------
# Login Screen
# -----------------------------

title_label = tk.Label(
    window,
    text="SECURE URL SHORTENER",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=40)


subtitle_label = tk.Label(
    window,
    text="Create and manage shortened URLs securely",
    font=("Arial", 11)
)
subtitle_label.pack(pady=10)


username_label = tk.Label(
    window,
    text="Enter username:",
    font=("Arial", 12)
)
username_label.pack(pady=(30, 5))


username_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 12)
)
username_entry.pack()


otp_button = tk.Button(
    window,
    text="Generate OTP",
    font=("Arial", 12, "bold"),
    width=15,
    command=generate_otp
)
otp_button.pack(pady=30)


otp_label = tk.Label(
    window,
    text="Click Generate OTP",
    font=("Arial", 10)
)
otp_label.pack(pady=5)


otp_entry = tk.Entry(
    window,
    width=20,
    font=("Arial", 12)
)
otp_entry.pack(pady=10)


verify_button = tk.Button(
    window,
    text="Verify OTP",
    font=("Arial", 11, "bold"),
    width=15,
    command=verify_otp
)
verify_button.pack(pady=10)


result_label = tk.Label(
    window,
    text="",
    font=("Arial", 10)
)
result_label.pack(pady=5)


# -----------------------------
# Start application
# -----------------------------
window.mainloop()
