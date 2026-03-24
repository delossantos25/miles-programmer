import tkinter as tk
from tkinter import messagebox

class DelossantosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Delossantos HO Exam")
        self.root.geometry("420x320")

        self.user_data = {}

        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.show_welcome()

    def clear_frame(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_welcome(self):
        self.clear_frame()

        frame = tk.Frame(self.container, bg="lightblue")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Welcome to Delossantos App", font=("Arial", 20), bg="lightblue").pack(pady=30)

        tk.Button(frame, text="Register", width=20, height=2, bg="green",command=self.show_register).pack(pady=10)

        tk.Button(frame, text="Login", width=20, height=2, bg="blue",command=self.show_login).pack(pady=10)

    def show_register(self):
        self.clear_frame()

        frame = tk.Frame(self.container, bg="lightblue")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Register", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=15)

        tk.Label(frame, text="Username:", bg="lightblue").pack()
        user_entry = tk.Entry(frame)
        user_entry.pack(pady=5)

        tk.Label(frame, text="Password:", bg="lightblue").pack()
        pass_entry = tk.Entry(frame, show="*")
        pass_entry.pack(pady=5)

        show_var = tk.IntVar()
        tk.Checkbutton(frame, text="Show Password", variable=show_var, bg="lightblue", command=lambda: pass_entry.config(show="" if show_var.get() else "*")).pack()

        def register_user():

            username = user_entry.get().strip()
            password = pass_entry.get().strip()

            if username == "" or password == "":
                messagebox.showwarning("Error", "Fields cannot be empty!")
            return

            self.user_data[username] = password
            messagebox.showinfo("Success", "Registered successfully!")
            self.show_welcome()

            tk.Button(frame, text="Submit", bg="lightblue", command=register_user).pack(pady=15)
            tk.Button(frame, text="Back", command=self.show_welcome).pack()
    def show_login(self):
        self.clear_frame()

        frame = tk.Frame(self.container, bg="lightblue")
        frame.pack(fill="both", expand=True)

        header = tk.Label(frame, text="Login", font=("Arial", 18, "bold"), bg="lihtblue")
        header.pack(pady=15)

        tk.Label(frame, text="Username:", bg="lightblue").pack()
        user_entry = tk.Entry(frame)
        user_entry.pack(pady=5)

        tk.Label(frame, text="Password:", bg="lightblue").pack()
        pass_entry = tk.Entry(frame, show="*")
        pass_entry.pack(pady=5)

        def login_user():
            username = user_entry.get()
            password = pass_entry.get()

            if username in self.user_data and self.user_data[username] == password:
                frame.configure(bg="lightblue"), header.config(text=f"Welcome, {username}!", bg="lightblue")
            else:
                frame.configure(bg="red")
                header.config(text="Invalid Credentials!", bg="lightblue")

        tk.Button(frame, text="Login", bg="green", fg="lightblue", command=login_user).pack(pady=15)

        tk.Button(frame, text="Back", command=self.show_welcome).pack()

if __name__ == "__main__":
    root = tk.Tk()
app = DelossantosApp(root)
root.mainloop()
