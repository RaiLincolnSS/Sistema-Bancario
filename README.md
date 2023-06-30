# Sistema-Bancario
Pequeno projeto desenvolvido na Formacao Python Developer da Digital Innovation One

# Descrição do projeto
Este código é um simulador simples de um sistema bancário que permite ao usuário realizar operações como depositar dinheiro, sacar dinheiro, exibir o extrato bancário e sair do programa.

# Funcionalidades

O programa apresenta as seguintes funcionalidades:

Depositar: Permite ao usuário digitar um valor a ser depositado em sua conta bancária. O valor é adicionado ao saldo e registrado no extrato.

Sacar: Permite ao usuário digitar um valor a ser sacado de sua conta bancária. Antes de efetuar o saque, o programa verifica se o valor está dentro do limite de saque diário e se há saldo disponível na conta. O saque é realizado apenas se essas condições forem atendidas. O valor sacado é subtraído do saldo e registrado no extrato.

Extrato: Exibe o extrato bancário atual, mostrando o saldo atual e todas as transações (depósitos e saques) registradas no extrato.

Sair: Encerra o programa.

# Variáveis
O programa utiliza as seguintes variáveis:

saldo: Variável que armazena o saldo atual da conta bancária.
limite: Variável que representa o limite de saque diário.
extrato: Lista que registra todas as transações (depósitos e saques) realizadas.
numero_saques: Variável que conta o número de saques realizados no dia.
LIMITE_SAQUES: Constante que define o limite máximo de saques diários.
limite_tentativas: Variável que registra o número de tentativas de saque com saldo insuficiente.

#Uso

O programa é executado em um loop infinito, exibindo um menu de opções ao usuário. O usuário deve digitar o número correspondente à opção desejada.

Para selecionar a opção Depositar, digite 1 e informe o valor a ser depositado. O valor será adicionado ao saldo e registrado no extrato.

Para selecionar a opção Sacar, digite 2 e informe o valor a ser sacado. O programa verifica se o valor está dentro do limite de saque diário e se há saldo disponível. Se as condições forem atendidas, o valor é subtraído do saldo e registrado no extrato.

Para selecionar a opção Extrato, digite 3. O programa exibirá o extrato bancário atual, mostrando o saldo e todas as transações registradas.

Para sair do programa, digite 4.

O programa utiliza a biblioteca os para limpar a tela e a biblioteca time para pausar a execução por alguns segundos.

# Restrições

O programa possui um limite de tentativas de saque com saldo insuficiente. Após três tentativas, o cartão é bloqueado por segurança e é necessário procurar uma agência para desbloqueá-lo.

O programa possui um limite de saques diários definido pela constante LIMITE_SAQUES. Após atingir esse limite, o usuário não pode realizar mais saques no dia.
