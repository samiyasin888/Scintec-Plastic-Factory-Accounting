import tkinter as tk
from tkinter import ttk, messagebox

from config.config import APP_COMPANY
from database.db import initialize_database
from services.accounting_service import AccountingService
from services.translation_service import Translator
from ui.reports_panel import ReportsPanel


class GlobalAccountingApp:
    def __init__(self, root):
        initialize_database()
        self.root = root
        self.root.title("Global Accounting")
        self.root.geometry("1280x820")
        self.root.minsize(1100, 700)
        self.service = AccountingService()
        self.lang = self.service.get_language()
        self.translator = Translator(self.lang)
        self.current_invoice_items = []
        self.project_name = "Global"
        self.company_name_var = tk.StringVar()
        self.build_ui()
        self.apply_company_branding()
        self.reload_data()

    def t(self, key):
        return self.translator.t(key)

    def apply_company_branding(self):
        company = self.service.get_company() or {}
        company_name = company.get("name") or APP_COMPANY
        self.company_name_var.set(company_name)
        self.root.title(f"{company_name} - {self.t('app_title')}")
        if hasattr(self, "header_label"):
            self.header_label.config(text=f"{company_name}  |  {self.t('app_title')}")

    def build_ui(self):
        header = ttk.Frame(self.root, padding=(20, 14, 20, 8))
        header.pack(fill=tk.X)
        self.header_label = ttk.Label(
            header,
            text="",
            font=("Arial", 16, "bold"),
            foreground="#1f2937",
        )
        self.header_label.pack(anchor="w")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.dashboard_tab = ttk.Frame(self.notebook)
        self.invoice_tab = ttk.Frame(self.notebook)
        self.inventory_tab = ttk.Frame(self.notebook)
        self.payroll_tab = ttk.Frame(self.notebook)
        self.reports_tab = ttk.Frame(self.notebook)
        self.settings_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.dashboard_tab, text=self.t("dashboard"))
        self.notebook.add(self.invoice_tab, text=self.t("invoices"))
        self.notebook.add(self.inventory_tab, text=self.t("inventory"))
        self.notebook.add(self.payroll_tab, text=self.t("payroll"))
        self.notebook.add(self.reports_tab, text=self.t("reports"))
        self.notebook.add(self.settings_tab, text=self.t("settings"))

        self.build_dashboard()
        self.build_invoice_tab()
        self.build_inventory_tab()
        self.build_payroll_tab()
        self.build_reports_tab()
        self.build_settings_tab()

    def build_dashboard(self):
        summary_frame = ttk.Frame(self.dashboard_tab, padding=20)
        summary_frame.pack(fill=tk.BOTH, expand=True)

        cards = [
            (self.t("total_products"), "products"),
            (self.t("inventory_value"), "inventory_qty"),
            (self.t("total_invoices"), "invoices"),
            (self.t("sales_total"), "sales_total"),
            (self.t("employees_count"), "employees"),
        ]

        for idx, (label, key) in enumerate(cards):
            card = ttk.LabelFrame(summary_frame, text=label, padding=20)
            card.grid(row=0, column=idx, padx=12, pady=12, sticky="nsew")
            value = tk.Label(card, text="0", font=("Arial", 22, "bold"), fg="#2c3e50")
            value.pack(anchor="center", pady=15)
            setattr(self, f"{key}_label", value)

        for i in range(5):
            summary_frame.grid_columnconfigure(i, weight=1)

        report = ttk.LabelFrame(self.dashboard_tab, text="Quick Overview", padding=15)
        report.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        info = tk.Text(report, height=12, wrap=tk.WORD, font=("Arial", 11))
        info.pack(fill=tk.BOTH, expand=True)
        info.insert(tk.END, "Global Accounting Dashboard\n\n")
        info.insert(tk.END, "- Invoices module ready for sales and purchase management\n")
        info.insert(tk.END, "- Inventory module tracks stock, cost, and selling prices\n")
        info.insert(tk.END, "- Payroll module supports salary and deduction calculations\n")
        info.insert(tk.END, "- Settings allow company identity and bilingual support\n")
        info.configure(state=tk.DISABLED)

    def build_reports_tab(self):
        self.reports_panel = ReportsPanel(self.reports_tab)

    def build_invoice_tab(self):
        form = ttk.Frame(self.invoice_tab, padding=10)
        form.pack(fill=tk.X)

        ttk.Label(form, text=self.t("invoice_number")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.invoice_number_var = tk.StringVar(value="INV-001")
        ttk.Entry(form, textvariable=self.invoice_number_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form, text=self.t("customer_name")).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.customer_name_var = tk.StringVar(value="Walk-in Customer")
        ttk.Entry(form, textvariable=self.customer_name_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form, text=self.t("product_name")).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.product_name_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.product_name_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form, text=self.t("quantity")).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.quantity_var = tk.StringVar(value="1")
        ttk.Entry(form, textvariable=self.quantity_var).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(form, text=self.t("unit_price")).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.unit_price_var = tk.StringVar(value="0")
        ttk.Entry(form, textvariable=self.unit_price_var).grid(row=4, column=1, padx=5, pady=5)

        ttk.Button(form, text=self.t("add_item"), command=self.add_invoice_item).grid(row=5, column=0, padx=5, pady=10)
        ttk.Button(form, text=self.t("create_invoice"), command=self.create_invoice).grid(row=5, column=1, padx=5, pady=10)

        cols = ("name", "qty", "price", "total")
        self.invoice_tree = ttk.Treeview(self.invoice_tab, columns=cols, show="headings")
        for col in cols:
            self.invoice_tree.heading(col, text=col)
            self.invoice_tree.column(col, width=150)
        self.invoice_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def add_invoice_item(self):
        try:
            qty = float(self.quantity_var.get())
            price = float(self.unit_price_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid quantity and unit price.")
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

        customer = self.customer_name_var.get() or "Walk-in Customer"
        tax_rate = float(self.service.get_company().get("tax_rate", 0.15))
        self.service.add_invoice(self.invoice_number_var.get(), customer, self.current_invoice_items, tax_rate)
        self.current_invoice_items = []
        self.invoice_tree.delete(*self.invoice_tree.get_children())
        messagebox.showinfo("Success", "Invoice created successfully.")
        self.reload_data()
        if hasattr(self, "reports_panel"):
            self.reports_panel.refresh()

    def build_inventory_tab(self):
        form = ttk.Frame(self.inventory_tab, padding=10)
        form.pack(fill=tk.X)

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
            ttk.Label(form, text=label).grid(row=idx, column=0, sticky="w", padx=5, pady=5)
            var = tk.StringVar()
            self.product_vars[key] = var
            ttk.Entry(form, textvariable=var).grid(row=idx, column=1, padx=5, pady=5)

        ttk.Button(form, text=self.t("add_product"), command=self.add_product).grid(row=len(fields), column=0, columnspan=2, pady=10)

        cols = ("code", "name", "category", "unit", "cost_price", "selling_price", "stock_quantity", "min_stock")
        self.product_tree = ttk.Treeview(self.inventory_tab, columns=cols, show="headings")
        for col in cols:
            self.product_tree.heading(col, text=col)
            self.product_tree.column(col, width=120)
        self.product_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def add_product(self):
        try:
            self.service.add_product(
                self.product_vars["code"].get(),
                self.product_vars["name"].get(),
                self.product_vars["category"].get(),
                self.product_vars["unit"].get(),
                float(self.product_vars["cost_price"].get()),
                float(self.product_vars["selling_price"].get()),
                float(self.product_vars["stock_quantity"].get()),
                float(self.product_vars["min_stock"].get()),
            )
            messagebox.showinfo("Success", "Product added successfully.")
            self.reload_data()
            if hasattr(self, "reports_panel"):
                self.reports_panel.refresh()
        except Exception as exc:
            messagebox.showerror("Error", f"Could not add product: {exc}")

    def build_payroll_tab(self):
        form = ttk.Frame(self.payroll_tab, padding=10)
        form.pack(fill=tk.X)

        ttk.Label(form, text=self.t("employee_name")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.employee_name_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.employee_name_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form, text=self.t("position")).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.position_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.position_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form, text=self.t("salary")).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.salary_var = tk.StringVar(value="0")
        ttk.Entry(form, textvariable=self.salary_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form, text=self.t("bonus")).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.bonus_var = tk.StringVar(value="0")
        ttk.Entry(form, textvariable=self.bonus_var).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(form, text=self.t("deductions")).grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.deductions_var = tk.StringVar(value="0")
        ttk.Entry(form, textvariable=self.deductions_var).grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(form, text=self.t("period")).grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.period_var = tk.StringVar(value="2026-10")
        ttk.Entry(form, textvariable=self.period_var).grid(row=5, column=1, padx=5, pady=5)

        ttk.Button(form, text=self.t("add_employee"), command=self.add_employee).grid(row=6, column=0, padx=5, pady=10)
        ttk.Button(form, text=self.t("generate_payroll"), command=self.generate_payroll).grid(row=6, column=1, padx=5, pady=10)

        cols = ("employee_name", "period", "gross_salary", "bonus", "deductions", "net_salary")
        self.payroll_tree = ttk.Treeview(self.payroll_tab, columns=cols, show="headings")
        for col in cols:
            self.payroll_tree.heading(col, text=col)
            self.payroll_tree.column(col, width=150)
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
            if hasattr(self, "reports_panel"):
                self.reports_panel.refresh()
        except Exception as exc:
            messagebox.showerror("Error", f"Could not add employee: {exc}")

    def generate_payroll(self):
        employees = self.service.list_employees()
        if not employees:
            messagebox.showwarning("Warning", "No employees found.")
            return

        for emp in employees:
            self.service.add_payroll(
                emp["id"],
                self.period_var.get(),
                float(emp.get("salary", 0)),
                float(emp.get("bonus", 0)),
                float(emp.get("deductions", 0)),
            )

        messagebox.showinfo("Success", "Payroll generated successfully.")
        self.reload_data()
        if hasattr(self, "reports_panel"):
            self.reports_panel.refresh()

    def build_settings_tab(self):
        form = ttk.Frame(self.settings_tab, padding=20)
        form.pack(fill=tk.BOTH, expand=True)

        company = self.service.get_company() or {}
        self.company_name_var = tk.StringVar(value=company.get("name", APP_COMPANY))
        self.country_var = tk.StringVar(value=company.get("country", "Saudi Arabia"))
        self.currency_var = tk.StringVar(value=company.get("currency", "USD"))
        self.tax_var = tk.StringVar(value=str(company.get("tax_rate", 0.15)))
        self.language_var = tk.StringVar(value=company.get("language", "en"))

        fields = [
            (self.t("company_name"), self.company_name_var),
            (self.t("country"), self.country_var),
            (self.t("currency"), self.currency_var),
            (self.t("tax_rate"), self.tax_var),
            (self.t("language"), self.language_var),
        ]

        for idx, (label, var) in enumerate(fields):
            ttk.Label(form, text=label).grid(row=idx, column=0, sticky="w", padx=5, pady=8)
            ttk.Entry(form, textvariable=var, width=35).grid(row=idx, column=1, padx=5, pady=8)

        ttk.Button(form, text=self.t("save"), command=self.save_settings).grid(row=len(fields), column=0, columnspan=2, pady=15)

    def save_settings(self):
        try:
            self.service.save_company(
                self.company_name_var.get(),
                self.country_var.get(),
                self.currency_var.get(),
                float(self.tax_var.get()),
                self.language_var.get(),
            )
            self.lang = self.language_var.get()
            self.translator = Translator(self.lang)
            self.apply_company_branding()
            self.notebook.tab(0, text=self.t("dashboard"))
            self.notebook.tab(1, text=self.t("invoices"))
            self.notebook.tab(2, text=self.t("inventory"))
            self.notebook.tab(3, text=self.t("payroll"))
            self.notebook.tab(4, text=self.t("reports"))
            self.notebook.tab(5, text=self.t("settings"))
            messagebox.showinfo("Success", "Settings saved successfully.")
            self.reload_data()
            if hasattr(self, "reports_panel"):
                self.reports_panel.refresh()
        except Exception as exc:
            messagebox.showerror("Error", f"Could not save settings: {exc}")

    def reload_data(self):
        summary = self.service.dashboard_summary()
        for key, value in summary.items():
            label = getattr(self, f"{key}_label", None)
            if label:
                label.config(text=str(value))

        if hasattr(self, "product_tree"):
            self.product_tree.delete(*self.product_tree.get_children())
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

        if hasattr(self, "payroll_tree"):
            self.payroll_tree.delete(*self.payroll_tree.get_children())
            for row in self.service.list_payroll():
                self.payroll_tree.insert("", "end", values=(
                    row.get("employee_name", ""),
                    row.get("period", ""),
                    row.get("gross_salary", 0),
                    row.get("bonus", 0),
                    row.get("deductions", 0),
                    row.get("net_salary", 0),
                ))
