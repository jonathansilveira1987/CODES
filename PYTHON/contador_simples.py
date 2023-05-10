from time import sleep

# Contador Manual.
a = int(input('\nAté quanto você deseja contar: '))
print('\033[32m')
for i in range(a + 1):
    # sleep(0.5)
    print(i)
print('\033[m')

# Contador com ponto Inicial & Final.
b = int(input('Ponto A: '))
c = int(input('Ponto B: '))
d = range(b, c + 1)
print('\033[33m')
for e in d:
    # sleep(0.5)
    print(e)
print('\033[m')