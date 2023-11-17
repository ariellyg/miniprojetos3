from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        super().__init__(nome, cpf)
        self.nome = nome
        self.cpf = cpf
        self.nivel = nivel
        self.tipo = Tipo.STA
        self.salario= 1000 + 100 * self.nivel



