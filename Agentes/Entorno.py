import time

class Entorno:
    def __init__(self, ancho, alto, titulo, matriz_entorno, matriz_decisiones, raton):
        self.matriz_entorno = matriz_entorno
        self.matriz_decisiones = matriz_decisiones
        self.raton = raton
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo

    def desplegar_entorno(self):
        ha_ganado = False

        while not ha_ganado:
            self.imprimir_entorno()
            ha_ganado = self.raton.actualizar(self.matriz_entorno, self.matriz_decisiones)
            time.sleep(0.5)  # Pausa para ver los cambios

        print("¡El ratón ha encontrado el queso!")

    def imprimir_entorno(self):
        for fila in self.matriz_entorno:
            for celda in fila:
                if celda == 2:
                    print("R ", end="")  # Ratón
                elif celda == 3:
                    print("Q ", end="")  # Queso
                elif celda == 1:
                    print("# ", end="")  # Obstáculo
                else:
                    print(". ", end="")  # Espacio vacío
            print()
        print("-" * 20)
