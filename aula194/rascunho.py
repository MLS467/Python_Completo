import sys


SYSTEM = sys.platform


if SYSTEM == "win32":
    print("Windows")
else:
    print("Linux")
