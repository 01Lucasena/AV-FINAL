class Endereco:

    def __init__(self, logradouro: str, numero: str, complemento: str):
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
    
    def __str__(self):
        return (
            
            f"\nLogradouro: {self.logradouro} || Número: {self.numero} || Complemento: {self.complemento}"
        )
    

 
