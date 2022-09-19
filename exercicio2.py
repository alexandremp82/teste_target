print('='*30)
print('Sequência de Fibonacci')
print('='*30)
num = int(input('Quantos termos você quer mostrar?: '))
t1 = 0
t2 = 1
esta = False
print('{} » {}'.format(t1, t2), end='')
cont = 3


while cont <= num:
    t3 = t1 + t2
    if t3 == num:
        esta = True
    print(' » {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print()
if esta == True:
    print(f'O numero {num} está na sequência fibonacci.')
else:
    print(f'O numero {num} não está na sequência fibonacci.')
print(' fim ')
print('='*30)