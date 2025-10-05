class Towel:
    def __init__(self, color:str, size:str):
        self.color=color
        self.size=size
        self.wetness: int = 0
    def getMaxWetness (self) -> int: 
        if self.size =="P":
            return 10
        if self.size == "M":
            return 20
        if self.size== "G":
            return 30
        return 0
        
    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()
    def wringOut(self) -> None:
        self.wetness = 0
    
    def isDry(self) -> bool:
        return self.wetness == 0


    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self.color} {self.size} {self.wetness}"
    
    
towel = Towel("rosa", "G")
towel.show()  
towel.dry(5)
towel.show()  
print(towel.isDry()) 
towel.dry(10)
towel.show()  
towel.dry(10) 
towel.show()  

towel.wringOut()
towel.show()  

towel = Towel("preto", "P")
print(towel.isDry()) 
towel.dry(5)
towel.show()
print(towel.isDry())
towel.dry(1)