from time import sleep
def criar_linha():
    print('-'*40)

criar_linha()
print('Bem Vindo Ao Sistema do Banco Xarpy')
criar_linha()
valor_em_conta = 0
opcao = 0
valor_deposito = 0
valor_saque = 0

def agradecimento():
    print('OBRIGADA POR USAR NOSSOS SERVIÇOS!!!')

def opcao_sacar(valor_em_conta,valor_saque):
    valor_movimentado = valor_em_conta - valor_saque
    return valor_movimentado

def opcao_deposito(valor_em_conta,valor_deposito):
    valor_movimentado = valor_em_conta + valor_deposito
    return valor_movimentado

def extrato(**kwargs):
    print(f'~~~~ EXTRATO BANCARIO ~~~~')
    print(F'Valor Atual em Conta : R${valor_em_conta}\nValor de Ultima Movimentação de DEPÓSITO - R${valor_deposito}\nValor de Ultima Movimentação de SAQUE - R${valor_saque}')
    criar_linha()

while opcao != 4:

    sleep(2)
    print('[1] Sacar\n[2] Depositar\n[3] Extrato\n[4] Sair')
    opcao = int(input('Escolha uma opção do painel : '))
    criar_linha()
    if opcao == 1:
        valor_saque = int(input('Digite o valor que você gostaria de sacar: R$'))
        if valor_em_conta >= valor_saque:
            novo_saldo = opcao_sacar(valor_em_conta,valor_saque)
            valor_em_conta = novo_saldo
            print('PROCESSANDO ...')
            sleep(2)
            print(f'SEU SAQUE NO VALOR DE {valor_saque} FOI REALIZADO COM SUCESSO !!!\nSeu Saldo Atual é de R$',novo_saldo)
            criar_linha()
        else :
            print(f'SEU SAQUE NO VALOR DE {valor_saque} NÃO PÔDE SER REALIZADO !!!\nSeu Saldo Atual é de R${valor_em_conta}')
            criar_linha()


    if opcao == 2:
        valor_deposito =int(input('Digite o valor que você deseja depositar em sua conta: R$'))
        novo_saldo = opcao_deposito(valor_em_conta,valor_deposito)
        valor_em_conta = novo_saldo
        print('PROCESSANDO ...')
        sleep(2)
        print(f'SEU DEPOSITO NO VALOR DE {valor_deposito} FOI REALIZADO COM SUCESSO !!!\nSeu Saldo Atual é de R$', valor_em_conta)
        criar_linha()
    if opcao == 3:
        extrato(valor_em_conta = valor_em_conta ,valor_deposito = valor_deposito,valor_saque = valor_saque)
    if opcao > 4 or opcao < 1 :
        print('Opção Invalida. Favor Digitar um dos Números Disponiveis Como Opção Na Tela')
        criar_linha()


agradecimento()
criar_linha()
