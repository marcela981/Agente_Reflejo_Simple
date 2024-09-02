# Agente de reflejo simple

Este código simula un ratón virtual que navega por un entorno en busca de un queso, utilizando un conjunto de decisiones predefinidas basadas en sus percepciones del entorno. El ratón es capaz de tomar decisiones y moverse dentro de una cuadrícula, evitando obstáculos y bucles, hasta que encuentra el queso o la simulación termina.

## Ejecución

1. **Seleccionar un Mapa y Decisiones**:
   Al ejecutar el programa, se te pedirá que selecciones un mapa (Hay 6 mapas) y un conjunto de decisiones (Hay 6 decisiones).
   
3. **Ejecutar la Simulación**:
   Ejecuta el archivo `main.py` para iniciar la simulación:
   ```bash
   python main.py
   ```

4. **Observa el Comportamiento del Ratón**:
   - El ratón (`R`) intentará moverse por la cuadrícula, evitando obstáculos (`#`) y buscando el queso (`Q`).
   - La simulación finalizará cuando el ratón encuentre el queso, entre en un bucle, o intente atravesar un muro.
