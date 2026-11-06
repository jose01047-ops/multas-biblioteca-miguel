import subprocess
import sys
from pathlib import Path

programa = Path(__file__).with_name("multas.py")

casos = [
    ("0\n2\n", "$0.00"),
    ("3\n2\n", "$12.00"),
    ("5\n1\n", "$10.00"),
    ("-1\n3\n", "Error:"),
    ("abc\n", "Error:"),
    ("2\n0\n", "$0.00"),
    ("2\n-1\n", "Error:")
]

for numero, (entrada, esperado) in enumerate(casos, 1):
    resultado = subprocess.run(
        [sys.executable, str(programa)],
        input=entrada,
        capture_output=True,
        text=True
    )
    assert resultado.returncode == 0
    assert esperado in resultado.stdout
    print(f"Prueba {numero}: correcta")

print("7 de 7 pruebas correctas")
