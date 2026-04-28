"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""

# TODO: Implementar según README.md

import sys
try:
    cargaTotal = float(sys.argv[1])
    Soportess = float(sys.argv[2])
except (ValueError, IndexError):
    print("Error: Invalid input! Enter numeric values only.")
else:
    try:
        if Soportess == 0:
            print("Error: Cannot divide by zero. Supports must be greater than zero.")
    except:
        loadPerSupport = cargaTotal / Soportess
        print(f"Load per support point: {loadPerSupport:.2f} N")
    