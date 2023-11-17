from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class Terceirizado(Funcionario):

    def __init__(self, cpf: str, nome: str, insalubre: bool):
        super().__init__(nome, cpf)
        self.nome = nome
        self.cpf = cpf
        self.insalubre = insalubre
        self.tipo = Tipo.TERC
        if self.insalubre:
            self.salario = 1500
        else:
            self.salario = 1000

