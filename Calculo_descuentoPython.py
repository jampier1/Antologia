def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado a una compra.
    :param monto_total: Total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función
monto1 = 200  # Ejemplo de compra de $200 con descuento por defecto
monto2 = 300  # Ejemplo de compra de $300 con descuento personalizado (15%)
descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, 15)

# Monto final a pagar después del descuento
monto_final1 = monto1 - descuento1
monto_final2 = monto2 - descuento2

# Mostrar resultados
print(f"Compra de ${monto1}: Descuento de ${descuento1:.2f}, Total a pagar: ${monto_final1:.2f}")
print(f"Compra de ${monto2} con 15% de descuento: Descuento de ${descuento2:.2f}, Total a pagar: ${monto_final2:.2f}")
