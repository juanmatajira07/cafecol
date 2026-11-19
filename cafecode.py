"""
Programa: cafecode.py
Proyecto: CaféCode · sistema de la tostadora de café
Autor: Juan Sebastián Matajira Orduz · Ficha 3601599
Fecha: 2026-11-19
Versión: 0.4
Descripción: TU DESCRIPCIÓN AQUÍ (2 o 3 líneas: qué hace este programa)
"""

NOMBRE_TOSTADORA = "CaféCode · Tostadora de Café"
ANCHO = 40
PRECIO_LIBRA_ESPECIAL = 38000     # pesos por libra
PRECIO_LIBRA_TRADICIONAL = 26000
PORCENTAJE_DESCUENTO = 0.05       # descuento de temporada: 5 %
LIBRAS_TABLA = 5                  # filas de la tabla de precios

PUNTAJE_MINIMO = 0
PUNTAJE_MAXIMO = 100
PUNTAJE_EXCEPCIONAL = 90
PUNTAJE_EXCELENTE = 85
PUNTAJE_ESPECIAL = 80
HUMEDAD_MINIMA = 10.0
HUMEDAD_MAXIMA = 12.0
HUMEDAD_POSIBLE = 100.0
PRECIO_EXCEPCIONAL = 52000
PRECIO_EXCELENTE = 45000
PRECIO_ESPECIAL = 38000
PRECIO_COMERCIAL = 26000

ventas_registradas = 0 # (contador)
total_vendido = 0 # (acumulador de pesos)
libras_vendidas = 0.0 # (acumulador de libras)
lotes_clasificados = 0 # (contador)
lotes_especiales = 0 # (contador: puntaje de 80 o más)

opcion = ""
while opcion != "0":
    print()
    print("=" * ANCHO)
    print(f"{NOMBRE_TOSTADORA:^{ANCHO}}")
    print("=" * ANCHO)
    print("1. Registrar venta")
    print("2. Clasificar lote")
    print("3. Tabla de precios")
    print("4. Resumen del día")
    print("0. Salir")
    opcion = input("Elige una opción: ").strip()

    match opcion:
        case "1":
            # ---------- PARTE D · REGISTRAR VENTA ----------
            # El nombre ya está resuelto: es el patrón «leer, revisar
            # con while, volver a leer». Úsalo para las dos cantidades:
            #   texto = input("Libras de café especial: ").strip()
            #   texto = texto.replace(",", ".")
            #   mientras NO sea número positivo: muestra el error
            #   «  Error: escribe un número positivo, ej. 2,5.» y
            #   vuelve a leer. Al salir del while, convierte con float().
            # Si las dos cantidades suman 0: imprime
            #   «La venta no tiene café. No se registró.» y usa continue.
            # Calcula subtotal, descuento y total como en ventas.py,
            # suma al contador y a los dos acumuladores, y muestra
            # Cliente, Libras, Total a pagar y «Venta n.° N registrada.»
            nombre_cliente = input("Nombre del cliente: ").strip()
            #while nombre_cliente == "":
            #    print("  Error: el nombre no puede estar vacío.")
            #    nombre_cliente = input("Nombre del cliente: ").strip()
            # TU CÓDIGO AQUÍ

            #print("Registrar venta: en construcción")

        case "2":
            # ---------- PARTE E · CLASIFICAR LOTE ----------
            # 1. Pide el código con el mismo patrón del nombre
            #    (.strip().upper(); no puede quedar vacío).
            # 2. El puntaje ya está resuelto con while True: continue
            #    vuelve a preguntar y break sale cuando el dato sirve.
            #    Quita los # del bloque del puntaje y haz el de la
            #    humedad igual (número y no mayor que HUMEDAD_POSIBLE).
            # 3. Copia la clasificación de clasificacion.py (if/elif/else)
            #    y el estado de la humedad.
            # 4. Suma 1 a lotes_clasificados y, si el puntaje es de 80
            #    o más, suma 1 a lotes_especiales.
            # 5. Muestra Lote, Puntaje SCA, Categoría, Precio por lb y
            #    Estado con el patrón de fila f"{'Etiqueta:':<16}{valor}"
            # TU CÓDIGO AQUÍ: código del lote
            #
            # while True:
            #     texto = input("Puntaje de catación (0 a 100): ").strip()
            #     texto = texto.replace(",", ".")
            #     if not texto.replace(".", "", 1).isdigit():
            #         print("  Error: el puntaje es un número, ej. 86,5.")
            #         continue
            #     puntaje = float(texto)
            #     if PUNTAJE_MINIMO <= puntaje <= PUNTAJE_MAXIMO:
            #         break
            #     print("  Error: el puntaje debe estar entre 0 y 100.")
            #
            # TU CÓDIGO AQUÍ: humedad, clasificación, contadores y ficha
            print("Clasificar lote: en construcción")

        case "3":
            # ---------- PARTE F · TABLA DE PRECIOS ----------
            # Con for libras in range(1, LIBRAS_TABLA + 1): muestra una
            # fila por cada libra con el valor especial y el tradicional
            # en pesos colombianos. Encabezado sugerido:
            #   print(f"{'Libras':<8}{'Especial':>16}{'Tradicional':>16}")
            # TU CÓDIGO AQUÍ
            print("Tabla de precios: en construcción")

        case "4":
            # ---------- PARTE G · RESUMEN DEL DÍA ----------
            # Si no hay ventas ni lotes: «Todavía no hay movimientos hoy.»
            # Si no: ventas, libras vendidas, total vendido, venta
            # promedio (solo si hay ventas: no se divide entre cero),
            # lotes clasificados y lotes especiales.
            # TU CÓDIGO AQUÍ
            print("Resumen del día: en construcción")

        # TU CÓDIGO AQUÍ: case "0" y case _ (PARTE C)
        case "0":
            print("Cerrando CaféCode...")
        case _:
            print("Opción no válida. Elige un número del menú.")
# ---------------------------------------------------------------------
# 4. CIERRE · PARTE G (se ejecuta una sola vez, al salir del ciclo)
# Muestra «Ventas del día: N · Total: $X» y «¡Hasta pronto!»
# ---------------------------------------------------------------------
# TU CÓDIGO AQUÍ
