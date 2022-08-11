import tkinter as tk
from auth_service import register, login


def clear_window(window):
    for child in window.winfo_children():
        child.destroy()


def render_main_screen(window):
    tk.Button(
        window,
        text="Login",
        bg="green",
        fg="white",
        command=lambda: render_login_screen(window)
    ).grid(row=0, column=0)

    tk.Button(
        window,
        text="Register",
        bg="yellow",
        fg="black",
        command=lambda: render_register_screen(window)
    ).grid(row=0, column=1)


def render_products_screen(window):
    clear_window(window)


def render_login_screen(window):
    clear_window(window)

    tk.Label(text="Please enter your username: ").grid(row=0, column=0)
    username = tk.Entry()
    username.grid(row=0, column=1)

    tk.Label(text="Please enter your password: ").grid(row=2, column=0)
    password = tk.Entry(window, show="*")
    password.grid(row=2, column=1)

    def on_login():
        username_value = username.get()
        password_value = password.get()

        result = login(username_value, password_value)
        if result:
            render_products_screen(window)
        else:
            tk.Label(window, text="Invalid credentials!", fg="red").grid(row=3, column=1)

    tk.Button(
        window,
        text="Login",
        bg="green",
        fg="white",
        command=lambda: on_login()
    ).grid(row=4, column=1)


def render_register_screen(window):
    clear_window(window)
    tk.Label(text="Please enter your username: ").grid(row=0, column=0)
    username = tk.Entry()
    username.grid(row=0, column=1)

    tk.Label(text="Please enter your email: ").grid(row=1, column=0)
    email = tk.Entry(window)
    email.grid(row=1, column=1)

    tk.Label(text="Please enter your password: ").grid(row=2, column=0)
    password = tk.Entry(window, show="*")
    password.grid(row=2, column=1)

    tk.Label(text="Please confirm your password:").grid(row=3, column=0)
    confirm_password = tk.Entry(window, show="*")
    confirm_password.grid(row=3, column=1)

    def on_register():
        username_value = username.get()
        email_value = email.get()
        password_value = password.get()
        confirm_password_value = confirm_password.get()

        if password_value != confirm_password_value:
            tk.Label(window, text="Password must match!", fg="red").grid(row=4, column=1)
        else:
            result = register(username_value, email_value, password_value)
            if result:
                render_login_screen(window)
            else:
                tk.Label(window, text="Username is already registered!", fg="red").grid(row=4, column=1)

    tk.Button(
        window,
        text="Register",
        bg="green",
        fg="white",
        command=lambda: on_register()
    ).grid(row=5, column=1)