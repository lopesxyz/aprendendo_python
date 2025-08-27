#operadores 

n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
sobra = n1 % n2
divisaoInteira = n1 // n2
potenciacao = n1 ** n2
raiz = pow (n1, 0.5)

print ('A soma é:', soma)
print ('A subtracao é:', subtracao)
print ('A multiplicacao é:', multiplicacao)
print ('A divisao é:', divisao)
print ('A sobra é:', sobra)
print ('A divisão inteira é:', divisaoInteira)
print ('A raiz é:', raiz)


#Funções condicionais

print ('------------------------------------')
print ('Seja bem-vindo ao sistema de horário')
print ('------------------------------------')

hora = int(input('Digite o horário em números:'))

if hora < 12:
    print ('Bom Dia!')
elif hora < 18:
    print ('Boa Tarde!')
else: 
    print ('Boa Noite!')
    