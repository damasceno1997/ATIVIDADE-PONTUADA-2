import os

os.system('cls || clear')

print("\nBem-vindo ao sistema de agendamento de exames médicos do Hospital Vida Plena")

exames = [
    {"codigo": 1, "nome": "Hemograma completo", "preco": 50.00},
    {"codigo": 2, "nome": "Raio-X", "preco": 80.00},
    {"codigo": 3, "nome": "Ultrassonografia", "preco": 250.00},
    {"codigo": 4, "nome": "Eletrocardiograma", "preco": 120.00},
    {"codigo": 5, "nome": "Tomografia", "preco": 400.00},
    {"codigo": 6, "nome": "Ressonância magnética", "preco": 2000.00},
    {"codigo": 7, "nome": "Glicose", "preco": 150.00},
]

exames_escolhidos = []
subtotal = 0.0 

while True:
    print("\nExames disponíveis:")
    for exame in exames:
        print(f"Código: {exame['codigo']} - Nome: {exame['nome']} - Preço: R${exame['preco']:.2f}")
    
    try:
        codigo = int(input("\nDigite o código do exame desejado: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    
    exame_encontrado = next((e for e in exames if e["codigo"] == codigo), None)
    
    if exame_encontrado:
        exames_escolhidos.append(exame_encontrado)
        subtotal += exame_encontrado["preco"]
        print(f"Exame '{exame_encontrado['nome']}' adicionado.")
    else:
        print("Código inválido.")
        continue

    continuar = input("\nDeseja adicionar outro exame? (sim/não): ").strip().lower()
    
    if continuar != "sim":
        break

print("\nExames escolhidos:")
for exame in exames_escolhidos:
    print(f"Código: {exame['codigo']} - Nome: {exame['nome']} - Preço: R${exame['preco']:.2f}")

print(f"\nSubtotal: R${subtotal:.2f}")

forma_pagamento = input("\nEscolha a forma de pagamento (Convênio, Particular, Cartão de crédito): ").strip().lower()

if forma_pagamento == "convênio":
    desconto = subtotal * 0.15
    valor_final = subtotal - desconto
    print(f"Desconto aplicado: R${desconto:.2f}")
elif forma_pagamento == "particular":
    valor_final = subtotal
    print("Sem desconto.")
elif forma_pagamento == "cartão de crédito":
    acrescimo = subtotal * 0.08
    valor_final = subtotal + acrescimo
    print(f"Acréscimo aplicado: R${acrescimo:.2f}")
else:
    print("Forma de pagamento inválida. Sem desconto ou acréscimo aplicado.")
    valor_final = subtotal

print(f"\nValor final a ser pago: R${valor_final:.2f}")

print("\nObrigado por utilizar o sistema de agendamento de exames médicos do Hospital Vida Plena!")
    