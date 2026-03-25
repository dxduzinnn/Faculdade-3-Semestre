#a
num = int(input('Digite um número maior que 1:'))

if num <= 1:
  print('Número inválido! DIgite um número maior que 1')
else:
  print(f'Divisores de {num}:')

  for i in range (1, num + 1):
    if num % i == 0:
      print(i)

#b
cont = 0

num = int(input('Digite um número positivo: '))

if num <= 1:
  print('Número inválido! DIgite um número maior que 1')
else:
  print(f'Quantidade de divisores de {num}: ')

  for i in range(1, num + 1):
    if num % i == 0:
      cont += 1

print(f'O número {num} possui {cont} divisores.')

#c
num = int(input('Digite um número inteiro: '))

if num <= 1:
  print('Número inválido! DIgite um número maior que 1')
else:
  primo = True

  for i in range(2, num):
      if num % i == 0:
          primo = False
          break
  if primo:
    print('O número é primo')
  else:
    print('O número não é primo.')

