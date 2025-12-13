from abc import ABC, abstractmethod  #usa para o "contrato" obriga certas coisas 

class Animal(ABC):  #a classe mãe agora é uma classe filha de ABC mas ainda é classe mãe do resto   
    def __init__(self, nome: str):
        self.__nome: str = nome

    def apresentarNome(self) -> str:   #metodo concreto = função com codigo
        print(f"Eu sou um(a) {self.__nome}!")       #se esta retornando, precisa printar depois
    
    @abstractmethod #agora coloca isso acima das funções abstratas
    def fazerSom(self):
        pass

    @abstractmethod  #metodo abstrato = função sem código
    def mover(self):
        pass

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazerSom(self):
        print(f"Ruaaawww")
    
    def mover(self):
        print(f"azunhada")
    
class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazerSom(self):
        print(f"fummmm uuhhhh")
    
    def mover(self):
        print(f"jogar água")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazerSom(self):
        print(f"psiiiiiiiiiiiiiisiihrhrhrh")

    
    def mover(self):
        print(f"picada")
    

    # "animal = Animal()" -> Não se cria objeto da classe mãe
    
    #função global: não é relacionada a um objeto especifico e pode ser usada em qualquer momento

def apresentar(animal: Animal):
    animal.apresentarNome()
    animal.fazerSom()
    animal.mover()
    print(isinstance(animal, Cobra))

animal = Cobra("Jararaca")
apresentar(animal)   #ja que apresentar é uma função global, não chama ela a pertir de uma classe
    
bixo = [Elefante("dumbo"), Leao("simba"), Cobra("coral")]
for i in bixo:
    apresentar(i)