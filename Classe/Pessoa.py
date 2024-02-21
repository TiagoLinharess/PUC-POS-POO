import abc

class Pessoa(abc.ABC):
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
    
    @abc.abstractmethod
    def consulta_nome(self) -> str:
        return self.__nome
        
    
class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str):
        super().__init__(nome, idade)
        self.__curso = curso
    
    def consulta_nome(self) -> str:
        return f'{super().consulta_nome()} {self.__curso}'

pessoa_1 = Aluno("Tiago", 12, "SI")
pessoa_2 = Aluno("Anna Julia", 23, "Medicina")

print(pessoa_1.consulta_nome())
print(pessoa_2.consulta_nome())