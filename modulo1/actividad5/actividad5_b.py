#Calcula el precio del boleto basado en la edad
def calcular_precio_boleto(edad):
    """Función para calcular el precio del boleto según la edad"""
    if edad < 3:
        return 0, "GRATIS"
    elif edad <= 12:
        return 10, f"${10}"
    else:
        return 15, f"${15}"

print("=== CINEMOX ===")
print("Precios de entradas:")
print("• 0-2 años: GRATIS")
print("• 3-12 años: $10")
print("• 13+ años: $15")
print("=" * 35)

while True:
    entrada = input("Ingresa la edad (o 'fin' para terminar): ").strip()
    
    if entrada.lower() in ['fin', 'salir', 'quit', 'exit']:
        print("Disfruta tu funcion!")
        break
    
    try:
        edad = int(entrada)
        
        if edad < 0:
            print("❌ La edad no puede ser negativa")
            continue
        elif edad > 120:
            print("❌ Por favor, ingresa una edad válida")
            continue
            
        precio, precio_texto = calcular_precio_boleto(edad)
        print(f"👤 Edad: {edad} años → Precio: {precio_texto}")
        
        # Preguntar si quiere continuar
        print()
        if input("¿Continuar? (Enter para sí, 'n' para no): ").lower() == 'n':
            print("👋 ¡Hasta pronto!")
            break
            
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido")
    
    print("-" * 50)