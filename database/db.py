"""
Database Module - SQLite Connection and Initialization
Responsible for local database creation and connection management.
"""

import os
import sqlite3
from pathlib import Path


def get_app_data_path():
    if os.name == 'nt':
        app_data = os.getenv('APPDATA')
        app_folder = os.path.join(app_data, 'Global Accounting')
    else:
        app_folder = os.path.expanduser('~/.global_accounting/GlobalAccounting')
    Path(app_folder).mkdir(parents=True, exist_ok=True)
    return app_folder


def get_db_path():
    return os.path.join(get_app_data_path(), 'global.db')


def get_connection():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                country TEXT DEFAULT 'Saudi Arabia',
                currency TEXT DEFAULT 'USD',
                tax_rate REAL DEFAULT 15.0,
                language TEXT DEFAULT 'en',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE,
                name TEXT NOT NULL,
                category TEXT,
                unit TEXT,
                cost_price REAL DEFAULT 0,
                selling_price REAL DEFAULT 0,
                quantity INTEGER DEFAULT 0,
                min_quantity INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS invoices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoice_number TEXT UNIQUE,
                customer_name TEXT,
                date TEXT,
                subtotal REAL DEFAULT 0,
                tax_amount REAL DEFAULT 0,
                total REAL DEFAULT 0,
                status TEXT DEFAULT 'pending',
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS invoice_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoice_id INTEGER NOT NULL,
                product_id INTEGER,
                product_name TEXT,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                line_total REAL,
                FOREIGN KEY(invoice_id) REFERENCES invoices(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                emp_number TEXT UNIQUE,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                department TEXT,
                base_salary REAL DEFAULT 0,
                allowances REAL DEFAULT 0,
                deductions REAL DEFAULT 0,
                salary_type TEXT DEFAULT 'monthly',
                status TEXT DEFAULT 'active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payroll (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_id INTEGER NOT NULL,
                month TEXT NOT NULL,
                base_salary REAL,
                allowances REAL DEFAULT 0,
                deductions REAL DEFAULT 0,
                gross_salary REAL,
                net_salary REAL,
                paid_date TEXT,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY(employee_id) REFERENCES employees(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT DEFAULT 'admin',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()

        company = cursor.execute("SELECT * FROM companies WHERE id = 1").fetchone()
        if not company:
            cursor.execute(
                "INSERT INTO companies (name, country, currency, tax_rate, language) VALUES (?, ?, ?, ?, ?)",
                ('Scintec Plastic Factory', 'Saudi Arabia', 'USD', 15.0, 'en')
            )
            conn.commit()

        user = cursor.execute("SELECT * FROM users WHERE username = 'admin'").fetchone()
        if not user:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                ('admin', 'admin', 'admin')
            )
            conn.commit()

        print(f"Database initialized: {get_db_path()}")
    finally:
        conn.close()


if __name__ == '__main__':
    init_database()
