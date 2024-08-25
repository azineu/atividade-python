#1,4

idade=int(input('digite sua idade'))
if idade>= 18:
    print('maior de idade')
else:
    print('não atigniu maioridade')

#2,3
    
senha=str(input('digite sua senha'))
if senha=='soueu123':
    print('sua senha é valida')
else:
    print('senha invalida')
#5
    
n1=float(input('digite nota 1'))
n2=float(input('digite nota 2'))
n3=float(input('digite nota 3'))
media=(n1+n2+n3)/3
if media>=7:
    print('aprovado')
else:
    print('reprovado')
#6
    
salario=float(input('digite seu salario'))
if salario<=300:
    print(salario*1.35)
else:
    print(salario*1.15)

n1=float(input('digite um numero'))
n2=float(input('digite outro numero'))
va=input('digite 1 para adição e 2 para sub')
if va=='1':
 print(n1+n2)
else:
 print(n1-n2)

