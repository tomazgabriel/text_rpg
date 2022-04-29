import jogador as jg
import comandos as c

script_loop = True
script_loop_game = True

jogador = jg.Jogador()
teste = 1

while script_loop == True:
    while script_loop_game == True:
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


    script_loop = False