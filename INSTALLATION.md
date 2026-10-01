# Global Accounting - Installation and Deployment Guide

## Quick Start for End Users

### Option 1: Using the Windows Installer (Recommended)

1. Download `GlobalAccounting-Setup-1.0.0.exe`
2. Double-click the installer
3. Follow the installation wizard
4. Choose installation location (default: `C:\Program Files\Global Accounting`)
5. Create desktop shortcut (optional)
6. Click "Install"
7. The application will launch automatically after installation

### Option 2: Portable Executable

1. Download `GlobalAccounting.exe`
2. Place it in any folder
3. Double-click to run
4. No installation required
5. Data will be stored in: `C:\Users\<your-username>\AppData\Local\GlobalAccounting\`

## Installation Paths

### Application Files
```
Windows Installer:
C:\Program Files\Global Accounting\GlobalAccounting.exe

Portable:
Any folder of your choice
```

### User Data & Database
All user data is stored in:
```
C:\Users\<your-username>\AppData\Local\GlobalAccounting\global.db
```

This ensures:
- Data persistence across application updates
- Multiple users can have separate databases on the same computer
- Safe backup location

## Building the Installer (For Developers)

### Prerequisites
- Python 3.10+
- Inno Setup 6.2+ (for creating the installer)
- PyInstaller

### Step 1: Build the Executable
```bash
python build_app.py
```
This creates: `dist/GlobalAccounting.exe`

### Step 2: Create the Installer
1. Install Inno Setup from: https://jrsoftware.org/isdl.php
2. Open `setup.iss` with Inno Setup
3. Click "Build" → "Compile"
4. The installer will be created in: `dist/installer/GlobalAccounting-Setup-1.0.0.exe`

### Step 3: Distribution
- Share `GlobalAccounting-Setup-1.0.0.exe` with clients
- Or share portable `GlobalAccounting.exe` if installer not needed

## First Run Setup

On first launch, the application will:
1. Create the database folder in AppData
2. Initialize the database with default schema
3. Set default company: "Scintec Plastic Factory"
4. Load default settings (English language, USD currency, Saudi Arabia)

### Customizing Company Information
1. Open the application
2. Go to **Settings** tab
3. Update:
   - Company Name
   - Country
   - Currency
   - Tax Rate
   - Language (Arabic/English)
4. Click **Save**

## Backup and Recovery

### Backup User Data
To backup all business data:
```
Copy: C:\Users\<your-username>\AppData\Local\GlobalAccounting\global.db
To: Your backup location
```

### Restore from Backup
```
Replace: C:\Users\<your-username>\AppData\Local\GlobalAccounting\global.db
With: Your backup file
```

### Manual Database Reset
To start fresh with a new database:
1. Delete: `C:\Users\<your-username>\AppData\Local\GlobalAccounting\global.db`
2. Restart the application
3. A new database will be created automatically

## System Requirements

| Requirement | Minimum |
|---|---|
| Operating System | Windows 7 SP1 or later |
| RAM | 256 MB |
| Disk Space | 100 MB |
| Display | 1024x768 resolution |
| Internet | Not required (offline application) |

## Uninstallation

### Using Windows Installer
1. Go to **Control Panel** → **Programs and Features**
2. Find "Global Accounting"
3. Click **Uninstall**
4. Follow the uninstaller wizard

**Note:** Uninstalling does NOT delete user data in `AppData\Local\GlobalAccounting\`

### Portable Version
Simply delete the `GlobalAccounting.exe` file. User data remains in AppData.

## Troubleshooting

### Database not found on startup
- The database is created automatically
- Check folder permissions in `AppData\Local\GlobalAccounting\`
- Try running as Administrator

### Application crashes on startup
- Check Windows Event Viewer for error details
- Reinstall the application
- Ensure you have write permissions to AppData folder

### Data not saving
- Verify disk space availability
- Check folder permissions
- Close other instances of the application

### Invoice export fails
- Ensure you have write permissions to the export directory
- Try exporting to a different location (e.g., Desktop)

## Multi-Client Deployment

For deploying to multiple clients:

1. Each client gets their own installation
2. Each installation has its own database in AppData
3. Company settings are configured per installation
4. No shared server required (fully offline)

## Future Updates

When new versions are released:
1. Download the new installer
2. Run the installer
3. Choose the same installation folder
4. Existing data in AppData will be preserved
5. Application will continue with updated features

## Support and Documentation

- **User Manual:** See README.md in installation folder
- **Technical Support:** Contact Scintec Plastic Factory
- **Bug Reports:** Submit through official channels

## Version Information

**Current Version:** 1.0.0
**Release Date:** October 2026
**Platform:** Windows 7+
**Status:** Production Ready

---

For additional help or feature requests, please contact the development team.
