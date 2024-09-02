class Lector:
    def __init__(self):
        pass

    def leer_archivo_entorno(self, archivo):
        matriz_entorno = []
        with open(archivo, "r") as file:
            for line in file:
                matriz_entorno.append(list(map(int, line.split())))
        return matriz_entorno
    
    def intentar_bool(self, s):
        if s == "True":
            return True
        elif s == "False":
            return False
        return s  # Esto devuelve la acción, que es un string


    def leer_archivo_decisiones(self, archivo):
        matriz_decisiones = []
        with open(archivo, "r") as file:
            for line in file:
                print(f"Leyendo línea de decisión: {line.strip()}")  # Añadir esta línea para depuración
                matriz_decisiones.append(list(map(self.intentar_bool, line.split())))
        return matriz_decisiones


