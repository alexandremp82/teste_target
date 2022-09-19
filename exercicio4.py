def moeda(preço=0, moeda="R$"):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
out = float(19849.53)
total = float(sp + rj + mg + es + out)

print(f'O valor do faturamento mensal foi: {moeda(total)}')
psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
pout = ((out/total)*100)

print(f'Porcentagem de SP: {psp:.2f}%')
print(f'Porcentagem de RJ: {prj:.2f}%')
print(f'Porcentagem de MG: {pmg:.2f}%')
print(f'Porcentagem de ES: {pes:.2f}%')
print(f'Porcentagem de OUT {pout:.2f}%')