"""/*
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""


def isPrimo(number):
    primo = True
    for i in range(number):
        if i!=0:
            if(number%i==0)and(number/i<=i):
                primo = False
    if primo:
        print(number)
        return(True)
    else:
        return(False)

def lisOfPrimes(number):
    primos = []
    for i in range(number):
        if isPrimo(i):
            primos.append(i)
    print (len(primos))
    return primos

print(isPrimo(9594))
print(lisOfPrimes(10))