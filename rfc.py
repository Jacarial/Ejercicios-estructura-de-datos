
# Función para obtener la primera vocal de una cadena
def obtener_primera_vocal(cadena):
    vocales = "AEIOU"
    for letra in cadena:
        if letra.upper() in vocales:
            return letra.upper()
    return cadena[1].upper() if len(cadena) > 1 else 'X'

# Función para formatear el RFC
def generar_rfc(apellido_paterno, apellido_materno, primer_nombre, año, mes, día):
    # Obtener las primeras letras y la primera vocal
    primera_letra_ap = apellido_paterno[0].upper()
    primera_vocal_ap = obtener_primera_vocal(apellido_paterno)
    primera_letra_am = apellido_materno[0].upper()
    primera_letra_nombre = primer_nombre[0].upper()

    # Formatear fecha
    año = str(año)[-2:]  # Tomar los últimos dos dígitos del año

    # Asegurar que mes y día tengan dos dígitos
    mes = str(mes).zfill(2)
    día = str(día).zfill(2)

    # Construir RFC
    rfc = (primera_letra_ap + primera_vocal_ap + primera_letra_am +
           primera_letra_nombre + año + mes + día)

    return rfc

# Pedir información al usuario
apellido_paterno = input("Ingrese su Apellido Paterno: ")
apellido_materno = input("Ingrese su Apellido Materno: ")
primer_nombre = input("Ingrese su Primer Nombre: ")

año = int(input("Ingrese el año de nacimiento (ej. 1991): "))
mes = int(input("Ingrese el número de mes de nacimiento (ej. 4): "))
día = int(input("Ingrese el día de nacimiento (ej. 7): "))

# Generar RFC
rfc_generado = generar_rfc(apellido_paterno, apellido_materno, primer_nombre, año, mes, día)

# Imprimir RFC generado
print("RFC generado:", rfc_generado)
