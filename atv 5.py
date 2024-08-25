#1
x=0
while(x<=100):
    print(x)
    x+=1
else:
    print("fim")
#2
num=int(input("digite um numero"))
while num!=0:
    print(num*2)
    num=int(input("digite um numero"))
#3
atv=print("calculo")
while atv!="nao":
    d=int(input("distância percorrida por um atleta"))
    t=int(input("tempo percorrida por um atleta"))
    v=d/t
    print(v)
    atv=input("deseja refazer o caluclo, digite 'sim' para continuar e 'nao' para encerrar")
#4
for x in range(1,21,2):
    print(x)
#5
for x in range(1,201,2):
    print(x)
#6
for x in range(1,301,4):
    print(x)
#7
for num in range(10):
  num = int(input('Digite um número: '))
  num1 = num * 2
  num2 = num * 3
  print(num1)
  print(num2)
