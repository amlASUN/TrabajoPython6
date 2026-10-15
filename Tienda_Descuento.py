"""}==========O=========={
 Cabecera
 Tienda_Descuento
 Autores: Aitor y Jaime
 Fecha: 15/10/2026 
 }==========O=========={"""

# Bibliotecas
# No se importan bibliotecas

# Constantes
iva10 = 0.10
iva15 = 0.15

# Intput de precio
precio_puesto = float(input("Pon aquí el precio del producto:"))

# Función con 10% de descuento
def calculo_iva_10():
    calculo_total = precio_puesto - (precio_puesto * iva10) # Operación
    precio_descontado = precio_puesto * iva10 # Operación
    print("El precio aplicado tiene un 10% descuento. :)") # Salida
    print(f"El descuento es de: {precio_descontado:.2f}€") # Salida
    print(f"El precio final es: {calculo_total:.2f}€") # Salida

# Función con 15% de descuento
def calculo_iva_15():
    calculo_total = precio_puesto - (precio_puesto * iva15) # Operación
    precio_descontado = precio_puesto * iva15 # Operación
    print("El precio aplicado tiene un 15% descuento. :)") # Salida
    print(f"El descuento es de: {precio_descontado:.2f}€") # Salida
    print(f"El precio final es: {calculo_total:.2f}€") # Salida

# Función general del programa
def main():
    if precio_puesto >= 300: # Función comparativa
        calculo_iva_15() # Llamada a función 15%

    elif precio_puesto >= 100: # Función comparativa
        calculo_iva_10() # Llamada a función 10%

    else: 
        print("El descuento no aplica :(") # Salida
        print(f"El precio final es: {precio_puesto:.2f}€") # Salida

# Llamada a función main
if __name__ == "__main__":
    main()