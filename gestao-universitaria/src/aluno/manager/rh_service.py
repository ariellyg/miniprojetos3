from src.aluno.base.funcionario import Funcionario
from src.cliente.irh_service import IRHService
from src.cliente.tipo import Tipo


class RHService(IRHService):

    def __init__(self):
        self.funcionarios = []
        self.diarias = {}
        self.divisaolucros = 0

    def cadastrar(self, funcionario: Funcionario):
        if funcionario.getTipo() == Tipo.PROF:
            if funcionario.getClasse() not in ['A','B','C','D','E']:
                return False
        if funcionario.getTipo() == Tipo.STA:
            if funcionario.getNivel() not in range(1, 31):
                return False
        for afuncionario in self.funcionarios:
            if afuncionario.getCpf() == funcionario.getCpf():
                return False

        self.funcionarios.append(funcionario)
        return True

    def remover(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                self.funcionarios.remove(funcionario)
                return True
        return False

    def obterFuncionario(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                return funcionario
        return None

    def getFuncionarios(self):
        funcionariosEmOrdem = sorted(self.funcionarios, key=lambda f: f.getNome())
        return funcionariosEmOrdem

    def getFuncionariosPorCategorias(self, tipo):
        funcionariosTipo = []
        for funcionario in self.funcionarios:
            if tipo == funcionario.getTipo():
                funcionariosTipo.append(funcionario)
        funcionariosEmOrdemPorTipo = sorted(funcionariosTipo, key=lambda f: f.getNome())
        return funcionariosEmOrdemPorTipo

    def getTotalFuncionarios(self):
        return len(self.funcionarios)

    def solicitarDiaria(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf and funcionario.getTipo() != Tipo.TERC:
                NomeFuncionario = funcionario.getNome()
                if NomeFuncionario not in self.diarias:
                    self.diarias[NomeFuncionario] = 0
                if funcionario.getTipo() == Tipo.PROF and self.diarias[NomeFuncionario] < 3:
                    funcionario.salario += 100
                    self.diarias[NomeFuncionario] += 1
                    return True
                elif funcionario.getTipo() == Tipo.STA and self.diarias[NomeFuncionario] < 1:
                    funcionario.salario += 100
                    self.diarias[NomeFuncionario] += 1
                    return True

        return False

    def partilharLucros(self, valor: float):
        if self.getTotalFuncionarios() == 0:
            return False
        self.divisaolucros = valor / self.getTotalFuncionarios()
        for funcionario in self.funcionarios:
            funcionario.salario += self.divisaolucros
        return True

    def iniciarMes(self):
        for funcionario in self.funcionarios:
            funcionario.salario -= self.divisaolucros
            
        self.diarias.clear()
        return True

    def calcularSalarioDoFuncionario(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario.getCpf() == cpf:
                return funcionario.getSalario()
        return None

    def calcularFolhaDePagamento(self):
        TotalSalarios = 0
        for funcionario in self.funcionarios:
            TotalSalarios += funcionario.getSalario()
        return TotalSalarios

