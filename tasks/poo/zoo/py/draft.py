class Animal:
    def __init__(self, nome: str):
        self.__nome: str = nome

    def apresentarNome(self) -> str:
        return f"Eu sou um(a) {self.__nome}!"
    
    def fazerSom(self):
        pass

    def mover(self):
        pass

class Leao(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazerSom(self):
        return f"Ruaaawww"
    
    def mover(self):
        return f"azunhada"
    
class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazerSom(self):
        return f"fummmm uuhhhh"
    
    def mover(self):
        return f"jogar água"

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazerSom(self):
        return f"pssiiiiiiiiiiihhhhrhrhrhhr"
    
    def mover(self):
        return f"picada"
    
def main():
    animal = Animal()

    while True:
        linha: str = input()
        print("$" + linha)
        args: list[str] = linha.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(animal)
    
main()