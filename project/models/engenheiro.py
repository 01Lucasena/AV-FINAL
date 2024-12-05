from project.models.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, crea: str,  nome, email, salario, endereco):
        super().__init__(nome, email, salario, endereco)

        self.crea = crea
        
    
    def salario_final(self):
        pass
    
    def __str__(self):
        return (
            f"{super().__str__()}"
            f"CREA: {self.crea}"            
            f"Salário Final: {self.salario_final}"            
        )