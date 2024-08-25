#1
print(5+10/2)
print((5+10)/2)
print(2+2)
print(2*2)
print(2**2)
print(2-2)
print(4/2)
print(5//2)
print(4%2)

#2
fah = float(input('digite a temperatura em fahrenheit'))
c=5*((fah-32)/9)
print('temperatura em graus celsius é:', c)

#3
h1 = float(input('digite sua altura homem'))
h2 = float(input('digite sua altura mulher'))

p1=(72.7*h1)-58
p2=(62.1*h2)-44.7
print('peso ideal para homem:', p1)
print('peso ideal para mulher:', p2)

#4
s=float(input('posição final'))
s0=float(input('posiçao inicial'))
v=float(input('velocidade'))
At=float(input('variaçao de temperatura'))
v0=float(input('velocidade inicial'))
a=float(input('aceleraçao'))
t=float(input('tempo'))
vf=float(input('velocidade final'))
As=float(input('deslocamento'))

sd=s0+v*At
v=v0+a*t
sp=s0+v0*t+(0.5*(a*t)**2)
vf=((v0**2)+(2*a*As))**0.5

print('funçao horaria do deslocamento:', sd)
print('funçao horaria de velocidade', v)
print('funçao horaira de posiçao', sp)
print('equaçao de torricelli', vf)


