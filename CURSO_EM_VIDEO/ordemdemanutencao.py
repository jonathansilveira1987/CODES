ordens = []

ordem = input('Informe o n�mero da ordem: ')
ordens.append(ordem)


ordens = ['20565285',
            '30565285',
            '10565285',
            '30565285',
            '50565285',
            '20565285',
            '30565285',
            '90565285'
]

print('\nOrdens de Manuten��o:')
print('\n')

for ordem in ordens:
    if ordem[0] == '2':
        print(f'Ordem {ordem} - \033[0;31mManuten��o Preventiva.\033[m')
    if ordem[0] == '3':
        print(f'Ordem {ordem} - \033[0;33mManuten��o Corretiva.\033[m')
    else:
        print(f'Ordem {ordem} - \033[0;32mManuten��o Preditiva.\033[m')
print('\n')