class Funcionario:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    def getNome(self) -> str:
        return self.nome

    def getCpf(self) -> str:
        return self.cpf

    def getSalario(self) -> float:
        return self.salario

    def getTipo(self):
        return self.tipo

    def getClasse(self):
        return self.classe

    def getNivel(self):
        return self.nivel

    def getInsalubre(self):
        return self.insalubre

