import os
import time




menu = """

|===========================================|
|       [1] Depositar                       |
|       [2] Sacar                           |
|       [3] Extrato                         | 
|       [4] Sair                            |
|===========================================|
"""

saldo = 0 
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
limite_tentativas = 0



while True:

    if limite_tentativas >= 3:
        print('Seu cartao foi bloqueado por seguranca\nprocure uma agencia para desbloquear')
        break

    opcao = int(input(menu))

    if opcao == 1:

        valor_depositado = float(input('Digite o valor a ser depositado: '))

        extrato.append("Depositado: R$"+str(valor_depositado))

        saldo += valor_depositado

        print('Deposito realizado com sucesso!\nSeu saldo é de R${:.2f}'.format(saldo))

    elif opcao == 2:
        
        
        while True:

            
            if numero_saques >= LIMITE_SAQUES:
                print("limite de saques diario excedido")
                break

            elif numero_saques < LIMITE_SAQUES:

                valor_sacado = float(input('Digite o valor a ser sacado: '))

                if valor_sacado > limite:

                    print('Limite insuficiente\n Seu limite é de R${:.2f}\nTente outro valor'.format(limite))
                    
                    continue


                elif valor_sacado > saldo:


                    print('Saldo insuficiente\n tente outro valor\n Seu saldo é de R${:.2f}'.format(saldo))
                    
                    limite_tentativas+=1
                    
                    opcao = input('Deseja tentar novamente?[Sim/Não] ')
                    
                    if opcao == 'Sim' or opcao == 'sim' or opcao == 'SIM' or opcao == 's' or opcao == 'S':
                    
                        continue
                    
                    elif opcao == 'Não'or opcao == 'não' or opcao == 'NÃO' or opcao == 'n' or opcao == 'N':
                    
                        break
                elif valor_sacado <= saldo:
                    
                    extrato.append("Sacado: R$"+str(valor_sacado))

                    saldo -= valor_sacado
                    
                    print('Saque realizado com sucesso!\nSeu saldo é de R${:.2f}'.format(saldo))
                    
                    numero_saques+=1

                    break

                elif limite_tentativas  >= 3:
                    print('Limite de tentativas excedido\n Cartao bloqueado por seguranca')
                    
                    break
                
                elif valor_sacado > limite:
                    
                    print('Limite insuficiente\n Seu limite é de R${:.2f}Tente outro valor'.format(limite))
                    
                    continue

            
    
    elif opcao == 3:

        os.system('clear')

        print('Segue extrato abaixo\n')
        print('Saldo atual: R${:.2f}'.format(saldo))
        print('\n'.join(extrato))
        
        
        time.sleep(20)
        
        os.system('clear')
        
        continue


    elif opcao == 4:

        
        print('Sair')
        
        break

    time.sleep(2)

    os.system('clear')