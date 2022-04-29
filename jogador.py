class Jogador:
    def __init__(self):
        self.arma = 5
        self.armadura = 5
        self.hp = 10
        self.maxHp = 10
        self.ataque = 1 + self.arma
        self.defesa = 1 + self. armadura
        self.comida = 0
        self.inventario = 100 - self.comida
        self.level = 1
        self.xp = 0
        self.nextlvlxp = self.level * 100
        pass
