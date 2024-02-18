import csv

class Pokemon:
    all = []
    def __init__(self, dex, name, hp, attack, defense, sp_atk, sp_def, speed):
        self.Dex = dex
        self.Name = name
        self.Hp = hp
        self.Attack = attack
        self.Defense = defense
        self.Sp_Atk = sp_atk
        self.Sp_Def = sp_def      
        self.Speed = speed

        Pokemon.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("dex.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    Pokemon(
                    dex = row[0],
                    name = row[1], 
                    hp = int(row[2]), 
                    attack = int(row[3]),
                    defense = int(row[4]),
                    sp_atk= int(row[5]),
                    sp_def = int(row[6]),
                    speed= int(row[7])
                    )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): #Controla como o objeto é impresso na tela
        return f"'{self.Name}', '{self.Hp}', '{self.Attack}', '{self.Defense}', '{self.Sp_Atk}', '{self.Sp_Def}', '{self.Speed}')\n"

class Legendary(Pokemon): #Child Class
    def __init__(self, dex, name, hp, attack, defense, sp_atk, sp_def, speed):
        super().__init__(dex, name, hp, attack, defense, sp_atk, sp_def, speed) #super() serve para usar a função da classe pai como está lá

    @classmethod
    def instantiate_legendaries_from_csv(cls):
        legendaries = ["Articuno", "Zapdos", "Moltres", "Mew", "Mewtwo"]
        with open("dex.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[1] in legendaries:
                    cls(
                        dex=int(row[0]),
                        name=row[1], 
                        hp=int(row[2]), 
                        attack=int(row[3]),
                        defense=int(row[4]),
                        sp_atk=int(row[5]),
                        sp_def=int(row[6]),
                        speed=int(row[7])
                    )

    def __repr__(self):
            return f"{self.__class__.__name__} " + super().__repr__()

# Pokemon.instantiate_from_csv()
Legendary.instantiate_legendaries_from_csv()
print(Legendary.all)

# Verifica se um determinado valor é inteiro num Pokémon específico usando o método estático
#bulbasaur = next(pokemon for pokemon in Pokemon.all if pokemon.Name == "Bulbasaur")
#print(Pokemon.is_integer(bulbasaur.Hp))


#print(Pokemon.all) #Mostra todos os Pokémon listados

# print(Pokemon.all) #Todas as instâncias da Classe