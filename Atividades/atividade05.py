n1 = float(input('Digite a nota 1 do aluno: '))
n2 = float(input('Digite a nota 2 do aluno: '))
substitutiva = input('O aluno realizou a substitutiva ? ').lower().strip()
n3 = 0
if substitutiva == 'sim':
    n3 = float(input('Digite o valor da nota substitutiva: '))
else: 
    n3 = -1

if n1 < n3:
    n1 = n3
elif n2 < n3:
    n2 = n3

media = (n1 + n2 ) / 2


if media >= 6:
    print(f'Aprovado, a média foi {media}')

elif media >= 3:
    print(f'Em recuperação, a média foi {media}')
else:
    print(f'Reprovado, a média foi {media}')

