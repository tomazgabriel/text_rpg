from numpy import diag
import jogador as jg
import os
import random as rr


global dia
dia = 1
jogador = jg.Jogador()

def limparConsole():
    print("\n\n")
    comando_exit = input("Pressione c para continuar ")
    if comando_exit == "c":
        clear = lambda : os.system('cls')
        clear()
def limparConsoleAuto():
    clear = lambda : os.system('cls')
    clear()        

limparConsole()
#nome
nome = input("Digite seu nome: ")

def statusJogador():
    print(f"\nStatus:\nDia:{dia} Nome:{nome} Level:{jogador.level} XP:{jogador.xp} Prox.LVL:{jogador.nextlvlxp} Hp:{jogador.hp} Ataque:{jogador.ataque} Defesa:{jogador.defesa} Comida:{jogador.comida} Espaço:{jogador.inventario}")
    print(f"\nSelecione um comando: \n D - Descansar, A - Atividades,  L - Lutar, I - Inventário, S - Sair")


def controleLevel():
    if jogador.xp >= jogador.nextlvlxp:
        print("\nVocê passou de level! Escolha um atributo:\n A - Ataque\n D - Defesa")
        atribute = input(" ")
        if atribute == "a" or atribute == "A":
            jogador.ataque += 1
        elif atribute == "d" or atribute == "D":
            jogador.defesa += 1
            jogador.maxHp += 1
            jogador.xp = 0
            jogador.level += 1
        limparConsole()


def descansar():
    if jogador.hp > jogador.maxHp and jogador.comida > 1:
        jogador.hp = jogador.maxHp
    elif jogador.hp < jogador.maxHp and jogador.comida > 1:
        jogador.hp += 5
        jogador.comida -= 1
    print(f"\nSeu hp é: {jogador.hp}")
    global dia
    dia += 1



def inventario():
    print(f"\nEquipando:\n Arma:{jogador.arma}\nArmadura:{jogador.armadura}")
    limparConsole()


def lutar():
    inimigo_cap = rr.randint(1, (jogador.level+3))
    inimigo_hp = inimigo_cap + 10
    inimigo_att = inimigo_cap + rr.randint(inimigo_cap, (inimigo_cap + 3))
    inimigo_def = inimigo_cap + rr.randint(inimigo_cap, (inimigo_cap + 3))
    inimigo_vida = True
    while inimigo_vida == True:
        print(f"\n Você encontrou um inimigo com level {inimigo_cap}, o que fazer:\n A - Atacar\n D - Defender\n F - Fugir")
        comando_luta = input("")
        #Quando derrotar o inimigo
        if inimigo_hp <= 0:
            jogador.xp += inimigo_cap
            inimigo_vida = False
            limparConsole()
        #Quando perder
        if jogador.hp <= 0:
            print("\n Você perdeu e seu XP foi reduzido")
            jogador.xp = 0
            jogador.hp = jogador.maxHp
            inimigo_vida = False
            limparConsole()
        #Fugir
        if comando_luta == "f" or comando_luta == "F":
            inimigo_vida = False
            limparConsole()
        #Combate
        if jogador.hp > 0 and inimigo_hp > 0:
            if comando_luta == "a" or comando_luta == "A":
                dano = (jogador.ataque - inimigo_def)
                dano_inimigo = (inimigo_att - jogador.defesa)
                if dano <= 0:
                    dano = 1
                if dano_inimigo <= 0:
                    dano_inimigo = 0
                jogador.hp -= dano_inimigo
                inimigo_hp -= dano
                #print(f"\n Você atacou e criou {dano} de dano!\n Você foi atacado e recebeu {dano_inimigo} de dano!")
                historico = f"\n Você atacou e criou {dano} de dano!\n Você foi atacado e recebeu {dano_inimigo} de dano!"
                limparConsoleAuto()

            elif comando_luta == "d" or comando_luta == "B":
                dano = (jogador.defesa - inimigo_att)
                dano_inimigo = (jogador.defesa - inimigo_att)
                if dano <= 0:
                    dano = 0
                if dano_inimigo <= 0:
                    dano_inimigo = 0
                jogador.hp -= dano_inimigo
                inimigo_hp -= dano
                #print(f"\n Você atacou e criou {dano} de dano!\n Você foi atacado e recebeu {dano_inimigo} de dano!")
                historico = f"\n Você atacou e criou {dano} de dano!\n Você foi atacado e recebeu {dano_inimigo} de dano!"
                limparConsoleAuto()
            #Status da batalha
            print(f"\nStatus da batalha: HP:{jogador.hp}   HP Inimigo:{inimigo_hp}\n{historico}")

def atividades():
    limparConsoleAuto()
    x = input("\n P - pescar")

    if x == 'p' or x == 'P':
        limparConsoleAuto()
        print(f"\nSeu nível de pesca atual é:{jogador.pesca}")



