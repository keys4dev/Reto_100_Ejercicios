"""/***
 * Reto #50
 * LA ENCRIPTACIÓN DE KARACA
 * Fecha publicación enunciado: 12/12/22
 * Fecha publicación resolución: 19/12/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que sea capaz de encriptar y desencriptar texto utilizando el
 * algoritmo de encriptación de Karaca (debes buscar información sobre él).
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
***/

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

// "1lpp0"""

def encrypt(text:str):
    crypted = ""
    for index in text:
        match index:
            case "a":
                index = '0'
            case "e":
                index = '1'
            case "i":
                index = '2'
            case "o":
                index = '3'
            case "u":
                index = '4'
        crypted = index + crypted
    crypted = crypted + "aca"
    print(crypted)

def decrypt(crypted:str):
    text = ""
    crypted = crypted[:-3]
    for index in crypted:
        match index:
            case "0":
                index = 'a'
            case "1":
                index = 'e'
            case "2":
                index = 'i'
            case "3":
                index = 'o'
            case "4":
                index = 'u'
        text = index + text
    print(text)

encrypt("Jose Luis Sanchez Lopez")
decrypt("z1p3L z1hcn0S s24L 1s3Jaca")