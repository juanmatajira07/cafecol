"""
Programa: cafecode.py
Proyecto: CaféCode · sistema de la tostadora de café
Autor: Juan Sebastián Matajira Orduz · Ficha 3601599
Fecha: 2026-11-19
Versión: 0.4
Descripción: TU DESCRIPCIÓN AQUÍ (2 o 3 líneas: qué hace este programa)
"""

NOMBRE_TOSTADORA = "CaféCode · Tostadora de Café"
ANCHO_RECIBO = 40
PRECIO_LIBRA_ESPECIAL = 38000     # pesos por libra
PRECIO_LIBRA_TRADICIONAL = 26000
PORCENTAJE_DESCUENTO = 0.05       # descuento de temporada: 5 %
LIBRAS_TABLA = 5                  # filas de la tabla de precios
GRAMOS_POR_LIBRA=500
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
    print("=" * ANCHO_RECIBO)
    print(f"{NOMBRE_TOSTADORA:^{ANCHO_RECIBO}}")
    print("=" * ANCHO_RECIBO)
    print("1. Registrar venta")
    print("2. Clasificar lote")
    print("3. Tabla de precios")
    print("4. Resumen del día")
    print("0. Salir")
    opcion = input("Elige una opción: ").strip()

    match opcion:
        case "1":
            nombre_cliente = input("Nombre del cliente: ").strip()
            while nombre_cliente == "":
                print("  Error: el nombre no puede estar vacío.")
                nombre_cliente = input("Nombre del cliente: ").strip()
            texto = input("Libras de café especial: ").strip()
            texto = texto.replace(",", ".")
            while not texto.replace(".", "",1).isdigit():
                print(" Error: escribe un número positivo, ej. 2,5.")
                texto = input("Libras de café especial: " ).strip()
                texto = texto.replace(",", ".")
            libras_especial = float(texto)
            texto = input("Libras de café tradicional: ").strip()
            texto = texto.replace(",", ".")
            while not texto.replace(".", "",1).isdigit():
                print(" Error: escribe un número positivo, ej. 2,5.")
                texto = input("Libras de café tradicional: " ).strip()
                texto = texto.replace(",", ".")
            libras_tradicional = float(texto)
            subtotal_especial = libras_especial * PRECIO_LIBRA_ESPECIAL
            subtotal_tradicional = libras_tradicional * PRECIO_LIBRA_TRADICIONAL
            subtotal = subtotal_especial + subtotal_tradicional
            descuento = subtotal * PORCENTAJE_DESCUENTO
            total = subtotal - descuento
            total_libras = libras_especial + libras_tradicional
            total_gramos = total_libras * GRAMOS_POR_LIBRA
            if total_libras == 0:
                print("La venta no tiene café. No se registró")
                continue
            print("=" * ANCHO_RECIBO)
            print(f"{NOMBRE_TOSTADORA:^{ANCHO_RECIBO}}")
            print("=" * ANCHO_RECIBO)
            print(f"Cliente: {nombre_cliente}")

            especial_txt = f"${subtotal_especial:,.0f}".replace(",", ".")
            lb_especial_txt = f"{libras_especial:.1f}".replace(".", ",")
            tradicional_txt = f"${subtotal_tradicional:,.0f}".replace(",", ".")
            lb_tradicional_txt = f"{libras_tradicional:.1f}".replace(".", ",")
            subtotal_txt = f"${subtotal:,.0f}".replace(",", ".")
            etiqueta_descuento = "Descuento (5%)"
            descuento_txt = f"-${descuento:,.0f}".replace(",", ".")
            total_txt = f"${total:,.0f}".replace(",", ".")
            lb_total_txt = f"{total_libras:.1f}".replace(",", ".")
            gramos_txt = f"{total_gramos:,.0f}".replace(",", ".")
            print("-" * ANCHO_RECIBO)
            print(f"{'Producto':<18}{"Libras":>8}{"Valor":>14}")
            print(f"{'Café especial':<18}{lb_especial_txt:>8}{especial_txt:>14}")
            print(f"{'Café tradicional':<18}{lb_tradicional_txt:>8}{tradicional_txt:>14}")
            print("-"*ANCHO_RECIBO)
            print(f"{'Subtotal':<26}{subtotal_txt:>14}")
            print(f"{etiqueta_descuento:<26}{descuento_txt:>14}")
            print(f"{'TOTAL A PAGAR:':<26}{total_txt:>14}")
            print("-"*ANCHO_RECIBO)
            print(f"Café entregado: {lb_total_txt} lb ({gramos_txt} g)")
            print("="*ANCHO_RECIBO)
            print('¡Gracias por apoyar el café de Caldas!')

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
            codigo_lote = input("Código del lote: ").strip().upper()
            while True:
                texto_puntaje = input("Puntaje de catación (0 a 100): ").strip()
                texto_puntaje = texto_puntaje.replace(",", ".")
                if not texto_puntaje.replace(".", "", 1).isdigit():
                    print("  Error: el puntaje es un número, ej. 86,5.")
                    continue
                puntaje = float(texto_puntaje)
                if PUNTAJE_MINIMO <= puntaje <= PUNTAJE_MAXIMO:
                    break
                print("  Error: el puntaje debe estar entre 0 y 100.")
                    
            # TU CÓDIGO AQUÍ: humedad, clasificación, contadores y ficha
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
                print("=" * ANCHO_RECIBO)
                print(f"{'FICHA DE CALIDAD · CaféCode':^{ANCHO_RECIBO}}")
                print("=" * ANCHO_RECIBO)
                print(f"{'Lote:':<16}{codigo_lote}")
                print(f"{'Puntaje SCA:':<16}{puntaje_txt}")
                print(f"{'Categoría:':<16}{categoria}")
                print(f"{'Precio por lb:':<16}{precio_txt}")
                print(f"{'Humedad:':<16}{humedad_txt}")
                print(f"{'Estado:':<16}{estado_humedad}")
                print(f"{'Tueste:':<16}{tueste}")
                print(f"{'Perfil:':<16}{perfil}")
                print("=" * ANCHO_RECIBO)
            if puntaje >=80:
                lotes_especiales+=1
            elif puntaje>0:
                lotes_clasificados+=1

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
