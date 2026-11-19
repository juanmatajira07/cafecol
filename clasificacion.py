"""
Programa: clasificacion.py
Proyecto: CaféCode · sistema de la tostadora de café
Autor: Sebastian Matajira · Ficha 3601599
Fecha: 2026-11-12
Versión: 0.3
Descripción: Este programa te entrega un recibo con algunos datos
técnicos del lote de cafe, con los cuales se calcula el puntaje y
categoria. Y finalmente se entrega un precio final.
"""

PUNTAJE_MINIMO = 0
PUNTAJE_MAXIMO = 100
PUNTAJE_EXCEPCIONAL = 90     # escala SCA: 90 a 100
PUNTAJE_EXCELENTE = 85       # escala SCA: 85 a 89,99
PUNTAJE_ESPECIAL = 80        # desde 80 el café se considera especial
PRECIO_EXCEPCIONAL = 52000   # pesos por libra
PRECIO_EXCELENTE = 45000
PRECIO_ESPECIAL = 38000
PRECIO_COMERCIAL = 26000
HUMEDAD_MINIMA = 10.0
HUMEDAD_MAXIMA = 12.0
HUMEDAD_POSIBLE = 100.0
ANCHO_FICHA = 40

codigo_lote = input("Código del lote: ").strip().upper()
texto_puntaje = input("Puntaje de catación (0 a 100): ").strip()
texto_puntaje = texto_puntaje.replace(",", ".")
texto_humedad = input("Humedad del grano (%): ").strip().replace(",", ".")
opcion_tueste = input("Tueste (1 claro, 2 medio, 3 oscuro): ").strip()

mensaje_error = ""
if codigo_lote == "":
    mensaje_error = "el código del lote no puede estar vacío."
elif not texto_puntaje.replace(".", "", 1).isdigit():
    mensaje_error = "el puntaje debe ser un número positivo, ej. 86,5."
elif not texto_humedad.replace(".", "", 1).isdigit():
    mensaje_error = "la humedad debe ser un número"
elif not PUNTAJE_MINIMO <= float(texto_puntaje) <= PUNTAJE_MAXIMO:
    mensaje_error = "El puntaje debe estar entre 0 y 100"
elif float(texto_humedad) > HUMEDAD_POSIBLE:
    mensaje_error = "El porcentaje no puede pasar de 100"

if mensaje_error == "":
    puntaje = float(texto_puntaje)
    humedad = float(texto_humedad)
    if puntaje >= PUNTAJE_EXCEPCIONAL:
        categoria = "Excepcional"
        precio_libra = PRECIO_EXCEPCIONAL
    elif puntaje >= PUNTAJE_EXCELENTE:
        categoria = "Excelente"
        precio_libra = PRECIO_EXCELENTE
    elif puntaje >= PUNTAJE_ESPECIAL:
        categoria = "Muy bueno (Especial)"
        precio_libra = PRECIO_ESPECIAL
    else:
        categoria = "Comercial"
        precio_libra = PRECIO_COMERCIAL

    if HUMEDAD_MINIMA <= humedad <= HUMEDAD_MAXIMA:
        estado_humedad = "Apto para tostión"
    elif humedad < HUMEDAD_MINIMA:
        estado_humedad = "Muy seco: revisar bodega"
    else:
        estado_humedad = "Muy húmedo: más secado"
    match opcion_tueste:
        case "1":
            tueste = "Claro"
            perfil = "Acidez y notas frutales"
        case "2":
            tueste = "Medio"
            perfil = "Acidez y dulzor en equilibrio"
        case "3":
            tueste = "Oscuro"
            perfil = "Cuerpo intenso, chocolate"
        case _:
            tueste = "Sin definir"
            perfil = "Opción de tueste no válida"
    puntaje_txt = f"{puntaje:,.2f}".replace(".", ",")
    humedad_txt = f"{humedad:,.1f}%".replace(".", ",")
    precio_txt = f"${precio_libra:,.0f}".replace(",", ".")

if mensaje_error != "":
    print(f"Error: {mensaje_error}")
    print("Vuelve a ejecutar el programa con datos correctos.")
else:
    print("=" * ANCHO_FICHA)
    print(f"{'FICHA DE CALIDAD · CaféCode':^{ANCHO_FICHA}}")
    print("=" * ANCHO_FICHA)
    print(f"{'Lote:':<16}{codigo_lote}")
    print(f"{'Puntaje SCA:':<16}{puntaje_txt}")
    print(f"{'Categoría:':<16}{categoria}")
    print(f"{'Precio por lb:':<16}{precio_txt}")
    print(f"{'Humedad:':<16}{humedad_txt}")
    print(f"{'Estado:':<16}{estado_humedad}")
    print(f"{'Tueste:':<16}{tueste}")
    print(f"{'Perfil:':<16}{perfil}")
    print("=" * ANCHO_FICHA)
