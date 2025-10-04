
class Animal:
    def __init__ (self, species:str, sound:str):
        self.species= species
        self.sound = sound
        self.age=0
    def make_sound(self) -> str:
        if self.age == 0:
            return "---"
        if self.age == 4:
            return "RIP"
        return self.sound
    def age_by (self,increment: int):
        if self.age >= 4:
            print(f"warning:{self.species} morreu")
            return
        self.age += increment
        if self.age >= 4:
            print(f"warning:{self.species} morreu")
            self.age = 4
        
    def __str__ (self)-> str:
        return f"{self.species}:{self.age}:{self.sound}"
def main ():
        animal=Animal("","")
        while True:
            try:
                line = input()
            except EOFError:
                break
            print(f"${line}")
            par=line.split()
            if not par:
                continue
            cmd=par[0]
            if cmd == "end":
                break
            elif cmd == "init":
                if len(par)<3:
                    print("fail: faltam argumentos")
                    continue
                species=par[1]
                sound=par[2]
                animal=Animal(species,sound)
            elif cmd == "grow":
                if len(par)<2:
                    print("fail: faltam argumentos")
                    continue
                try:
                    increment=int(par[1])
                    animal.age_by(increment)
                except ValueError:
                    print("fail: o incremento deve ser um inteiro")
            elif cmd == "show":
                print(animal)
            elif cmd == "sound":
                print(animal.make_sound())
            else:
                print("fail: comando invalido")
if __name__ == "__main__":
    main()               