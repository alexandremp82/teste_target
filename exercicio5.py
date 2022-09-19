texto = str(input('Digite um texto: '))

def inverter(texto):
    return texto[::-1]


print(f'texto digitado: {texto}')

print(f'texto invertido: {inverter(texto)}')
