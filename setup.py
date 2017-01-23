import cx_Freeze
import sys
#import matplotlib
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Hamilton\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Hamilton\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tk8.6"

includes      = []
include_files = [r"C:\\Users\\Hamilton\\AppData\\Local\\Programs\\Python\\Python35\\DLLs\\tcl86t.dll", \
                 r"C:\\Users\\Hamilton\\AppData\\Local\\Programs\Python\\Python35\\DLLs\\tk86t.dll"]

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("vpn.py", icon="icon.ico", base=base)]

cx_Freeze.setup(
    name = "Disc",
    options = {"build_exe": {"includes":includes, "include_files": include_files}},
    version = "0.01",
    description = "Crying T.T",
    executables = executables
    )
