"""
PyInstaller Build Script for Global Accounting
Creates a Windows executable from the Python source code
"""

import os
import sys

try:
    import PyInstaller.__main__
except ImportError:
    print("PyInstaller is not installed. Installing...")
    os.system(f"{sys.executable} -m pip install pyinstaller")
    import PyInstaller.__main__


def build_executable():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    arguments = [
        'main.py',
        '--name=GlobalAccounting',
        '--onefile',
        '--windowed',
        '--distpath=dist',
        '--workpath=build',
        '--specpath=specs',
        '-y',
    ]

    if os.path.exists(os.path.join(script_dir, 'icon.ico')):
        arguments.append('--icon=icon.ico')

    print("=" * 60)
    print("Global Accounting - Build Script")
    print("=" * 60)
    print("Building executable...")

    try:
        PyInstaller.__main__.run(arguments)
        print("\nBuild completed successfully.")
        print("Executable created at: dist/GlobalAccounting.exe")
        return 0
    except Exception as exc:
        print(f"Build failed: {exc}")
        return 1


if __name__ == '__main__':
    sys.exit(build_executable())
