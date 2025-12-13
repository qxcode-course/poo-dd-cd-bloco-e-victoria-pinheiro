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

class CartaoCredito:
    def __init__(self, valor: float, descricao: str, numero: str, nomeTitular: str, limiteDisponivel: int):
        super().__init__(valor, descricao)
        self.__numero: str = numero
        self.__nomeTitular: str = nomeTitular
        self.__limiteDisponivel: int = limiteDisponivel

    def processar(self):
        if self._valor > self.__limiteDisponivel:
            print("pagamento recusado")                
        else:
            self.__limiteDisponivel -= self._valor
            print("pagamento confirmado") 
        
class Pix:
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.__chave: str = chave
        self.__banco: str = banco

    def processar(self):
        self.validarValor() 
        print(f"{self.__banco} {self.__chave}")

    