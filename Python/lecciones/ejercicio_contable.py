# =================================
# EJERCICIO: CALCULADORA DE COMPRAS
# =================================

print("=== DATOS DEL PRODUCTO ===")

producto = input("Ingrese el nombre del producto: ")

precio = float(input("¿Cuál es el precio del artículo?: "))

cantidad = int(input("¿Cuántos artículos vas a seleccionar?: "))

total = precio * cantidad

print("\n=== RESUMEN DE COMPRA ===")
print("Producto:", producto)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Total de la compra:", total)
