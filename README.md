# Global Accounting

Global Accounting is a desktop accounting and inventory management system designed for manufacturing and industrial businesses.

## Features
- Company branding and customization
- Arabic and English language support
- Currency, country, and tax settings
- Inventory tracking
- Invoice creation and export
- Payroll management
- Dashboard summary and reports
- Local SQLite database
- Desktop application packaging support for Windows

## Default Company
- Name: Scintec Plastic Factory
- Country: Saudi Arabia
- Currency: USD
- Tax Rate: 15%
- Language: English

## Project Structure
```
Scintec-Plastic-Factory-Accounting/
├── config/
│   └── config.py                 # Application configuration
├── database/
│   └── db.py                     # Database initialization
├── services/
│   ├── accounting_service.py     # Business logic and translations
│   ├── translation_service.py    # Data layer
│   └── report_service.py         # Reports and exports
├── ui/
│   ├── main_window.py           # Main application UI
│   └── reports_panel.py         # Reports interface
├── main.py                       # Entry point
├── build_app.py                 # Build script for Windows
├── build_windows.bat            # Windows build helper
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Run Locally

1. Install Python 3.10+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Build Windows Executable

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the build script:
   ```bash
   python build_app.py
   ```
   Or on Windows, double-click:
   ```bash
   build_windows.bat
   ```
3. The executable will be created at:
   ```text
   dist/GlobalAccounting.exe
   ```

## Data Storage

The database is stored in the user's local application folder for packaged desktop builds:

**Windows:**
```text
C:\Users\<username>\AppData\Local\GlobalAccounting\global.db
```

**Linux/macOS:**
```text
~/.global_accounting/GlobalAccounting/global.db
```

## Initial Setup

On first run, the application creates a default company:
- **Company Name:** Scintec Plastic Factory
- **Country:** Saudi Arabia
- **Currency:** USD
- **Tax Rate:** 15%
- **Language:** English

You can customize all settings in the "Settings" tab.

## Modules

### Dashboard
Displays key metrics:
- Total Products
- Inventory Quantity
- Total Invoices
- Sales Total
- Employee Count

### Invoices
- Create and manage sales invoices
- Add line items with product name, quantity, and unit price
- Automatic tax calculation
- Preview and export to CSV

### Inventory
- Track products with code, name, category, and unit
- Monitor cost price and selling price
- Manage stock quantities and minimum stock levels
- Automatic stock reduction on invoice creation

### Payroll
- Add employees with salary, bonus, and deduction details
- Generate monthly payroll
- Calculate net salary automatically
- View payroll history

### Reports
- Summary of business metrics
- Export reports to CSV
- Refresh data on demand

### Settings
- Customize company name
- Set country and currency
- Configure tax rate
- Switch between Arabic (ar) and English (en)

## System Requirements

- **Operating System:** Windows 7 or later (or Linux/macOS)
- **Python Version:** 3.10 or higher (if running from source)
- **RAM:** 256 MB minimum
- **Disk Space:** 100 MB for application and database

## Customization for Clients

This application is designed to be customized for multiple clients:
1. Each client gets their own installation of `GlobalAccounting.exe`
2. Database is isolated per user/installation
3. Company name and settings are customizable via the Settings tab
4. All data remains local and under client control

## Troubleshooting

**Database not found:**
The database is created automatically on first run in the AppData folder.

**Invoice export fails:**
Ensure the `data/invoices` directory exists or is writable.

**Language not changing:**
After changing language in Settings, restart the application for full UI refresh.

## Future Enhancements

- Multi-user login
- Cloud backup
- Advanced financial reports
- PDF invoice printing
- Customer and supplier management
- Purchase order tracking
- Email notifications

## License

This project is provided for internal and business use as part of the Global Accounting system.

## Support

For issues or feature requests, please contact the development team.
