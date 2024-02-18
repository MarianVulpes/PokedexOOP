import pypokedex
import numpy as np
import csv

class Pokemon:
    def __init__(self):
        self.Kanto = np.arange(1, 151)
        
    def write_pokemon(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in self.Kanto:
                dex_number = int(i)
                row = self.get_by_dex(dex_number)
                if row:
                    writer.writerow(row)

    def get_by_dex(self, num):
        assert isinstance(num, int), "Dex must be an integer"
        pok = pypokedex.get(dex=num)
        name = pok.name
        return self.get_poke(name=name)

    def get_poke(self, name: str):
        assert isinstance(name, str), "Name must be a string"
        p = pypokedex.get(name= name)
        dex = p.dex
        name = name.capitalize()
        hp = p.base_stats.hp
        attack = p.base_stats.attack
        defense = p.base_stats.defense
        sp_atk = p.base_stats.sp_atk
        sp_def = p.base_stats.sp_def      
        speed = p.base_stats.speed
        return [dex, name, hp, attack, defense, sp_atk, sp_def, speed]
    
    def base_stats(self): #Usado para teste
        print(self.name)
        print(f"HP:\t{self.hp}")
        print(f"Atk:\t{self.attack}")
        print(f"Def:\t{self.defense}")
        print(f"Spa.Atk:{self.sp_atk}")
        print(f"Spa.Def:{self.sp_def}")
        print(f"Speed:\t{self.speed}\n")

poke = Pokemon()
poke.write_pokemon("dex.csv")