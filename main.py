#!/usr/bin/env python3
"""
Script de saludo según la hora del día.
Imprime un saludo apropiado basado en la hora actual.
"""

from datetime import datetime


def obtener_saludo():
    """
    Determina el saludo apropiado según la hora del día.
    
    Returns:
        str: El saludo correspondiente a la hora actual
    """
    hora_actual = datetime.now().hour
    
    # 6:01 - 12:00: "Buenos días"
    if 6 < hora_actual <= 12:
        return "Buenos días"
    # 12:01 - 20:00: "Buenas tardes"
    elif 12 < hora_actual <= 20:
        return "Buenas tardes"
    # 20:01 - 6:00: "Buenas noches"
    else:
        return "Buenas noches"


if __name__ == "__main__":
    saludo = obtener_saludo()
    print(saludo)
