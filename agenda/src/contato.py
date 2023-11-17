from src.fone import Fone


class Contato:

    def __init__(self, nome):
        self.nome = nome
        self.fones = []
    def getName(self) -> str:
        return self.nome

    def getQuantidadeFones(self) -> int:
        return len(self.fones)

    def getFones(self) -> list:
        return self.fones

    def adicionarFone(self, fone: Fone) -> bool:
        if fone.validarNumero(fone.numero):
            self.fones.append(fone)
            return True
        return False

    def removerFone(self, index: int) -> bool:
        if index < 0 or index > len(self.fones):
            return False
        del self.fones[index]
        return True
