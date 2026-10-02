import tkinter as tk
from ui.login import LoginWindow

if __name__ == "__main__":
    from database.db import init_database
    init_database()
    root = tk.Tk()
    root.withdraw()
    LoginWindow(root)
    root.mainloop()
