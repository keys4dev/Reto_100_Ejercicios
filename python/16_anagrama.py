"""/*
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */

 """

def isAnagrama(text1, text2):
    if text1 == text2:
        print("Is not Anagrama")
        return False
    else:
        array1 = list(text1)
        array2 = list(text2)
        array1.sort()
        array2.sort()
        result1 = ''.join([str(elem) for elem in array1])
        result2 = ''.join([str(elem) for elem in array2])
        if (result1 == result2):
            print("Is Anagrama")
            return True
        else:
            print("Is not Anagrama")
            return False

isAnagrama("amor", "roma")