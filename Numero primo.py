def main():
    numero = int(input('Digite o número que deseja saber se é primo:\n'))
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(f'O resto da divisão do {numero} por {i} é: {numero % i}')
            contador += 1
    
    if contador == 2:
        print(f'O número {numero} é primo')
    else:
        print(f'O número {numero} não é primo')

main()


