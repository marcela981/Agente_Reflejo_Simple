class Raton:
    @staticmethod
    def encontrar_raton(matriz_entorno):
        for fila in range(len(matriz_entorno)):
            for columna in range(len(matriz_entorno[0])):
                if matriz_entorno[fila][columna] == 2:
                    return fila, columna
        return None

    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.posiciones_visitadas = set()  # Para rastrear las posiciones visitadas

    def percibir_entorno(self, matriz_entorno):
        filas = len(matriz_entorno)
        columnas = len(matriz_entorno[0])

        izquierda = self.x > 0 and matriz_entorno[self.y][self.x - 1] != 1
        derecha = self.x < columnas - 1 and matriz_entorno[self.y][self.x + 1] != 1
        arriba = self.y > 0 and matriz_entorno[self.y - 1][self.x] != 1
        abajo = self.y < filas - 1 and matriz_entorno[self.y + 1][self.x] != 1

        return izquierda, derecha, arriba, abajo

    def tomar_decision(self, matriz_entorno, matriz_decisiones):
        izquierda, derecha, arriba, abajo = self.percibir_entorno(matriz_entorno)

        print(f"Percepciones: Izquierda={izquierda}, Derecha={derecha}, Arriba={arriba}, Abajo={abajo}")

        for decision in matriz_decisiones:
            if (izquierda == decision[0] and
                derecha == decision[1] and
                arriba == decision[2] and
                abajo == decision[3]):
                print(f"Decisión tomada: {decision[4]}")
                return decision[4]
        print("Ninguna acción definida para esta combinación de percepciones.")
        return "nada"

    def mover_raton(self, accion, matriz_entorno):
        nuevo_x, nuevo_y = self.x, self.y

        if accion == "izquierda":
            nuevo_x -= 1
        elif accion == "arriba":
            nuevo_y -= 1
        elif accion == "derecha":
            nuevo_x += 1
        elif accion == "abajo":
            nuevo_y += 1

        # Verifica si la nueva posición es un muro
        if matriz_entorno[nuevo_y][nuevo_x] == 1:
            print("El ratón intentó atravesar un muro. Terminando la simulación.")
            return False  # Termina la simulación si intenta atravesar un muro
        else:
            self.x, self.y = nuevo_x, nuevo_y
            return True

    def actualizar(self, matriz_entorno, matriz_decisiones):
        posicion_actual = (self.y, self.x)
        if posicion_actual in self.posiciones_visitadas:
            print("El ratón está en un bucle, terminando la simulación.")
            return True  # Terminar simulación

        self.posiciones_visitadas.add(posicion_actual)

        accion = self.tomar_decision(matriz_entorno, matriz_decisiones)
        if accion == "nada":
            return True  # Terminar simulación si no hay decisión

        if not self.mover_raton(accion, matriz_entorno):
            return True  # Termina si el ratón intenta atravesar un muro

        if matriz_entorno[self.y][self.x] == 3:
            print("¡El ratón ha encontrado el queso!")
            return True  # Ha ganado

        matriz_entorno[self.y][self.x] = 2  # Actualizar la posición del ratón
        return False
