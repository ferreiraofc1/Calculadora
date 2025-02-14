def add(x, y):
    """Função para adição"""
    return x + y

def subtract(x, y):
    """Função para subtração"""
    return x - y

def multiply(x, y):
    """Função para multiplicação"""
    return x * y

def divide(x, y):
    """Função para divisão"""
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        # Receber a entrada do usuário
        choice = input("Digite a escolha (1/2/3/4): ")

        # Verificar se a escolha é válida
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if choice == '1':
                print(f"Resultado: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"Resultado: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Resultado: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"Resultado: {num1} / {num2} = {divide(num1, num2)}")

            # Perguntar se o usuário quer fazer outra operação
            next_calculation = input("Quer fazer outro cálculo? (s/n): ")
            if next_calculation.lower() != 's':
                break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    calculator()
