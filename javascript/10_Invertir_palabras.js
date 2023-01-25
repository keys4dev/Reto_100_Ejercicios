/*
Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso. 
Cada palabra estará formada exclusivamente por letras, y existirá exactamente un espacio entre cada pareja de palabras. 
La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", de un espacio en blanco y de la frase invertida.

(Asegúrate de que has leído las preguntas frecuentes antes de plantear tu solución)
El primer dato de entrada será la cantidad de valores que se van a analizar.

Ejemplo de entrada

3
this is a test
foobar
all your base

Salida correspondiente

Case #1: test a is this
Case #2: foobar
Case #3: base your all
*/

const input = 'base your all'

const arraywords = input.split(" ")
let output = []
while (arraywords.length > 0) {
    output.push(arraywords.pop())
}

console.log(output.toString().replaceAll(","," "));