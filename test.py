class Pokemon:
    all = []
    def __init__(self, Name: str, Atk: int, Speed: int):
        #Validação
        assert isinstance(Name, str), "Name must be a string"

        #Self Objeto
        self.Name = Name
        self.Atk = Atk
        self.Speed = Speed

        #Ação
        Pokemon.all.append(self)

    def __repr__(self): #Controla como o objeto é impresso na tela
        return f"Pokemon('{self.Name}')"
    
pok1 = Pokemon("Weavile", 120, 125)
pok2 = Pokemon("Landorus", 125, 101)

print(Pokemon.__dict__) #Todos os atributos em Nível de Classe
print(pok1.__dict__) #Todos os atributos em Nível de Instância
print(Pokemon.all) #Todas as instâncias da Classe