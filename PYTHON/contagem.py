print('\nContagem')
a1 = int(input('\nPonto Inicial: '))
a2 = int(input('Ponto Final: '))
print('\033[0;35m')
for n in range(a1, a2 + 1):
    print(n, end=" ")
print('\033[m')
print("\n\033[0;32mAcabou!\033[m\n")