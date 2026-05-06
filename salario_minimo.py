salario_minimo = 1621

salario_usuario = float(input("Digite o valor do seu salário: R$ "))

quantidade_salarios = salario_usuario / salario_minimo

print("Você recebe " + str(round(quantidade_salarios, 2)) + " salários mínimos.")