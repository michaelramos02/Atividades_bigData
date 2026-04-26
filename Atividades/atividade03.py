tempoFiliacao = int(input('Digite o tempo de filiação na empresa: '))
valorMovimentado = float(input('Digite o valor movimentado nos ultimos 6 meses: '))

if tempoFiliacao > 3 or valorMovimentado >= 5000:
    print('O Cooperado(a) tem direito ao beneficio especial')
else:
    print('Cooperado(a) ainda não atende aos critérios para o benefício')