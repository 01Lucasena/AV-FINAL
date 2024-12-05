from abc import ABC, abstractmethod
from project.models.endereco import Endereco
from dataclasses import dataclass

@dataclass
class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:

        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        return self.salario

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"\nNome: {self.nome}"
            f"\nE-mail: {self.email}"
            f"\nSalário: {self.salario}"
            f"\nEndereço: {self.endereco}"
        )