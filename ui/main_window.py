import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from database.db import get_connection


class GlobalAccountingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Global Accounting")
        self.root.geometry("1400x820")
        self.root.minsize(1100, 700)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.dashboard_values = {
            'products': tk.StringVar(value='0'),
            'inventory': tk.StringVar(value='0'),
            'invoices': tk.StringVar(value='0'),
            'sales': tk.StringVar(value='0.00'),
            'employees': tk.StringVar(value='0'),
        }

        self.company_name_var = tk.StringVar()
        self.country_var = tk.StringVar()
        self.currency_var = tk.StringVar()
        self.tax_rate_var = tk.StringVar()
        self.language_var = tk.StringVar()

        self.product_id_var = tk.IntVar(value=0)
        self.product_code_var = tk.StringVar()
        self.product_name_var = tk.StringVar()
        self.product_category_var = tk.StringVar()
        self.product_unit_var = tk.StringVar()
        self.product_cost_var = tk.StringVar()
        self.product_price_var = tk.StringVar()
        self.product_qty_var = tk.StringVar()
        self.product_min_var = tk.StringVar()

        self.employee_id_var = tk.IntVar(value=0)
        self.employee_number_var = tk.StringVar()
        self.employee_first_var = tk.StringVar()
        self.employee_last_var = tk.StringVar()
        self.employee_email_var = tk.StringVar()
        self.employee_phone_var = tk.StringVar()
        self.employee_department_var = tk.StringVar()
        self.employee_base_salary_var = tk.StringVar()
        self.employee_allowances_var = tk.StringVar()
        self.employee_deductions_var = tk.StringVar()

        self.invoice_customer_var = tk.StringVar()
        self.invoice_product_var = tk.StringVar()
        self.invoice_qty_var = tk.StringVar(value='1')
        self.invoice_total_var = tk.StringVar(value='0.00')
        self.invoice_items = []

        self.build_ui()
        self.refresh_all()

    def build_ui(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        header = ttk.Frame(main_frame)
        header.pack(fill=tk.X)
        ttk.Label(header, text="Global Accounting", font=("Arial", 22, "bold")).pack(side=tk.LEFT)
        ttk.Label(header, text="Desktop Accounting & Inventory System", font=("Arial", 10), foreground="#666").pack(side=tk.LEFT, padx=15)

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10)

        self.dashboard_tab = ttk.Frame(self.notebook)
        self.products_tab = ttk.Frame(self.notebook)
        self.invoices_tab = ttk.Frame(self.notebook)
        self.payroll_tab = ttk.Frame(self.notebook)
        self.reports_tab = ttk.Frame(self.notebook)
        self.settings_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.dashboard_tab, text="Dashboard")
        self.notebook.add(self.products_tab, text="Products")
        self.notebook.add(self.invoices_tab, text="Invoices")
        self.notebook.add(self.payroll_tab, text="Payroll")
        self.notebook.add(self.reports_tab, text="Reports")
        self.notebook.add(self.settings_tab, text="Settings")

        self.build_dashboard_tab()
        self.build_products_tab()
        self.build_invoices_tab()
        self.build_payroll_tab()
        self.build_reports_tab()
        self.build_settings_tab()

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to exit Global Accounting?"):
            self.root.destroy()

    def build_dashboard_tab(self):
        frame = self.dashboard_tab
        ttk.Label(frame, text="Dashboard Overview", font=("Arial", 16, "bold")).pack(pady=20)

        metrics = ttk.Frame(frame)
        metrics.pack(fill=tk.BOTH, expand=True, padx=20)

        cards = [
            ("Total Products", 'products'),
            ("Inventory Qty", 'inventory'),
            ("Invoices", 'invoices'),
            ("Sales", 'sales'),
            ("Employees", 'employees'),
        ]

        for index, (label, key) in enumerate(cards):
            col = index % 3
            row = index // 3
            card = ttk.Frame(metrics, relief=tk.RIDGE, padding=12)
            card.grid(row=row, column=col, padx=12, pady=12, sticky='nsew')
            ttk.Label(card, text=label, font=("Arial", 10)).pack(anchor='w')
            ttk.Label(card, textvariable=self.dashboard_values[key], font=("Arial", 18, "bold"), foreground="#2e7d32").pack(anchor='w', pady=(10, 0))

        for i in range(3):
            metrics.grid_columnconfigure(i, weight=1)

    def build_products_tab(self):
        frame = self.products_tab
        left = ttk.Frame(frame)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        right = ttk.Frame(frame)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(left, text="Product Form", font=("Arial", 12, "bold")).pack(anchor='w', pady=(0, 10))

        fields = [
            ("Code", self.product_code_var),
            ("Name", self.product_name_var),
            ("Category", self.product_category_var),
            ("Unit", self.product_unit_var),
            ("Cost Price", self.product_cost_var),
            ("Selling Price", self.product_price_var),
            ("Quantity", self.product_qty_var),
            ("Minimum Qty", self.product_min_var),
        ]

        for label, var in fields:
            ttk.Label(left, text=label).pack(anchor='w', pady=(8, 2))
            ttk.Entry(left, textvariable=var, width=30).pack(anchor='w', pady=(0, 5))

        btns = ttk.Frame(left)
        btns.pack(fill=tk.X, pady=10)
        ttk.Button(btns, text="Save Product", command=self.save_product).pack(side=tk.LEFT, padx=3)
        ttk.Button(btns, text="Clear", command=self.clear_product_form).pack(side=tk.LEFT, padx=3)
        ttk.Button(btns, text="Delete", command=self.delete_product).pack(side=tk.LEFT, padx=3)

        columns = ("code", "name", "category", "unit", "qty", "price")
        self.product_tree = ttk.Treeview(right, columns=columns, show='headings')
        for column, heading in [('code', 'Code'), ('name', 'Name'), ('category', 'Category'), ('unit', 'Unit'), ('qty', 'Qty'), ('price', 'Price')]:
            self.product_tree.heading(column, text=heading)
            self.product_tree.column(column, width=120, anchor='center')
        self.product_tree.pack(fill=tk.BOTH, expand=True)
        self.product_tree.bind('<<TreeviewSelect>>', self.on_product_select)

    def build_invoices_tab(self):
        frame = self.invoices_tab
        left = ttk.Frame(frame)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        right = ttk.Frame(frame)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(left, text="Create Invoice", font=("Arial", 12, "bold")).pack(anchor='w', pady=(0, 10))

        ttk.Label(left, text="Customer Name").pack(anchor='w')
        ttk.Entry(left, textvariable=self.invoice_customer_var, width=40).pack(anchor='w', pady=(0, 10))

        ttk.Label(left, text="Product").pack(anchor='w')
        self.invoice_product_combo = ttk.Combobox(left, textvariable=self.invoice_product_var, state='readonly', width=37)
        self.invoice_product_combo.pack(anchor='w', pady=(0, 10))

        ttk.Label(left, text="Quantity").pack(anchor='w')
        ttk.Entry(left, textvariable=self.invoice_qty_var, width=20).pack(anchor='w', pady=(0, 10))

        ttk.Button(left, text="Add Item", command=self.add_invoice_item).pack(anchor='w', pady=(0, 10))
        ttk.Button(left, text="Save Invoice", command=self.save_invoice).pack(anchor='w', pady=(0, 10))
        ttk.Button(left, text="Clear Invoice", command=self.clear_invoice_form).pack(anchor='w')

        ttk.Label(left, text="Total").pack(anchor='w', pady=(10, 2))
        ttk.Entry(left, textvariable=self.invoice_total_var, state='readonly', width=20).pack(anchor='w')

        columns = ('item', 'product', 'qty', 'price', 'total')
        self.invoice_tree = ttk.Treeview(right, columns=columns, show='headings')
        for col, heading in [('item', 'Item'), ('product', 'Product'), ('qty', 'Qty'), ('price', 'Price'), ('total', 'Total')]:
            self.invoice_tree.heading(col, text=heading)
            self.invoice_tree.column(col, width=120, anchor='center')
        self.invoice_tree.pack(fill=tk.BOTH, expand=True)

    def build_payroll_tab(self):
        frame = self.payroll_tab
        left = ttk.Frame(frame)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        right = ttk.Frame(frame)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(left, text="Employee Form", font=("Arial", 12, "bold")).pack(anchor='w', pady=(0, 10))

        fields = [
            ('Employee Number', self.employee_number_var),
            ('First Name', self.employee_first_var),
            ('Last Name', self.employee_last_var),
            ('Email', self.employee_email_var),
            ('Phone', self.employee_phone_var),
            ('Department', self.employee_department_var),
            ('Base Salary', self.employee_base_salary_var),
            ('Allowances', self.employee_allowances_var),
            ('Deductions', self.employee_deductions_var),
        ]

        for label, var in fields:
            ttk.Label(left, text=label).pack(anchor='w', pady=(8, 2))
            ttk.Entry(left, textvariable=var, width=30).pack(anchor='w', pady=(0, 5))

        btns = ttk.Frame(left)
        btns.pack(fill=tk.X, pady=10)
        ttk.Button(btns, text="Save Employee", command=self.save_employee).pack(side=tk.LEFT, padx=3)
        ttk.Button(btns, text="Clear", command=self.clear_employee_form).pack(side=tk.LEFT, padx=3)
        ttk.Button(btns, text="Delete", command=self.delete_employee).pack(side=tk.LEFT, padx=3)

        columns = ('number', 'first', 'last', 'department', 'salary', 'net')
        self.employee_tree = ttk.Treeview(right, columns=columns, show='headings')
        for col, heading in [('number', 'No.'), ('first', 'First Name'), ('last', 'Last Name'), ('department', 'Department'), ('salary', 'Salary'), ('net', 'Net')]:
            self.employee_tree.heading(col, text=heading)
            self.employee_tree.column(col, width=120, anchor='center')
        self.employee_tree.pack(fill=tk.BOTH, expand=True)
        self.employee_tree.bind('<<TreeviewSelect>>', self.on_employee_select)

    def build_reports_tab(self):
        frame = self.reports_tab
        ttk.Label(frame, text="Reports & Analytics", font=("Arial", 14, "bold")).pack(pady=10)

        top = ttk.Frame(frame)
        top.pack(fill=tk.X, padx=20, pady=10)
        ttk.Button(top, text="Generate Summary", command=self.generate_summary_report).pack(side=tk.LEFT)

        self.report_text = tk.Text(frame, height=25, width=120)
        self.report_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def build_settings_tab(self):
        frame = self.settings_tab
        ttk.Label(frame, text="Company Settings", font=("Arial", 14, "bold")).pack(pady=10)

        form = ttk.Frame(frame)
        form.pack(fill=tk.BOTH, expand=True, padx=20)

        settings = [
            ('Company Name', self.company_name_var),
            ('Country', self.country_var),
            ('Currency', self.currency_var),
            ('Tax Rate %', self.tax_rate_var),
            ('Language (en/ar)', self.language_var),
        ]

        for label, var in settings:
            ttk.Label(form, text=label).pack(anchor='w', pady=(8, 2))
            ttk.Entry(form, textvariable=var, width=40).pack(anchor='w', pady=(0, 8))

        ttk.Button(form, text="Save Settings", command=self.save_settings).pack(anchor='w', pady=10)

    def refresh_all(self):
        self.load_company_settings()
        self.refresh_dashboard()
        self.refresh_products()
        self.refresh_invoices()
        self.refresh_employees()
        self.generate_summary_report()

    def load_company_settings(self):
        conn = get_connection()
        try:
            company = conn.execute("SELECT * FROM companies WHERE id = 1").fetchone()
            if company:
                self.company_name_var.set(company['name'])
                self.country_var.set(company['country'])
                self.currency_var.set(company['currency'])
                self.tax_rate_var.set(str(company['tax_rate']))
                self.language_var.set(company['language'])
        finally:
            conn.close()

    def refresh_dashboard(self):
        conn = get_connection()
        try:
            products_count = conn.execute("SELECT COUNT(*) as c FROM products").fetchone()['c']
            inventory_total = conn.execute("SELECT COALESCE(SUM(quantity), 0) as total FROM products").fetchone()['total']
            invoices_count = conn.execute("SELECT COUNT(*) as c FROM invoices").fetchone()['c']
            sales_total = conn.execute("SELECT COALESCE(SUM(total), 0) as total FROM invoices").fetchone()['total']
            employees_count = conn.execute("SELECT COUNT(*) as c FROM employees").fetchone()['c']

            self.dashboard_values['products'].set(str(products_count))
            self.dashboard_values['inventory'].set(str(inventory_total))
            self.dashboard_values['invoices'].set(str(invoices_count))
            self.dashboard_values['sales'].set(f"{float(sales_total):.2f}")
            self.dashboard_values['employees'].set(str(employees_count))
        finally:
            conn.close()

    def clear_product_form(self):
        self.product_id_var.set(0)
        self.product_code_var.set('')
        self.product_name_var.set('')
        self.product_category_var.set('')
        self.product_unit_var.set('')
        self.product_cost_var.set('')
        self.product_price_var.set('')
        self.product_qty_var.set('')
        self.product_min_var.set('')

    def on_product_select(self, event):
        selection = self.product_tree.selection()
        if not selection:
            return
        row = self.product_tree.item(selection[0], 'values')
        if not row:
            return
        code = row[0]
        conn = get_connection()
        try:
            product = conn.execute("SELECT * FROM products WHERE code = ?", (code,)).fetchone()
            if product:
                self.product_id_var.set(product['id'])
                self.product_code_var.set(product['code'])
                self.product_name_var.set(product['name'])
                self.product_category_var.set(product['category'] or '')
                self.product_unit_var.set(product['unit'] or '')
                self.product_cost_var.set(str(product['cost_price']))
                self.product_price_var.set(str(product['selling_price']))
                self.product_qty_var.set(str(product['quantity']))
                self.product_min_var.set(str(product['min_quantity']))
        finally:
            conn.close()

    def save_product(self):
        name = self.product_name_var.get().strip()
        code = self.product_code_var.get().strip()
        if not name or not code:
            messagebox.showwarning('Warning', 'Product name and code are required.')
            return

        conn = get_connection()
        try:
            data = (
                code,
                name,
                self.product_category_var.get().strip(),
                self.product_unit_var.get().strip(),
                float(self.product_cost_var.get() or 0),
                float(self.product_price_var.get() or 0),
                int(self.product_qty_var.get() or 0),
                int(self.product_min_var.get() or 0),
            )

            if self.product_id_var.get() == 0:
                conn.execute(
                    "INSERT INTO products (code, name, category, unit, cost_price, selling_price, quantity, min_quantity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    data
                )
            else:
                conn.execute(
                    "UPDATE products SET code = ?, name = ?, category = ?, unit = ?, cost_price = ?, selling_price = ?, quantity = ?, min_quantity = ? WHERE id = ?",
                    (*data, self.product_id_var.get())
                )
            conn.commit()
            messagebox.showinfo('Success', 'Product saved successfully')
            self.clear_product_form()
            self.refresh_products()
            self.refresh_dashboard()
        except Exception as exc:
            messagebox.showerror('Error', f'Could not save product: {exc}')
        finally:
            conn.close()

    def delete_product(self):
        if self.product_id_var.get() == 0:
            messagebox.showwarning('Warning', 'Please select a product first.')
            return
        if messagebox.askyesno('Delete', 'Delete selected product?'):
            conn = get_connection()
            try:
                conn.execute('DELETE FROM products WHERE id = ?', (self.product_id_var.get(),))
                conn.commit()
                self.clear_product_form()
                self.refresh_products()
                self.refresh_dashboard()
            finally:
                conn.close()

    def refresh_products(self):
        for row in self.product_tree.get_children():
            self.product_tree.delete(row)

        conn = get_connection()
        try:
            rows = conn.execute('SELECT * FROM products ORDER BY name').fetchall()
            for product in rows:
                self.product_tree.insert('', 'end', values=(
                    product['code'],
                    product['name'],
                    product['category'] or '',
                    product['unit'] or '',
                    product['quantity'],
                    f"{product['selling_price']:.2f}"
                ))
        finally:
            conn.close()

    def clear_invoice_form(self):
        self.invoice_customer_var.set('')
        self.invoice_product_var.set('')
        self.invoice_qty_var.set('1')
        self.invoice_total_var.set('0.00')
        self.invoice_items = []
        self.invoice_tree.delete(*self.invoice_tree.get_children())
        self.load_product_choices()

    def load_product_choices(self):
        conn = get_connection()
        try:
            products = conn.execute('SELECT id, name, selling_price FROM products ORDER BY name').fetchall()
            choices = [p['name'] for p in products]
            self.invoice_product_combo['values'] = choices
        finally:
            conn.close()

    def add_invoice_item(self):
        product_name = self.invoice_product_var.get().strip()
        qty = self.invoice_qty_var.get().strip()
        if not product_name or not qty:
            messagebox.showwarning('Warning', 'Please choose a product and quantity.')
            return

        try:
            qty_num = int(qty)
        except ValueError:
            messagebox.showwarning('Warning', 'Quantity must be a number.')
            return

        conn = get_connection()
        try:
            product = conn.execute('SELECT * FROM products WHERE name = ?', (product_name,)).fetchone()
            if not product:
                messagebox.showwarning('Warning', 'Selected product not found.')
                return
            price = float(product['selling_price'])
            total = qty_num * price
            self.invoice_items.append({
                'product_id': product['id'],
                'product_name': product['name'],
                'qty': qty_num,
                'price': price,
                'total': total,
            })
        finally:
            conn.close()

        self.invoice_tree.delete(*self.invoice_tree.get_children())
        total_all = 0.0
        for index, item in enumerate(self.invoice_items, start=1):
            self.invoice_tree.insert('', 'end', values=(index, item['product_name'], item['qty'], f"{item['price']:.2f}", f"{item['total']:.2f}"))
            total_all += item['total']
        self.invoice_total_var.set(f"{total_all:.2f}")
        self.invoice_qty_var.set('1')
        self.invoice_product_var.set('')

    def save_invoice(self):
        customer_name = self.invoice_customer_var.get().strip()
        if not customer_name or not self.invoice_items:
            messagebox.showwarning('Warning', 'Customer name and at least one invoice item are required.')
            return

        company = get_connection().execute('SELECT * FROM companies WHERE id = 1').fetchone()
        tax_rate = float(company['tax_rate']) if company else 15.0
        subtotal = sum(item['total'] for item in self.invoice_items)
        tax = subtotal * (tax_rate / 100.0)
        total = subtotal + tax

        conn = get_connection()
        try:
            invoice_number = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            conn.execute(
                "INSERT INTO invoices (invoice_number, customer_name, date, subtotal, tax_amount, total, status) VALUES (?, ?, ?, ?, ?, ?, 'paid')",
                (invoice_number, customer_name, datetime.now().strftime('%Y-%m-%d'), subtotal, tax, total)
            )
            invoice_id = conn.execute("SELECT last_insert_rowid() as id").fetchone()['id']
            for item in self.invoice_items:
                conn.execute(
                    "INSERT INTO invoice_items (invoice_id, product_id, product_name, quantity, unit_price, line_total) VALUES (?, ?, ?, ?, ?, ?)",
                    (invoice_id, item['product_id'], item['product_name'], item['qty'], item['price'], item['total'])
                )
                conn.execute(
                    "UPDATE products SET quantity = quantity - ? WHERE id = ?",
                    (item['qty'], item['product_id'])
                )
            conn.commit()
            messagebox.showinfo('Success', f'Invoice saved successfully: {invoice_number}')
            self.clear_invoice_form()
            self.refresh_dashboard()
            self.refresh_products()
            self.refresh_invoices()
        except Exception as exc:
            messagebox.showerror('Error', f'Failed to save invoice: {exc}')
        finally:
            conn.close()

    def refresh_invoices(self):
        # not used for tree view, but ensure product choices loaded
        self.load_product_choices()

    def clear_employee_form(self):
        self.employee_id_var.set(0)
        self.employee_number_var.set('')
        self.employee_first_var.set('')
        self.employee_last_var.set('')
        self.employee_email_var.set('')
        self.employee_phone_var.set('')
        self.employee_department_var.set('')
        self.employee_base_salary_var.set('')
        self.employee_allowances_var.set('')
        self.employee_deductions_var.set('')

    def on_employee_select(self, event):
        selection = self.employee_tree.selection()
        if not selection:
            return
        row = self.employee_tree.item(selection[0], 'values')
        if not row:
            return
        emp_no = row[0]
        conn = get_connection()
        try:
            employee = conn.execute("SELECT * FROM employees WHERE emp_number = ?", (emp_no,)).fetchone()
            if employee:
                self.employee_id_var.set(employee['id'])
                self.employee_number_var.set(employee['emp_number'])
                self.employee_first_var.set(employee['first_name'])
                self.employee_last_var.set(employee['last_name'])
                self.employee_email_var.set(employee['email'] or '')
                self.employee_phone_var.set(employee['phone'] or '')
                self.employee_department_var.set(employee['department'] or '')
                self.employee_base_salary_var.set(str(employee['base_salary']))
                self.employee_allowances_var.set(str(employee['allowances']))
                self.employee_deductions_var.set(str(employee['deductions']))
        finally:
            conn.close()

    def save_employee(self):
        first_name = self.employee_first_var.get().strip()
        last_name = self.employee_last_var.get().strip()
        if not first_name or not last_name:
            messagebox.showwarning('Warning', 'First and last name are required.')
            return

        conn = get_connection()
        try:
            emp_number = self.employee_number_var.get().strip() or f"EMP-{datetime.now().strftime('%d%m%Y%H%M%S')}"
            base = float(self.employee_base_salary_var.get() or 0)
            allow = float(self.employee_allowances_var.get() or 0)
            deduct = float(self.employee_deductions_var.get() or 0)
            if self.employee_id_var.get() == 0:
                conn.execute(
                    "INSERT INTO employees (emp_number, first_name, last_name, email, phone, department, base_salary, allowances, deductions) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (emp_number, first_name, last_name, self.employee_email_var.get().strip(), self.employee_phone_var.get().strip(), self.employee_department_var.get().strip(), base, allow, deduct)
                )
            else:
                conn.execute(
                    "UPDATE employees SET emp_number = ?, first_name = ?, last_name = ?, email = ?, phone = ?, department = ?, base_salary = ?, allowances = ?, deductions = ? WHERE id = ?",
                    (emp_number, first_name, last_name, self.employee_email_var.get().strip(), self.employee_phone_var.get().strip(), self.employee_department_var.get().strip(), base, allow, deduct, self.employee_id_var.get())
                )
            conn.commit()
            messagebox.showinfo('Success', 'Employee saved successfully')
            self.clear_employee_form()
            self.refresh_employees()
        finally:
            conn.close()

    def delete_employee(self):
        if self.employee_id_var.get() == 0:
            messagebox.showwarning('Warning', 'Please select an employee first.')
            return
        if messagebox.askyesno('Delete', 'Delete selected employee?'):
            conn = get_connection()
            try:
                conn.execute('DELETE FROM employees WHERE id = ?', (self.employee_id_var.get(),))
                conn.commit()
                self.clear_employee_form()
                self.refresh_employees()
            finally:
                conn.close()

    def refresh_employees(self):
        for row in self.employee_tree.get_children():
            self.employee_tree.delete(row)

        conn = get_connection()
        try:
            rows = conn.execute('SELECT * FROM employees ORDER BY last_name').fetchall()
            for emp in rows:
                net = (float(emp['base_salary']) + float(emp['allowances'])) - float(emp['deductions'])
                self.employee_tree.insert('', 'end', values=(
                    emp['emp_number'],
                    emp['first_name'],
                    emp['last_name'],
                    emp['department'] or '',
                    f"{float(emp['base_salary']):.2f}",
                    f"{net:.2f}"
                ))
        finally:
            conn.close()

    def save_settings(self):
        conn = get_connection()
        try:
            conn.execute(
                "UPDATE companies SET name = ?, country = ?, currency = ?, tax_rate = ?, language = ? WHERE id = 1",
                (
                    self.company_name_var.get().strip(),
                    self.country_var.get().strip(),
                    self.currency_var.get().strip(),
                    float(self.tax_rate_var.get() or 0),
                    self.language_var.get().strip(),
                )
            )
            conn.commit()
            messagebox.showinfo('Success', 'Settings saved successfully')
        finally:
            conn.close()

    def generate_summary_report(self):
        conn = get_connection()
        try:
            product_count = conn.execute('SELECT COUNT(*) as c FROM products').fetchone()['c']
            inventory_total = conn.execute('SELECT COALESCE(SUM(quantity), 0) as total FROM products').fetchone()['total']
            invoice_count = conn.execute('SELECT COUNT(*) as c FROM invoices').fetchone()['c']
            sales_total = conn.execute('SELECT COALESCE(SUM(total), 0) as total FROM invoices').fetchone()['total']
            employees_count = conn.execute('SELECT COUNT(*) as c FROM employees').fetchone()['c']
            tax_total = conn.execute('SELECT COALESCE(SUM(tax_amount), 0) as total FROM invoices').fetchone()['total']

            report = []
            report.append("Global Accounting - Summary Report")
            report.append("=" * 60)
            report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            report.append(f"Total Products: {product_count}")
            report.append(f"Total Inventory Quantity: {inventory_total}")
            report.append(f"Total Invoices: {invoice_count}")
            report.append(f"Total Sales: {float(sales_total):.2f}")
            report.append(f"Total Tax Collected: {float(tax_total):.2f}")
            report.append(f"Total Employees: {employees_count}")
            report.append("=" * 60)
            report_text = "\n".join(report)
            self.report_text.delete('1.0', tk.END)
            self.report_text.insert(tk.END, report_text)
        finally:
            conn.close()
