# Solicita ao usuário o número inicial
numero_inicial = int(input("Digite o número inicial: "))

# Solicita ao usuário o número final
numero_final = int(input("Digite o número final: "))

# Verifica se o número inicial é menor ou igual ao número final
if numero_inicial <= numero_final:
    # Usa um laço while para imprimir os números de numero_inicial até numero_final
    numero_atual = numero_inicial
    while numero_atual <= numero_final:
        print(numero_atual)
        numero_atual += 1  # Incrementa o número atual em 1
else:
    print("O número inicial deve ser menor ou igual ao número final.")
