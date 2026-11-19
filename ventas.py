"""
Programa: ventas.py
Proyecto: CaféCode · sistema de la tostadora de café
Autor: SEBASTIAN MATAJIRA y ANDERSON MARIN · Ficha 3601599
Fecha: 2026-10-29
Versión: 0.2
Descripción: Este programa recibe la cantidad de café que el usuario quiere
comprar y su nombre, con esto crea un recibo personalizado para el cliente.
Con el total a pagar, el desglose de las cuentas y unos datos adicionales.
"""

NOMBRE_TOSTADORA = "CaféCode · Tostadora de Café"
PRECIO_LIBRA_ESPECIAL = 38000     # pesos por libra de café especial
PRECIO_LIBRA_TRADICIONAL = 26000  # pesos por libra de café tradicional
PORCENTAJE_DESCUENTO = 0.05  # Descuento de temporada del 5%
GRAMOS_POR_LIBRA = 500  # (la libra comercial en Colombia)
GRAMOS_POR_KILO = 1000 # La cantidad de gramos que tiene un kilo
GRAMOS_POR_BOLSA = 250 # La cantidad de gramos de café por bolsa
ANCHO_RECIBO = 40  # (caracteres de ancho del recibo)

nombre_cliente = input("Nombre del cliente: ")
libras_especial = input("Libras de café especial: ").replace(",", ".")
libras_especial = float(libras_especial)
libras_tradicional = input("Libras de café tradicional: ").replace(",", ".")
libras_tradicional = float(libras_tradicional)

subtotal_especial = libras_especial * PRECIO_LIBRA_ESPECIAL
subtotal_tradicional = libras_tradicional * PRECIO_LIBRA_TRADICIONAL
subtotal = subtotal_especial + subtotal_tradicional
descuento = subtotal * PORCENTAJE_DESCUENTO
total = subtotal - descuento
total_libras = libras_especial + libras_tradicional
total_gramos = total_libras * GRAMOS_POR_LIBRA

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

kilos_lote = float(input("kilos de café tostado del lote: ").replace(",", "."))
gramos_lote = round(kilos_lote*GRAMOS_POR_KILO)
bolsa_completa = gramos_lote//GRAMOS_POR_BOLSA
gramos_sobrantes = gramos_lote % GRAMOS_POR_BOLSA
print(f"Bolsas de 250g completas: {bolsa_completa}")
print(f"Gramos sobrantes: {gramos_sobrantes}")

