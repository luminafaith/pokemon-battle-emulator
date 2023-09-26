class Pokemon:
    def __init__(self, pokeNameInputted, pokeTypeInputted):
        self.pokeName = pokeNameInputted
        self.level = 5
        self.hp = 15
        self.attack = 10
        self.defence = 10
        self.specialAttack = 10
        self.specialDefence = 10
        self.speed = 10
        self.pokeType = pokeTypeInputted
    
    def __init__(self, pokeNameInputted, pokeTypeInputted, levelInputted, hpInputted, attackInputted, defenceInputted, specialAttackInputted, specialDefenceInputted, speedInputted):
        self.pokeName = pokeNameInputted
        self.level = levelInputted
        self.hp = hpInputted
        self.attack = attackInputted
        self.defence = defenceInputted
        self.specialAttack = specialAttackInputted
        self.specialDefence = specialDefenceInputted
        self.speed = speedInputted
        self.pokeType = pokeTypeInputted

class Move:
    def __init__(self, moveNameInputted, moveTypeInputted, powerInputted, accuracyInputted, categoryInputted):
        self.moveName = moveNameInputted
        self.moveType = moveTypeInputted
        self.movePower = powerInputted
        self.moveAccuracy = accuracyInputted
        self.moveCategory = categoryInputted

def calcDamage(attacker, defender, move):
    calcLevel = attacker.level
    calcPower = move.movePower
    if(move.moveCategory == 'physical'):
        calcA = attacker.attack
        calcD = defender.defence
    else:
        calcA = attacker.specialAttack
        calcD = defender.specialDefence
    calcTarget = 1
    calcPB = 1
    calcWeather = 1 # TODO: add weather
    calcGlaiveRush = 1 # TODO: add glaive rush move (gen 9, a long ways off)
    return 5