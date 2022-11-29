from random import randrange

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    
    """
    +-------+-------+-------+
    |       |       |       |
    |   1   |   2   |   3   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   4   |   X   |   6   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   7   |   8   |   9   |
    |       |       |       |
    +-------+-------+-------+
    """
    
    lenB = len(board)
    for i in range(lenB):
        print(('+'+'-'*(7))*3,end='+')
        print('')
        print(('|'+' '*(7))*3,end='|')
        print('')
        for j in range(lenB):
            print('|',end='')
            print('  ',board[i][j],'  ',end='')
        print('|')
        print(('|'+' '*(7))*3,end='|')
        print('')
    print(('+'+'-'*(7))*3,end='+')
    print('')

    return

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    vacios = []
    for i in range(len(board)):
        for j in range(len(board)):
            if type(board[i][j]) == int:
                vacios.append((i,j))
    return vacios

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    flag = 1
    cuadros = []
    errores = 10
    lenB = len(board)
    while flag:
        try:
            flag = 0
            free_fields = make_list_of_free_fields(board)
            if(free_fields == []):
                print("No hay más espacios")
                return 0
            
            print("Los cuadros disponibles para jugar son: ")
            for j,i in free_fields:
                cuadros.append(board[j][i])
            print(cuadros)
            
            print('Seleccione el cuadro a usar: ', end='')
            cuadro = int(input())
            if cuadro in cuadros:
                print("Usted seleccionó el cuadro ", cuadro)
                for row in range(lenB):
                    for val in range(lenB):
                        if board[row][val] == cuadro:
                            board[row][val] = "O"
                            return 1    
                flag=0
            else:
                print("Cuadro no disponible\n")
                cuadros.clear()
                errores-=1
                flag=1
                if errores <= 0:
                    flag = 0
                    print("Pierdes el turno, el cuadro no se actualizará...")
            
        except:
            flag = 1
            errores-=1
            print("Error")   
            if errores <= 0:
                flag = 0
                print("El cuadro no se actualizó")
        
    return 1

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    lenB = len(board)
    ganador = -1
    #Verificar horizontales
    point=0
    for row in board:
        for val in row:
            if val == sign:
                point+=1
            if point == 3:
                ganador = sign
        point = 0    
    
    #Verificar verticales
    point=0
    for col in range(lenB):
        for val in range(lenB):
            if board[val][col] == sign:
                point+=1
            if point == 3:
                ganador = sign
        point = 0    
    
    #Verificar diagonal \
    point=0
    for diag in range(lenB):
        if board[diag][diag] == sign:
            point+=1
        if point == 3:
            ganador = sign
    point = 0 
    
    #Verificar diagonal /
    point=0
    for diag in range(lenB):
        if board[diag][lenB-1-diag] == sign:
            point+=1
        if point == 3:
            ganador = sign
    point = 0 
    return ganador

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    flag = 1
    cuadros = []
    lenB = len(board)
    while flag:
        flag = 0
        free_fields = make_list_of_free_fields(board)
        if(free_fields == []):
            print("No hay más espacios")
            return 0
        
        for j,i in free_fields:
            cuadros.append(board[j][i])
        
        cuadro = randrange(10)
        if cuadro in cuadros:
            for row in range(lenB):
                for val in range(lenB):
                    if board[row][val] == cuadro:
                        board[row][val] = "X"
                        return 1  
            flag=0
        else:
            cuadros.clear()
            flag=1
    return 1


#Inicio del programa
juego = '1'
no_empate = 1
while juego == '1':
    
    game_board = [[i for i in range(1+(j*3),4+(j*3))] for j in range(0,3)]#Inicializar tablero
    game_board[1][1] = 'X'#Primer movimieno de la maquina
    display_board(game_board)#Dibujar tablero
    
    while True:#Inicializar juego
        no_empate = enter_move(game_board)#Pedir movimiento jugador
        display_board(game_board)#Dibujar tablero
        winner =  victory_for(game_board,'O')#Verificar si gana
        
        if winner == 'O':
            print("\n----¡HAS GANADO!----\n")
            break
        
        if no_empate == 0:
            print("\nEMPATE: Fin del juego\n")
            break
        
        no_empate = draw_move(game_board)#Juega la maquina
        display_board(game_board)#Dibujar tablero
        winner =  victory_for(game_board,'X')#Verificar si gana
        
        if winner == 'X':
            print("\n-----HAS PERDIDO-----\n")
            break
        
        if no_empate == 0:
            print("Fin del juego")
            break

    juego = input("Oprime el número 1 para volver a jugar, cualquier otra tecla para salir: ")
