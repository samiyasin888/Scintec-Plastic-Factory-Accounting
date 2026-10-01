# Global - Accounting Software

Global is a professional accounting and ERP-style application built for factories and industrial businesses. It is designed to work fully offline, support Arabic and English, and be flexible enough to be sold to multiple companies.

## Features

- Offline-first desktop application
- Invoices and sales tracking
- Inventory and stock control
- Payroll management
- Company settings and language switching
- SQLite local database
- Export-friendly data structure
- Scalable architecture for resale to other businesses

## Tech Stack

- Python 3.10+
- Tkinter
- SQLite
- Standard library only for core functionality

## Project Goals

- Factory accounting workflow
- Plastic manufacturing use case
- Suitable for local installation without internet
- Ready to adapt to other industries

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Database Initialization

```bash
python scripts/init_db.py
```

## Project Structure

```text
.
├── README.md
├── requirements.txt
├── main.py
├── config/
│   ├── __init__.py
│   └── config.py
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── models.py
├── services/
│   ├── __init__.py
│   ├── accounting_service.py
│   └── translation_service.py
├── ui/
│   ├── __init__.py
│   └── main_window.py
├── scripts/
│   └── init_db.py
└── data/
    └── global.db
```

## Notes

This is the initial version of the system and is intended as a strong base for a commercial product.

---

Global - Smart accounting system for modern factories.
