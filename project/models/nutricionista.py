from project.models.funcionario import Funcionario

class Nutricionista(Funcionario):
    def __init__(self, crn: str,  nome, email, salario, endereco):
        super().__init__(nome, email, salario, endereco)

        self.crn = crn
        
    
    def salario_final(self):
        pass
    
    def __str__(self):
        return (
            f"{super().__str__()}"
            f"CREA: {self.crn}"            
            f"Salário Final: {self}"            
        )