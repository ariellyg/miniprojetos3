from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        super().__init__(nome, cpf)
        self.nome = nome
        self.cpf = cpf
        self.classe = classe
        self.tipo = Tipo.PROF
        if self.classe == 'A':
             self.salario = 3000.0
        elif self.classe == 'B':
            self.salario= 5000.0
        elif self.classe == 'C':
            self.salario= 7000.0
        elif self.classe == 'D':
            self.salario = 9000.0
        elif self.classe == 'E':
            self.salario = 11000.0
