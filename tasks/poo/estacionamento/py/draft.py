class Veiculo:  #classe modelo para as outras classes conseguirem usar ela como atributo
    def __init__(self, id: str, tipo: str):
        self.__id: str = id
        self._tipo: str = tipo
        self._horaEntrada: int = 0

    def getId(self) -> str:   
        return self.__id
    
    def getTipo(self) -> str:
        return self._tipo
    
    def setEntrada(self, horaEntrada: int) -> None:  #faz um set para uma variável que é privada e precisa modificar depois (o valor dela vai modificar)
        self._horaEntrada = horaEntrada

    def getEntrada(self) -> int:
        return self._horaEntrada
    
    def calcularValor(self, horaSaida: int) -> None:     #vai ser usado pelas classes filhas
        pass #dizendo para o código ignora essa parte (abstract)

    # concatenação - ovo banana = ovobanana

    def __str__(self) -> str:
        x = 10 - len(self._tipo) #len conta os indices
        y = 10 - len(self.__id)
        unders = x * "_"   #atribui um valor para que, em vez de mutiplicar toda vez que precisar usar, use o "unders"
        unders2 = y * "_"      
        return f"{unders + self._tipo} : {unders2 + self.__id} : {self._horaEntrada}"

# self._tipo.rjust(10, "_") - até a str chegar na quantidade de caracteres q vc especificou, ele vai add a caractere q vc add para preencher

class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Bike") #coloca entre "" pq na classe mãe pede o tipo que é str

    def calcularValor(self, horaSaida: int):
       return 3
    
class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularValor(self, horaSaida: int):
        tempo = horaSaida - self._horaEntrada
        tempo /= 20
        return tempo
    
class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def calcularValor(self, horaSaida: int):
        tempo = horaSaida - self._horaEntrada
        tempo /= 10
        if tempo < 5:
            return 5
        else:
            return tempo

class Estacionamento:
    def __init__(self):
       self.__horaAtual: int = 0
       self.__veiculos: list[Veiculo] = [] #vetor = lista

    def procurarVeiculo(self, id: str) -> int:
        for i in range(0, len(self.__veiculos)):  #enquanto o i puder admitir um valor entre 0 e o tamanho da lista                       #in transforma o i em alguem
            if self.__veiculos[i].getId() == id:   #pegando o id do veiculo na posição i e comparando com o id que quer achar
                return i
        return -1   #-1 é o simbolo geral da computação indicando que não achou o que estava proucurando no vetor - ele precisa retornar alguma coisa mesmo não tendo achado

#se for pra repetir uma situação varias vezes, usa for ou while
#para fazer uma escolha usa if else, swith case

    def passarTempo(self, tempo: int) -> None:
        self.__horaAtual += tempo

    def estacionar(self, veiculo: Veiculo) -> None: #veiculo é objeto pq ele é feito pela forma de bolo Veiculo (classe)
        veiculo.setEntrada(self.__horaAtual) #chamando a função com um objeto
        self.__veiculos.append(veiculo) #para estacionar, precisa colocar o veiculo na lista. Então pega a lista, usa o append e coloca o que vai colocar na lista

    def pagar(self, id: str) -> None:
        pos = self.procurarVeiculo(id) #pos = posição
        if pos != -1:
            #pegar = self.__veiculos[pos] #pegando o veiculo que ta na posição pos e colocando ele na variavel pegar
            veiculo = self.__veiculos.pop(pos) #pop = se n der um indice pra ela, ela vai tirar o primeiro indice do vetor, se der um indice, ela vai tirar o indice que falou
            print(f"{veiculo.getTipo()} chegou {veiculo.getEntrada()} saiu {self.__horaAtual}. Pagar R$ {veiculo.calcularValor(horaSaida = self.__horaAtual):_.2f}")
#quando a função esta fora da classe na qual esta escrevendo, pega o objeto, coloca . e o nome da função e coloca o ()
#quando a função esta dentro da classe, usa self e o nome da função e coloca ()
#:_.2f se não tiver com nenhuma casa depois da virgula, ele completa com 00

    def __str__(self) -> str:
        if len(self.__veiculos) != 0:
            return f"{"\n".join(str(x) for x in self.__veiculos)}\nHora atual: {self.__horaAtual}"
        else:
            return f"Hora atual: {self.__horaAtual}"


def main():
    estacionamento = Estacionamento() #criando objeto da classe estacionamento

    while True:
        linha: str = input() #a linha é um str e vai receber um input do terminal
        print("$" + linha)
        args: list[str] = linha.split(" ") #args que é do tipo lista e essa lista vai poder ter uma str dentro. Args é uma lista de str |||| pegar a str e quebrar ela toda, ele lê palavra por palavra, então é preciso quebrar ela pro código entender o comando
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionamento) #printa a variável, não a classe
        elif args[0] == "tempo":
            estacionamento.passarTempo(tempo= int(args[1]))   #tipoQueVoceQuer(variavelQueVoceQuerNesseTipo)
        elif args[0] == "estacionar":
            if args[1] == "bike":
                veiculo = Bike(args[2])
                estacionamento.estacionar(veiculo)
            elif args[1] == "moto":
                veiculo = Moto(args[2])
                estacionamento.estacionar(veiculo)
            elif args[1] == "carro":
                veiculo = Carro(args[2])
                estacionamento.estacionar(veiculo)
        elif args[0] == "pagar":
            estacionamento.pagar(args[1])

main()