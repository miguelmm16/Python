def calcular_perimetro_retangulo(a, b):
    perimetro = 2 * a + 2 * b
    return perimetro

comprimento_lado_a = float(input("Digite o comprimento do lado A: "))
comprimento_lado_b = float(input("Digite o comprimento do lado B: "))

resultado_perimetro = calcular_perimetro_retangulo(comprimento_lado_a, comprimento_lado_b)
print(f"O perimetro do retangulo e: {resultado_perimetro}")
