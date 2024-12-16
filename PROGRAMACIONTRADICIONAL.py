# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Ingresar 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal para gestionar el flujo del programa
def main():
    # Ingresar las temperaturas de la semana
    temperaturas = ingresar_temperaturas()

    # Calcular el promedio de la semana
    promedio = calcular_promedio(temperaturas)

    # Mostrar el resultado
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
