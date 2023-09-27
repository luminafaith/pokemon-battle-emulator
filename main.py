import random


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
    calcCritical = 1 # TODO: add critical hit mechanics; rounds down to the nearest integer
    calcRandom = random.randint(85, 100) / 100 # TODO: rounds down to the nearest integer
    if(move.moveType == attacker.pokeType):
        calcSTAB = 1.5
    else:
        calcSTAB = 1
    calcTypeEff = 1 # TODO: add type effectiveness mechanics; rounds down to nearest intger
    calcBurn = 1 # TODO: add status effect check for burn
    calcOther = 1 # TODO: add held items and abilities
    calcZMove = 1 # TODO: add z-moves

    # doing the calculation
    step1 = (2 * calcLevel / 5) + 2
    step2 = step1 * calcPower * (calcA / calcD)
    step3 = (step2 / 50) +2
    step4 = step3 * calcTarget * calcPB * calcWeather * calcGlaiveRush * calcCritical
    step5 = round(step4)
    step6 = step5 * calcRandom
    step7 = round(step6)
    step8 = step7 * calcSTAB * calcTypeEff
    step9 = round(step8)
    step10 = step9 * calcBurn * calcOther * calcZMove
    step11 = round(step10)
    
    return step11