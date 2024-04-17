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
operacao_realizada = False

while True:
  opcao = input(menu) #entrada do usuário para a opção desejada

  if opcao == "d":
      valor = float(input("Informe o valor do depósito: "))

      if valor > 0:
          saldo += valor
          extrato += f"Depósito: R$ {valor:.2f}\n" #atribuição de valor a extrato
          operacao_realizada = True
      
      else:
          print("Operação falhou! O valor informado é inválido.") #caso o valor seja menor ou igual a zero
        
  elif opcao == "s":
    
    if numero_saques < LIMITE_SAQUES:
        sacar = float(input("Informe o valor do saque: ")) 
        
        if sacar > saldo:
                print("Você não tem saldo suficiente para realizar essa operação.")
          
        elif sacar > 0 and sacar <= limite:
              extrato += f"Saque: R$ {sacar:.2f}\n"
              saldo -= sacar
              numero_saques += 1
              operacao_realizada = True
              
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
      print("Limite de saques diários excedido. Tente novamente amanhã.")
      

  elif opcao == "e":
    if operacao_realizada:
      print(f"""\n      =================Extrato=================      \n
          Essas foram as movimentações:\n\n{extrato}\n
          Saldo final: R$ {saldo:.2f}

          Obrigado por usar nossos serviços!""") #usando o format para inserir de maneira mais fácil os valores de saldo e extrato

    else:
      print("\nNenhuma operação realizada anteriormente.")
    
  elif opcao == "q":
    print("Obrigado por usar nossos serviços")
    break

  else:
    print("Operação inválida. Por favor, escolha uma das opções do menu.")