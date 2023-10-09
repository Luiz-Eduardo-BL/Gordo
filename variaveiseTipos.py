import math

# Usuario digita o raio da circunferencia
raio = float(input("Digite o raio da circunferencia: "))
# Calculando o diametro da circunferencia
diametro = 2 * raio
# Calculando a area da circunferencia
area = math.pi * raio ** 2
# Calculando o perimetro da circunferencia
perimetro = 2 * math.pi * raio
# Mostrando os resultados para o usuario
print("O diametro da circunferencia eh: ", diametro)
print("A area da circunferencia eh: ", area)
print("O perimetro da circunferencia eh: ", perimetro)

