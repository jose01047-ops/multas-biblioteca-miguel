try:
    dias = int(input("Días de retraso: "))
    libros = int(input("Cantidad de libros: "))

    if dias < 0 or libros < 0:
        print("Error: no se admiten números negativos")
    else:
        multa = dias * libros * 2
        print(f"Multa total: ${multa:.2f}")

except ValueError:
    print("Error: escribe cantidades enteras")
