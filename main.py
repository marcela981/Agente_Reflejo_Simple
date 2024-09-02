from Agentes.Raton import Raton
from Agentes.Lector import Lector
from Agentes.Entorno import Entorno

def seleccionar_opcion(max_opciones, mensaje):
    while True:
        try:
            opcion = int(input(mensaje))
            if 1 <= opcion <= max_opciones:
                return opcion
            else:
                print(f"Por favor, selecciona un número entre 1 y {max_opciones}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def main():
    lector = Lector()
    
    # Preguntar al usuario qué mapa y decisiones quiere usar
    mapa_opcion = seleccionar_opcion(6, "Selecciona el número del mapa que deseas usar (1-6): ")
    decisiones_opcion = seleccionar_opcion(6, "Selecciona el número de las decisiones que deseas usar (1-6): ")

    mapa_archivo = f"mapa{mapa_opcion}.txt"
    decisiones_archivo = f"decisiones{decisiones_opcion}.txt"

    matriz_entorno = lector.leer_archivo_entorno(mapa_archivo)
    matriz_decisiones = lector.leer_archivo_decisiones(decisiones_archivo)

    y, x = Raton.encontrar_raton(matriz_entorno)
    raton = Raton(y, x)

    entorno = Entorno(ancho=800, alto=600, titulo="Simulación del Ratón", 
                      matriz_entorno=matriz_entorno, matriz_decisiones=matriz_decisiones, 
                      raton=raton)

    entorno.desplegar_entorno()

if __name__ == "__main__":
    main()
