from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self._valor: float = valor #float é numero com virgula
        self._descricao: str = descricao

    def resumo(self):
        print(f"Pagamento de R$ {self._valor}: {self._descricao}")

    def validarValor(self):
        if self._valor <= 0:
            raise ValueError("fail: valor inválido") #lança uma exceção. -> lança exceção para economizar retorno. Quando fala que algo ta errado, usa ela para evitar que o codigo pare para dizer que retornou errado, no caso, em vez disso, ele para o codigo e diz que esta errado

    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: str, nomeTitular: str, limiteDisponivel: float):
        super().__init__(valor, descricao)
        self.__numero: str = numero
        self.__nomeTitular: str = nomeTitular
        self.__limiteDisponivel: float = limiteDisponivel

    def processar(self):
        if self._valor > self.__limiteDisponivel:
            print("pagamento recusado")                
        else:
            self.__limiteDisponivel -= self._valor
            print("pagamento confirmado") 
        
class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.__chave: str = chave
        self.__banco: str = banco

    def processar(self):
        self.validarValor() 
        print(f"{self.__banco} {self.__chave}")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigoBarras:  str, vencimento: str):
        super().__init__(valor, descricao)
        self.__codigoBarras: str = codigoBarras
        self.__vencimento: str = vencimento

    def processar(self):
        print(f"Boleto gerado. Aguardando pagamento...")

def processar_pagamento(pagamento: Pagamento):
    pagamento.validarValor()
    pagamento.resumo()
    pagamento.processar()
    print(isinstance(pagamento, Pix))

pagamentos = [Pix(150, "Camisa Esportiva", "email@uxui.com", "Banco Nubank"), CartaoCredito(120, "Show Marisa Monte", "1234 5678 9012 1314", "vic", 740)]
for i in pagamentos:
    i.resumo()

