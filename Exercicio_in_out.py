def main():

    while True:
        n = input('Digite a quantidade de números que serão utilizados:\n')
        if n.isdigit():
            n = int(n)
            break
        else:
            print('Digite um número!!!\n')

    lista_in = []
    lista_out = []
    qtde1 = 0
    qtde2 = 0

    for i in range(1, n+1):
        x = int(input('Digite um número:\n'))

        if x in range(10, 21):
            lista_in.append(x)
            qtde1 += 1

        else:
            lista_out.append(x)
            qtde2 += 1

    print(f'Você digitou {qtde1} números dentro do range e {qtde2} fora\n'
        f'Os números In são: {lista_in}\n'
        f'Os números Out são: {lista_out}')

main()