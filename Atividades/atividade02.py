qtdCaixa = int(input('Digite a quantidade de caixa em estoque: '))
qtdSolicitada = int(input('Digite a quantidade solicitada pelo cliente: '))
pesoPedido = int(input('Digite o peso do pedido: '))

if qtdCaixa >= qtdSolicitada and pesoPedido <= 50: 
    print('O pedido pode ser liberado.')

else:
    print('O pedido não pode ser enviado')
    print('é necessário revisar as condições de estoque e transporte. ')