from src.aluno.base.circulo import Circulo
from src.aluno.base.contato import Contato
from src.cliente.circulo_base import CirculoBase
from src.cliente.circulo_not_found_exception import CirculoNotFoundException
from src.cliente.contato_base import ContatoBase
from src.cliente.contato_not_found_exception import ContatoNotFoundException
from src.cliente.icirculo_operations_manager import ICirculoOperationsManager
from src.cliente.icirculos_manager import ICirculosManager
from src.cliente.icontatos_manager import IContatosManager



class GContatos(IContatosManager, ICirculosManager, ICirculoOperationsManager):

    def __init__(self):
        self.contatos = []
        self.favoritos = []
        self.circulos = []
    def createContact(self, id: str, email: str) -> bool:
        for contato in self.contatos:
            if contato.getId() == id:
                return False
        Novoctt= Contato(id, email)
        self.contatos.append(Novoctt)
        return True

    def getAllContacts(self) -> list:
        return sorted(self.contatos, key=lambda c: c.getId())

    def updateContact(self, contato: Contato) -> bool:
        for ctt in self.contatos:
            if ctt.id == contato.id:
                ctt.email = contato.email
                return True

        return False

    def removeContact(self, id: str) -> bool:
        removed = False
        contatosParaRemover = []
        for contato in self.contatos:
            if contato.getId() == id:
                contatosParaRemover.append(contato)
                removed = True
        for contato in contatosParaRemover:
            self.contatos.remove(contato)
            for circulo in self.circulos:
                for ctt in circulo.cttcirculo:
                    if ctt.getId() == id:
                        circulo.cttcirculo.remove(ctt)
            if contato in self.favoritos:
                self.favoritos.remove(contato)

        return removed

    def getContact(self, id: str) -> Contato:
        for contato in self.contatos:
            if contato.getId() == id:
                return contato
        return None

    def getNumberOfContacts(self) -> int:
        return len(self.contatos)

    def favoriteContact(self, idContato: str) -> bool:
        for contato in self.contatos:
            if contato.getId() == idContato:
                self.favoritos.append(contato)
                return True
        return False

    def unfavoriteContact(self, idContato: str) -> bool:
        for contato in self.contatos:
            if contato.getId() == idContato:
                self.favoritos.remove(contato)
                return True
        return False
    def isFavorited(self, id: str) -> bool:
        if id in self.favoritos:
            return True
        return False

    def getFavorited(self) -> list:
        return sorted(self.favoritos, key=lambda x: x.getId())

    def createCircle(self, id: str, limite: int) -> bool:
        for circulo in self.circulos:
            if circulo.getId() == id:
                return False
        Novocirc= Circulo(id, limite)
        self.circulos.append(Novocirc)
        return True

    def updateCircle(self, circulo: Circulo) -> bool:
        if circulo.getLimite() <= 0:
            return False
        for index, circle in enumerate(self.circulos):
            if circle.getId() == circulo.getId():
                self.circulos[index].limite = circulo.getLimite()
                return True

        return False

    def getCircle(self, idCirculo: str) -> Circulo:
        for circulo in self.contatos:
            if circulo.getId() == idCirculo:
                return circulo
        return None

    def getAllCircles(self) -> list:
        return sorted(self.circulos, key=lambda c: c.getId())

    def removeCircle(self, idCirculo: str) -> bool:
        for circulo in self.circulos:
            if circulo.getId() == idCirculo:
                self.circulos.remove(circulo)
                return True
        return False

    def getNumberOfCircles(self) -> int:
        return len(self.circulos)

    def tie(self, idContato: str, idCirculo: str) -> bool:
        ContatoEncontrado = False
        CirculoEncontrado = False
        for contato in self.contatos:
            if contato.getId() == idContato:
                ContatoEncontrado = True
                break
        if not ContatoEncontrado:
            raise ContatoNotFoundException(idContato)
        for circulo in self.circulos:
            if circulo.getId() == idCirculo:
                CirculoEncontrado = True
                break
        if not CirculoEncontrado:
            raise CirculoNotFoundException(idCirculo)
        for circulo in self.circulos:
            if circulo.getId() == idCirculo and circulo.getLimite() > circulo.getNumberOfContacts():
                for ctt in self.contatos:
                    if ctt.getId() == idContato and ctt not in circulo.cttcirculo:
                        circulo.cttcirculo.append(ctt)
                        return True

        return False


    def untie(self, idContato: str, idCirculo: str) -> bool:
        contato_encontrado = False
        for contato in self.contatos:
            if contato.getId() == idContato:
                contato_encontrado = True
                break
        if not contato_encontrado:
            raise ContatoNotFoundException(idContato)
        circulo_encontrado = False
        for circulo in self.circulos:
            if circulo.getId() == idCirculo:
                circulo_encontrado = True
                if contato in circulo.cttcirculo:
                    circulo.cttcirculo.remove(contato)
                    return True
                break
        if not circulo_encontrado:
            raise CirculoNotFoundException(idCirculo)

        return False

    def getContacts(self, id: str) -> list:
        if id not in [circle.id for circle in self.circulos]:
            raise CirculoNotFoundException(id)

        for circulo in self.circulos:
            if circulo.getId() == id:
                return sorted(circulo.cttcirculo, key=lambda c: c.getId())
        return None

    def getCircles(self, id: str) -> list:
        if id not in [ctt.getId() for ctt in self.contatos]:
            raise ContatoNotFoundException(id)
        circulos = []

        for circulo in self.circulos:
            for ctt in circulo.cttcirculo:
                if ctt.getId() == id:
                    circulos.append(circulo)
        return sorted(circulos, key=lambda c: c.getId())

    def getCommomCircle(self, idContato1: str, idContato2: str) -> list:
        if idContato1 not in [ctt.getId() for ctt in self.contatos]:
            raise ContatoNotFoundException(idContato1)

        if idContato2 not in [ctt.getId() for ctt in self.contatos]:
            raise ContatoNotFoundException(idContato2)
        oscirculos = []
        for circulo1 in self.getCircles(idContato1):
            for circulo2 in self.getCircles(idContato2):
                if circulo1 == circulo2:
                    oscirculos.append(circulo1)
