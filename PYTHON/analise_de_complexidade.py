a = 0
n = int(input('\nVetor: '))
for i in range(n):
  for j in range(i + 1, n):
    a = a + i + j
print(f'\n{a}')

a = 0
for i in range(n):
  for j in range(n):
    for k in range(n):
      a = a + i + j + k
print(f'\n{n}')
print(f'{j}')
print(f'{k}')
print(f'{a}\n')

for i in range(n):
  i = 1
  while i < n:
    i = i * 2
    print(i, end=" ")
print('\n')