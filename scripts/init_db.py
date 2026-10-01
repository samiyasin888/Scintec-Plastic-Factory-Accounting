import tkinter as tk
from tkinter import ttk, messagebox

from config.config import APP_NAME, APP_VERSION, APP_COMPANY
from database.db import initialize_database
from services.accounting_service import AccountingService
from services.translation_service import Translator


class GlobalAccountingApp:
    def __init__(self, root):
        initialize_database()
        self.root = root
        self.root.title(f"{APP_NAME} - {APP_COMPANY}")
        self.root.geometry("1200x800")
        self.service = AccountingService()
        self.lang = self.service.get_language()
        self.translator = Translator(self.lang)
        self.current_invoice_items = []
        self.build_ui()
        self.reload_data()

    def t(self, key):
        return self.translator.t(key)

    def build_ui(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.dashboard_tab = ttk.Frame(self.notebook)
        self.invoice_tab = ttk.Frame(self.notebook)
        self.inventory_tab = ttk.Frame(self.notebook)
        self.payroll_tab = ttk.Frame(self.notebook)
        self.settings_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.dashboard_tab, text=self.t("dashboard"))
        self.notebook.add(self.invoice_tab, text=self.t("invoices"))
        self.notebook.add(self.inventory_tab, text=self.t("inventory"))
        self.notebook.add(self.payroll_tab, text=self.t("payroll"))
        self.notebook.add(self.settings_tab, text=self.t("settings"))

        self.build_dashboard()
        self.build_invoice_tab()
        self.build_inventory_tab()
        self.build_payroll_tab()
        self.build_settings_tab()

    def build_dashboard(self):
        cards = [
            (self.t("total_products"), "products"),
            (self.t("inventory_value"), "inventory_qty"),
            (self.t("total_invoices"), "invoices"),
            (self.t("sales_total"), "sales_total"),
            (self.t("employees_count"), "employees"),
        ]

        for idx, (label, key) in enumerate(cards):
            frame = ttk.LabelFrame(self.dashboard_tab, text=label, padding=12)
            frame.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")
            self.__dict__[f"{key}_label"] = tk.Label(frame, text="0", font=("Arial", 20, "bold"))
            self.__dict__[f"{key}_label"].pack()

        self.dashboard_tab.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

    def build_invoice_tab(self):
        form = ttk.Frame(self.invoice_tab)
        form.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(form, text=self.t("invoice_number")).grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.invoice_number_var = tk.StringVar(value="INV-001")
        ttk.Entry(form, textvariable=self.invoice_number_var).grid(row=0, column=1, padx=5, pady=4)

        ttk.Label(form, text=self.t("customer_name")).grid(row=1, column=0, sticky="w", padx=5, pady=4)
        self.customer_name_var = tk.StringVar(value="Walk-in Customer")
        ttk.Entry(form, textvariable=self.customer_name_var).grid(row=1, column=1, padx=5, pady=4)

        ttk.Label(form, text=self.t("product_name")).grid(row=2, column=0, sticky="w", padx=5, pady=4)
        self.product_name_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.product_name_var).grid(row=2, column=1, padx=5, pady=4)

        ttk.Label(form, text=self.t("quantity")).grid(row=3, column=0, sticky="w", padx=5, pady=4)
        self.quantity_var = tk.StringVar(value="1")
        ttk.Entry(form, textvariable=self.quantity_var).grid(row=3, column=1, padx=5, pady=4)

        ttk.Label(form, text=self.t("unit_price")).grid(row=4, column=0, sticky="w", padx=5, pady=4)
        self.unit_price_var = tk.StringVar(value="0")
        ttk.Entry(form, textvariable=self.unit_price_var).grid(row=4, column=1, padx=5, pady=4)

        ttk.Button(form, text=self.t("add_item"), command=self.add_invoice_item).grid(row=5, column=0, columnspan=2, pady=8)
        ttk.Button(form, text=self.t("create_invoice"), command=self.create_invoice).grid(row=6, column=0, columnspan=2, pady=8)

        columns = ("name", "qty", "price", "total")
        self.invoice_tree = ttk.Treeview(self.invoice_tab, columns=columns, show="headings")
        for col in columns:
            self.invoice_tree.heading(col, text=col)
            self.invoice_tree.column(col, width=120)
        self.invoice_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def add_invoice_item(self):
        try:
            qty = float(self.quantity_var.get())
            price = float(self.unit_price_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid quantity and price.")
            return

        item = {
            "name": self.product_name_var.get(),
            "quantity": qty,
            "unit_price": price,
            "total": qty * price,
        }
        self.current_invoice_items.append(item)
        self.invoice_tree.insert("", "end", values=(item["name"], item["quantity"], item["unit_price"], item["total"]))
        self.product_name_var.set("")
        self.quantity_var.set("1")
        self.unit_price_var.set("0")

    def create_invoice(self):
        if not self.current_invoice_items:
            messagebox.showwarning("Warning", "Please add at least one item before creating an invoice.")
            return

        invoice_number = self.invoice_number_var.get()
        customer_name = self.customer_name_var.get()
        tax_rate = self.service.get_company().get("tax_rate", 0.15)
        self.service.add_invoice(invoice_number, customer_name, self.current_invoice_items, tax_rate)
        self.current_invoice_items = []
        self.invoice_tree.delete(*self.invoice_tree.get_children())
        messagebox.showinfo("Success", "Invoice created successfully.")
        self.reload_data()

    def build_inventory_tab(self):
        form = ttk.Frame(self.inventory_tab)
        form.pack(fill=tk.X, padx=10, pady=10)

        fields = [
            (self.t("product_code"), "code"),
            (self.t("product_name"), "name"),
            (self.t("product_category"), "category"),
            (self.t("unit"), "unit"),
            (self.t("cost_price"), "cost_price"),
            (self.t("selling_price"), "selling_price"),
            (self.t("stock_quantity"), "stock_quantity"),
            (self.t("min_stock"), "min_stock"),
        ]

        self.product_vars = {}
        for idx, (label, key) in enumerate(fields):
            ttk.Label(form, text=label).grid(row=idx, column=0, sticky="w", padx=5, pady=4)
            var = tk.StringVar()
            self.product_vars[key] = var
            ttk.Entry(form, textvariable=var).grid(row=idx, column=1, padx=5, pady=4)

        ttk.Button(form, text=self.t("add_product"), command=self.add_product).grid(row=len(fields), column=0, columnspan=2, pady=8)

        columns = ("code", "name", "category", "unit", "cost_price", "selling_price", "stock_quantity", "min_stock")
        self.product_tree = ttk.Treeview(self.inventory_tab, columns=columns, show="headings")
        for col in columns:
            self.product_tree.heading(col, text=col)
            self.product_tree.column(col, width=120)
        self.product_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def add_product(self):
        required = ["code", "name", "category", "unit", "cost_price", "selling_price", "stock_quantity", "min_stock"]
        values = []
        for key in required:
            values.append(self.product_vars[key].get())
        try:
            self.service.add_product(values[0], values[1], values[2], values[3], float(values[4]), float(values[5]), float(values[6]), float(values[7]))
            messagebox.showinfo("Success", "Product added successfully.")
            self.reload_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Could not add product: {exc}")

    def build_payroll_tab(self):
        form = ttk.Frame(self.payroll_tab)
        form.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(form, text=self.t("employee_name")).grid(row=0, column=0, sticky="w", padx=5, pady=4)
        self.employee_name_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.employee_name_var).grid(row=0, column=1, padx=5, pady=4)

        ttk.Label(form, text=self.t("position")).grid(row=1, column=0, sticky="w", padx=5, pady=4)
        self.position_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.position_var).grid(row=1, column=1, padx=5, pady=4)

        ttk.Label(form, text=self.t("salary")).grid(row=2, column=0, sticky="w", padx=5, pady=4)
        self.salary_var = tk.StringVar(value="0")
        ttk.Entry(form, textvariable=self.salary_var).grid(row=2, column=1, padx=5, pady=4)

        ttk.Label(form, text=self.t("bonus")).grid(row=3, column=0, sticky="w", padx=5, pady=4)
        self.bonus_var = tk.StringVar(value="0")
        ttk.Entry(form, textvariable=self.bonus_var).grid(row=3, column=1, padx=5, pady=4)

        ttk.Label(form, text=self.t("deductions")).grid(row=4, column=0, sticky="w", padx=5, pady=4)
        self.deductions_var = tk.StringVar(value="0")
        ttk.Entry(form, textvariable=self.deductions_var).grid(row=4, column=1, padx=5, pady=4)

        ttk.Label(form, text=self.t("period")).grid(row=5, column=0, sticky="w", padx=5, pady=4)
        self.period_var = tk.StringVar(value="2026-10")
        ttk.Entry(form, textvariable=self.period_var).grid(row=5, column=1, padx=5, pady=4)

        ttk.Button(form, text=self.t("add_employee"), command=self.add_employee).grid(row=6, column=0, columnspan=2, pady=8)
        ttk.Button(form, text=self.t("generate_payroll"), command=self.generate_payroll).grid(row=7, column=0, columnspan=2, pady=8)

        columns = ("employee_name", "period", "gross_salary", "bonus", "deductions", "net_salary")
        self.payroll_tree = ttk.Treeview(self.payroll_tab, columns=columns, show="headings")
        for col in columns:
            self.payroll_tree.heading(col, text=col)
            self.payroll_tree.column(col, width=120)
        self.payroll_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def add_employee(self):
        try:
            self.service.add_employee(
                self.employee_name_var.get(),
                self.position_var.get(),
                float(self.salary_var.get()),
                float(self.bonus_var.get()),
                float(self.deductions_var.get()),
                "",
            )
            messagebox.showinfo("Success", "Employee added successfully.")
            self.reload_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Could not add employee: {exc}")

    def generate_payroll(self):
        employees = self.service.list_employees()
        if not employees:
            messagebox.showwarning("Warning", "No employees available.")
            return
        for emp in employees:
            gross = float(emp.get("salary", 0))
            bonus = float(emp.get("bonus", 0))
            deductions = float(emp.get("deductions", 0))
            self.service.add_payroll(emp["id"], self.period_var.get(), gross, bonus, deductions)
        messagebox.showinfo("Success", "Payroll generated successfully.")
        self.reload_data()

    def build_settings_tab(self):
        form = ttk.Frame(self.settings_tab)
        form.pack(fill=tk.X, padx=10, pady=10)

        self.settings_company_var = tk.StringVar(value=self.service.get_company().get("name", APP_COMPANY))
        self.settings_country_var = tk.StringVar(value=self.service.get_company().get("country", "Saudi Arabia"))
        self.settings_currency_var = tk.StringVar(value=self.service.get_company().get("currency", "USD"))
        self.settings_tax_var = tk.StringVar(value=str(self.service.get_company().get("tax_rate", 0.15)))
        self.settings_language_var = tk.StringVar(value=self.service.get_company().get("language", "en"))

        fields = [
            (self.t("company_name"), self.settings_company_var),
            (self.t("country"), self.settings_country_var),
            (self.t("currency"), self.settings_currency_var),
            (self.t("tax_rate"), self.settings_tax_var),
            (self.t("language"), self.settings_language_var),
        ]

        for idx, (label, var) in enumerate(fields):
            ttk.Label(form, text=label).grid(row=idx, column=0, sticky="w", padx=5, pady=5)
            ttk.Entry(form, textvariable=var).grid(row=idx, column=1, padx=5, pady=5)

        ttk.Button(form, text=self.t("save"), command=self.save_settings).grid(row=len(fields), column=0, columnspan=2, pady=10)

    def save_settings(self):
        try:
            company = self.service.get_company()
            self.service.save_company(
                self.settings_company_var.get(),
                self.settings_country_var.get(),
                self.settings_currency_var.get(),
                float(self.settings_tax_var.get()),
                self.settings_language_var.get(),
            )
            self.lang = self.settings_language_var.get()
            self.translator = Translator(self.lang)
            self.notebook.tab(0, text=self.t("dashboard"))
            self.notebook.tab(1, text=self.t("invoices"))
            self.notebook.tab(2, text=self.t("inventory"))
            self.notebook.tab(3, text=self.t("payroll"))
            self.notebook.tab(4, text=self.t("settings"))
            messagebox.showinfo("Success", "Settings saved successfully.")
            self.reload_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Could not save settings: {exc}")

    def reload_data(self):
        summary = self.service.dashboard_summary()
        for key, value in summary.items():
            label = getattr(self, f"{key}_label", None)
            if label:
                label.config(text=str(value))

        self.product_tree.delete(*self.product_tree.get_children()) if hasattr(self, "product_tree") else None
        for product in self.service.list_products():
            self.product_tree.insert("", "end", values=(
                product.get("code", ""),
                product.get("name", ""),
                product.get("category", ""),
                product.get("unit", ""),
                product.get("cost_price", 0),
                product.get("selling_price", 0),
                product.get("stock_quantity", 0),
                product.get("min_stock", 0),
            ))

        self.payroll_tree.delete(*self.payroll_tree.get_children()) if hasattr(self, "payroll_tree") else None
        for row in self.service.list_payroll():
            self.payroll_tree.insert("", "end", values=(
                row.get("employee_name", ""),
                row.get("period", ""),
                row.get("gross_salary", 0),
                row.get("bonus", 0),
                row.get("deductions", 0),
                row.get("net_salary", 0),
            ))
