from src.cliente.circulo_base import CirculoBase


class Circulo(CirculoBase):

    def __init__(self, id: str, limite: int):
        super().__init__(id, limite)
        self.id = id
        self.limite = limite
        self.cttcirculo = []

    def getNumberOfContacts(self):
        return len(self.contatos)


    def setLimite(self, limite: int):
        self.limite = limite

    def __eq__(self, other):
        return self.id == other.id