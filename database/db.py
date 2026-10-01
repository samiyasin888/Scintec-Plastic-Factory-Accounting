import sqlite3
from pathlib import Path

from config.config import DB_PATH


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                country TEXT,
                currency TEXT DEFAULT 'USD',
                tax_rate REAL DEFAULT 0.15,
                language TEXT DEFAULT 'en'
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE,
                name TEXT NOT NULL,
                category TEXT,
                unit TEXT,
                cost_price REAL DEFAULT 0,
                selling_price REAL DEFAULT 0,
                stock_quantity REAL DEFAULT 0,
                min_stock REAL DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                address TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                address TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS invoices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoice_number TEXT UNIQUE,
                invoice_date TEXT NOT NULL,
                customer_id INTEGER,
                customer_name TEXT,
                invoice_type TEXT DEFAULT 'sale',
                subtotal REAL DEFAULT 0,
                tax_amount REAL DEFAULT 0,
                total REAL DEFAULT 0,
                notes TEXT,
                FOREIGN KEY(customer_id) REFERENCES customers(id)
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS invoice_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoice_id INTEGER NOT NULL,
                product_id INTEGER,
                product_name TEXT NOT NULL,
                quantity REAL NOT NULL,
                unit_price REAL NOT NULL,
                total REAL NOT NULL,
                FOREIGN KEY(invoice_id) REFERENCES invoices(id),
                FOREIGN KEY(product_id) REFERENCES products(id)
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT,
                salary REAL DEFAULT 0,
                bonus REAL DEFAULT 0,
                deductions REAL DEFAULT 0,
                bank_account TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS payroll (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id INTEGER NOT NULL,
                period TEXT NOT NULL,
                gross_salary REAL DEFAULT 0,
                bonus REAL DEFAULT 0,
                deductions REAL DEFAULT 0,
                net_salary REAL DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(employee_id) REFERENCES employees(id)
            )
            """
        )

        conn.execute(
            "SELECT COUNT(*) FROM companies"
        )
        if conn.execute("SELECT COUNT(*) FROM companies").fetchone()[0] == 0:
            conn.execute(
                "INSERT INTO companies (name, country, currency, tax_rate, language) VALUES (?, ?, ?, ?, ?)",
                ("Scintec Plastic Factory", "Saudi Arabia", "USD", 0.15, "en"),
            )

        conn.commit()
    finally:
        conn.close()
