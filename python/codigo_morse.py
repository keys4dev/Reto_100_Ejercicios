"""/*
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

alfabeto_morse = {
    'A':'·-',
    'B':'-···',
    'C':'-·-·',
    'D':'-··',
    'E':'·',
    'F':'··-·',
    'G':'--·',
    'H':'····',
    'I':'··',
    'J':'·---',
    'K':'-·-',
    'L':'·-··',
    'M':'--',
    'N':'-·',
    'O':'---',
    'P':'·--·',
    'Q':'--·-',
    'R':'·-·',
    'S':'···',
    'T':'-',
    'U':'··-',
    'V':'···-',
    'W':'·--',
    'X':'-··-',
    'Y':'-·--',
    'Z':'--··',
    '1':'.----',
    '2':'··---',
    '3':'···--',
    '4':'····-',
    '5':'·····',
    '6':'-····',
    '7':'--···',
    '8':'---··',
    '9':'----·',
    '0':'-----',
    ' ':'/'
}
def find_in_dict(letter):
    for key, value in alfabeto_morse.items():
        if value == letter:
            return key
            
def text_to_morse(text):
    array = list(text)
    morse = ""
    for i in array:
        morse = morse + alfabeto_morse[i]
        morse = morse + " "
    return morse

def morse_to_text(morse):
    array = list(morse)
    text = ""
    letter = ""
    for i in array:
        if (i!=' '):
            letter = letter + i
        else:
            find_in_dict(letter)
            text = text + find_in_dict(letter)
            letter = ""
    text = text + find_in_dict(letter)
    return text

print(text_to_morse("Jose Luis".upper()))
print(morse_to_text("·--- --- ··· · / ·-·· ··- ·· ···".upper()))


