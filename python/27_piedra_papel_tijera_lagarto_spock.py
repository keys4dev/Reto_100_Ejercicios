'''
/*
 * Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
 *   "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
 * - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
 * - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.
 */
'''
#Mismo metodo resuelto mediante las combinaciones ganadoras
def winner_of(partidas):
    player1 = 0
    player2 = 0
    combinaciones_ganadoras = (
        ["π","βοΈ"],
        ["π","πΏ"],
        ["βοΈ","π"],
        ["βοΈ","π¦"],
        ["π","π"],
        ["π","πΏ"],
        ["πΏ","π¦"],
        ["πΏ","βοΈ"],
        ["π¦","π"],
        ["π¦","π"]
    )
    for partida in partidas:
        if (partida[0] == partida[1]):
            player1 += 1
            player2 += 1
        elif partida in combinaciones_ganadoras:
            player1 += 1
        else:
            player2 += 1
    
    if player1 == player2:
        print('Tie')
    elif player1 < player2:
        print('Player 2')
    elif player1 > player2:
        print('Player 1')

#Ejercicio resuelto mediante Match case ya que la mayoria son con combinaciones de listas
def winner_of_match_case(partidas):
    player1 = 0
    player2 = 0

    for partida in partidas:
        match partida[0]:
            case "βοΈ":
                match partida[1]:
                    case "βοΈ":
                        player1 += 1
                        player2 += 1
                    case "π":
                        player1 += 1
                    case "π":
                        player2 += 1
                    case "πΏ":
                        player2 += 1
                    case "π¦":
                        player1 += 1
            case "π":
                match partida[1]:
                    case "βοΈ":
                        player2 += 1
                    case "π":
                        player1 += 1
                        player2 += 1
                    case "π":
                        player1 += 1
                    case "πΏ":
                        player1 += 1
                    case "π¦":
                        player2 += 1
            case "πΏ":
                match partida[1]:
                    case "βοΈ":
                        player1 += 1
                    case "π":
                        player2 += 1
                    case "π":
                        player2 += 1
                    case "πΏ":
                        player1 += 1
                        player2 += 1
                    case "π¦":
                        player1 += 1
            case "π¦":
                match partida[1]:
                    case "βοΈ":
                        player2 += 1
                    case "π":
                        player1 += 1
                    case "π":
                        player1 += 1
                    case "πΏ":
                        player2 += 1
                    case "π¦":
                        player1 += 1
                        player2 += 1
            case "π":
                match partida[1]:
                    case "βοΈ":
                        player1 += 1
                    case "π":
                        player2 += 1
                    case "π":
                        player1 += 1
                        player2 += 1
                    case "πΏ":
                        player1 += 1
                    case "π¦":
                        player2 += 1
        
    if player1 == player2:
        print('Tie')
    elif player1 < player2:
        print('Player 2')
    elif player1 > player2:
        print('Player 1')



print('\nPruebas mediante match case')
winner_of_match_case([["πΏ","βοΈ"], ["βοΈ","πΏ"], ["π","βοΈ"]])   # Player 2
winner_of_match_case([["πΏ","βοΈ"], ["π","βοΈ"]])               # Tie
winner_of_match_case([["πΏ","πΏ"], ["βοΈ", "π"]])             # Player 1
winner_of_match_case([["π¦","βοΈ"], ["π","πΏ"], ["π","βοΈ"]])  # Player 1


print('\nPruebas mediante combinaciones')
winner_of([["πΏ","βοΈ"], ["βοΈ","πΏ"], ["π","βοΈ"]])   # Player 2
winner_of([["πΏ","βοΈ"], ["π","βοΈ"]])               # Tie
winner_of([["πΏ","πΏ"], ["βοΈ", "π"]])             # Player 1
winner_of([["π¦","βοΈ"], ["π","πΏ"], ["π","βοΈ"]])  # Player 1