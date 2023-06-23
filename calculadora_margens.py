def calcular_probabilidade_impli(custo, preco):
    probabilidade_impli = (preco - custo) / preco * 100
    return probabilidade_impli

def calcular_margem(custo, preco):
    margem = (preco - custo) / preco * 100
    return margem

def calcular_margem_lucro(custo, preco):
    margem_lucro = (preco - custo) / custo * 100
    return margem_lucro

# Solicitar os valores de custo e preço
custo = float(input("Digite o custo do produto: "))
preco = float(input("Digite o preço de venda do produto: "))

# Chame as funções e imprima os resultados
probabilidade_impli = calcular_probabilidade_impli(custo, preco)
margem = calcular_margem(custo, preco)
margem_lucro = calcular_margem_lucro(custo, preco)

print("Probabilidade Implícita: ", probabilidade_impli)
print("Margem: ", margem)
print("Margem de Lucro: ", margem_lucro)

