# funções das operações
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b


print("=== Calculadora ===")


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")


op = input("Opção: ")


if op == "1":
    print("Resultado:", somar(num1, num2))

elif op == "2":
    print("Resultado:", subtrair(num1, num2))


else:
    print("Opção inválida!")