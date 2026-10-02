import tkinter as tk
from tkinter import messagebox
from database.db import get_connection


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Global Accounting - Login")
        self.root.geometry("500x420")
        self.root.resizable(False, False)
        self._center_window()
        self.build_ui()
        self.init_default_user()

    def _center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def build_ui(self):
        title = tk.Label(self.root, text="Global Accounting", font=("Arial", 24, "bold"), fg="#2c3e50")
        title.pack(pady=25)

        subtitle = tk.Label(self.root, text="Professional Accounting Software", font=("Arial", 10), fg="#7f8c8d")
        subtitle.pack()

        form_frame = tk.Frame(self.root, bg="white")
        form_frame.pack(padx=40, pady=20, fill=tk.BOTH, expand=True)

        tk.Label(form_frame, text="Username:", font=("Arial", 11), bg="white").pack(anchor="w", pady=(10, 5))
        self.username_var = tk.StringVar(value="admin")
        username_entry = tk.Entry(form_frame, textvariable=self.username_var, font=("Arial", 11))
        username_entry.pack(fill=tk.X, pady=(0, 15))

        tk.Label(form_frame, text="Password:", font=("Arial", 11), bg="white").pack(anchor="w", pady=(10, 5))
        self.password_var = tk.StringVar(value="admin")
        password_entry = tk.Entry(form_frame, textvariable=self.password_var, font=("Arial", 11), show="*")
        password_entry.pack(fill=tk.X, pady=(0, 20))

        login_btn = tk.Button(
            form_frame,
            text="Login",
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            command=self.login,
            cursor="hand2",
            padx=40,
            pady=10,
        )
        login_btn.pack(fill=tk.X)

        info = tk.Label(self.root, text="Default: admin / admin", font=("Arial", 9), fg="#95a5a6")
        info.pack(pady=10)

    def init_default_user(self):
        conn = get_connection()
        try:
            conn.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT DEFAULT 'admin'
                )"""
            )
            conn.commit()
            user = conn.execute("SELECT * FROM users WHERE username = 'admin'").fetchone()
            if not user:
                conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ("admin", "admin", "admin"))
                conn.commit()
        finally:
            conn.close()

    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not password:
            messagebox.showwarning("Warning", "Please enter username and password")
            return

        conn = get_connection()
        try:
            user = conn.execute(
                "SELECT * FROM users WHERE username = ? AND password = ?",
                (username, password)
            ).fetchone()
            if user:
                self.root.destroy()
                import tkinter as tk
                from ui.main_window import GlobalAccountingApp
                root = tk.Tk()
                app = GlobalAccountingApp(root)
                root.mainloop()
            else:
                messagebox.showerror("Error", "Invalid username or password")
        finally:
            conn.close()
