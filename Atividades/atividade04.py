valorCompra = float(input('Digite o valor da compra: '))
formaPagamento = input('Digite a forma de pagamento: ').lower().strip()

match formaPagamento:
    case 'a vista':
        desconto = valorCompra * 0.10
        precoFinal = valorCompra - desconto
        print(f'a forma de pagamento é à vista, o valor orignal é R${valorCompra:.2f} e o valor final é R${precoFinal:.2f}')
    case 'pix':
        print(f'a forma de pagamento é pix, o valor orignal é R${valorCompra:.2f} e não houve desconto')
    case 'debito':
        acressimo = valorCompra * 0.05
        precoFinal = valorCompra + acressimo
        print(f'a forma de pagamento é débito, o valor orignal é R${valorCompra:.2f} e o valor final é R${precoFinal:.2f}')
    case 'credito':
        acressimo = valorCompra * 0.08
        precoFinal = valorCompra + acressimo
        print(f'a forma de pagamento é crédito, o valor orignal é R${valorCompra:.2f} e o valor final é R${precoFinal:.2f}')
    case 'cheque':
        acressimo = valorCompra * 0.12
        precoFinal = valorCompra + acressimo
        print(f'a forma de pagamento é cheque, o valor orignal é R${valorCompra:.2f} e o valor final é R${precoFinal:.2f}')
    case _ :
        print('Forma de pagamento inválida')