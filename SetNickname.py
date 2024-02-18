from Class_Poke import Pokemon

class Nickname:
    def __init__(self, pokemon, nickname):
        self._pokemon = pokemon
        self._nickname = nickname

    @property
    def pokemon(self):
        return self._pokemon
    
    @property
    def nickname(self):
        return self._nickname
    
    @nickname.setter # Se necessário ainda permitir a troca de nome utilize esse decorador
    def nickname(self, new_nickname):
        # raise AttributeError("Nickname cannot be changed") #Impede que o Nickname seja trocado
        self._nickname = new_nickname

    def __repr__(self): 
        return f"{self._nickname}"

    
pikachu = Pokemon(25, "Pikachu", 35, 55, 40, 50, 50, 90)
pikachu_nickname = Nickname(pikachu, "Sparky")

print(f'O Pikachu é chamado de {pikachu_nickname}')

try:
    pikachu_nickname.nickname = "Thunder"
except AttributeError as e:
    print(e)

print(f'O Pikachu agora é chamado de {pikachu_nickname}')
