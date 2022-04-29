import jogador as jg
import comandos as c

script_loop = True
script_loop_game = True

jogador = jg.Jogador()
teste = 1

while script_loop == True:
    while script_loop_game == True:
        #morte
        if jogador.hp < 0:
            print("\n Você perdeu e seu XP foi reduzido")
            jogador.xp = 0
            jogador.hp = jogador.maxHp
            c.limparConsole()

        c.statusJogador()
        comando = input("")
        #LVL
        c.controleLevel()
        #sair
        if comando == "s" or comando == "S":
            script_loop_game = False
        #descansar
        elif comando == "d" or comando == "D":
            c.descansar()

        #inventário
        elif comando == "i" or comando == "I":
            c.inventario()

        #Lutar
        elif comando == "l" or comando == "L":
            c.lutar()
        
        #atividades
        elif comando == "a" or comando == "A":
            c.atividades()


    script_loop = False