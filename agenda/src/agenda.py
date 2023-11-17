from src.contato import Contato
from src.identificador import Identificador


class Agenda:

    def __init__(self):
        self.contatos = []

    def getContatos(self) -> list:
        return sorted(self.contatos, key=lambda contato: contato.getName())

    def getQuantidadeDeContatos(self) -> int:
        return len(self.contatos)

    def getContato(self, nome:str) -> Contato:
        for contato in self.contatos:
            if contato.getName() == nome:
                return contato

    def adicionarContato(self, contato: Contato) -> bool:
        if len(self.contatos) > 0:
            actt= False
            for nome in self.contatos:
                if nome.getName() == contato.getName():
                    actt = True
                    for fone in contato.getFones():
                        nome.adicionarFone(fone)

            if actt:
                return False
            else:
                self.contatos.append(contato)
                return True
        else:
            self.contatos.append(contato)
            return True

    def removerContato(self, nome: str) -> bool:
        for contato in self.contatos:
            if contato.getName() == nome:
                self.contatos.remove(contato)
                return True

        return False

    def removerFone(self, nome:str, index: int) -> bool:
        for contato in self.contatos:
            if contato.getName() == nome and 0 < index < contato.getQuantidadeFones():
                contato.removerFone(index)
                return True

        return False


    def getQuantidadeDeFonesPorIdentificador(self, identificador: Identificador) -> int:
        QuantFones = 0
        for contato in self.contatos:
            for fone in contato.fones:
                if fone.getIdentificador() == identificador:
                    QuantFones += 1

        return QuantFones

    def getQuantidadeDeFones(self) -> int:
        QuantFones = 0
        for contato in self.contatos:
            if contato:
                QuantFones += contato.getQuantidadeFones()

        return QuantFones

    def pesquisar(self, expressao:str) -> list:
        listaPesquisa = []
        for contato in self.contatos:
            if expressao in contato.getName():
                listaPesquisa.append(contato)
            for fone in contato.getFones():
                if expressao in fone.numero:
                    listaPesquisa.append(contato)
        listaPesquisa = sorted(listaPesquisa, key=lambda contato: contato.getName())
        return listaPesquisa




