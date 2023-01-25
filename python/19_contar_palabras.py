"""/*
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

def update_dict(dccionario_in, word):
    if word in dccionario_in:
        word
        reps = dccionario_in[word]
        dccionario_in[word]=reps+1
    else:
        word
        dccionario_in[word]=1

def how_many_repeats(text):
    diccionario = {}
    array = list(text)
    word = ''
    for i in array:
        if (i.isalpha()):
            word = word+i.lower()
        if not(i.isalpha()):
            update_dict(diccionario, word)
            word = ''
    update_dict(diccionario, word)
    return diccionario


print(how_many_repeats("Hola me Y llamo OOO me jose, luis HOLA gusta y Me gusta ME llamarme HOLA Jose Luis"))