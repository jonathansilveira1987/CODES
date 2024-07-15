ativo = input('\nAtivo a ser analisado: ')
valor_dividendo = float(input('\nValor do dividendo mensal: '))
valor_acao = float(input('Valor da ação: '))

dividendo_mensal = (valor_dividendo / valor_acao) * 100
dividendo_anual = dividendo_mensal * 12

print(f'\nO DY mensal do ativo {ativo} é de {dividendo_mensal:.2f}%')
print(f'O DY anual do ativo {ativo} é de {dividendo_anual:.2f}%\n')