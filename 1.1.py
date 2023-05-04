nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ano_nascimento = 2022 - idade

for ano in range(ano_nascimento, 2024):
    print(f"No ano de {ano} {nome} completa {ano - ano_nascimento} anos.")
if idade <= 12:
    print("Portanto você é uma criança.")
elif idade <= 16:
    print("Portanto você é um adolescente.")
elif idade <= 59:
    print("Portanto você é um adulto.")
else:
    print("Portanto você é um idoso.")
