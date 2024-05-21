import time

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == 'd':
    print('Depósito')
    deposito = float(input("Digite o valor que deseja depositar: "))
    while deposito < 0:
       deposito = float(input("Valor inválido. \nDigite o valor que deseja depositar: "))
    saldo += deposito
    extrato += f'Depósito: R${deposito}\n'

  elif opcao == 's':
    print('Saque')
    saque = float(input("Digite o valor que deseja sacar: "))

    if saque > saldo:
      print("Saque não realizado. Saldo indisponível. ")
      print(f"Valor disponivel para saque: R$ {saldo}")

    elif saque > limite:
      print("Valor do saque excede o limite.")

    elif numero_saques >= LIMITE_SAQUES:
      print("Já foi realizado os 3 saques diários permitidos. Tente novamente amanhã. ")

    elif saque > 0:
      saldo -= saque
      numero_saques = numero_saques+1
      extrato += f'Saque: R${saque}\n'

  elif opcao == 'e':
    if extrato == '':
      print("Extrato inexistente!")
    else:
      print("=========== EXTRATO ===========")
      print(extrato)
      print(f"\nSaldo Disponível: R$ {saldo}")
      print("===============================")

  elif opcao == 'q':
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")