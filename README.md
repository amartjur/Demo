# Script de Saludo según la Hora del Día

Este proyecto contiene un script en Python que imprime un saludo apropiado según la hora actual del día.

## Funcionalidad

El script determina qué saludo mostrar basándose en la hora actual:

- **6:01 - 12:00**: "Buenos días"
- **12:01 - 20:00**: "Buenas tardes"
- **20:01 - 6:00**: "Buenas noches"

## Requisitos

- Python 3.x
- Módulo `datetime` (incluido en la biblioteca estándar de Python)

## Uso

Para ejecutar el script, simplemente usa el siguiente comando:

```bash
python3 main.py
```

El script imprimirá el saludo apropiado según la hora actual del sistema.

## Ejemplo de salida

```bash
$ python3 main.py
Buenos días
```

(El saludo variará dependiendo de la hora en que ejecutes el script)
