# Clase que representa un clima semanal
class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas de la semana

    def ingresar_temperaturas(self):
        for i in range(7):  # Ingresar 7 días de la semana
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


# Función principal para gestionar el flujo del programa
def main():
    # Crear un objeto de la clase ClimaSemanal
    clima = ClimaSemanal()

    # Ingresar las temperaturas de la semana
    clima.ingresar_temperaturas()

    # Calcular el promedio de la semana
    promedio = clima.calcular_promedio()

    # Mostrar el resultado
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")


# Ejecutar el programa
if __name__ == "__main__":
    main()
