import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from services.report_service import export_summary_csv, get_report_data


class ReportsPanel:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.build_ui()
        self.refresh()

    def build_ui(self):
        top = ttk.Frame(self.frame)
        top.pack(fill=tk.X, pady=(0, 10))

        ttk.Button(top, text="Export CSV", command=self.export_csv).pack(side=tk.LEFT)
        ttk.Button(top, text="Refresh", command=self.refresh).pack(side=tk.LEFT, padx=(10, 0))

        self.tree = ttk.Treeview(self.frame, columns=("metric", "value"), show="headings")
        self.tree.heading("metric", text="Metric")
        self.tree.heading("value", text="Value")
        self.tree.column("metric", width=280)
        self.tree.column("value", width=180)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        data = get_report_data()
        rows = [
            ("Products", data["product_count"]),
            ("Total Units", data["total_units"]),
            ("Stock Value", data["stock_value"]),
            ("Invoices", data["invoice_count"]),
            ("Total Sales", data["total_sales"]),
            ("Total Payroll", data["total_payroll"]),
        ]
        for row in rows:
            self.tree.insert("", "end", values=row)

    def export_csv(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile="global_reports.csv",
        )
        if not path:
            return
        result = export_summary_csv(path)
        messagebox.showinfo("Export", f"Report exported to: {result}")
