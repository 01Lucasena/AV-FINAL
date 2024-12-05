import os
from project.models.endereco import Endereco
from project.models.funcionario import Funcionario
from project.models.engenheiro import Engenheiro
from project.models.nutricionista import Nutricionista
os.system("cls||clear")

nutricionista = Nutricionista(
    crn = input("Digite seu CRN: "),
    nome = input("Digite seu nome: "),
    email = input("Digite seu email: "),
    salario = float(input("Digite seu salário:")),
    endereco = Endereco(
    logradouro = input("Digite seu logradouro: "),
    numero = input("Digite seu número: "),
    complemento = input("Digite seu complemento: "),
    )
)

engenheiro = Engenheiro(
    crea = input("\nDigite seu CREA: "),
    nome = input("Digite seu nome: "),
    email = input("Digite seu email: "),
    salario = float(input("Digite seu salário:")),
    endereco = Endereco(
    logradouro = input("Digite seu logradouro: "),
    numero = input("Digite seu número: "),
    complemento = input("Digite seu complemento: "),
    )
)

print(nutricionista)
print(engenheiro)
