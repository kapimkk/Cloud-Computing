# Pede ao usuario para digitar um numero

numero = int(input("digite um numero: "))

# Verifica se o numero é dividido por 2 e o resto é 0, se nao ele é impar

if numero % 2 == 0:
    print(f"o numero {numero} é par")
else:
    print(f"o numero {numero} é impar")