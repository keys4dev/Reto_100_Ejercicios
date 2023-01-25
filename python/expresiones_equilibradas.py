"""/*
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""
def containskey(symbols, symbol):
    if symbol in symbols:
        return True
    elif symbol in symbols.values():
        return True
    else:
        return False
    
def containsvalue(symbols, symbol):
    if symbol in symbols.values():
        return True
    else:
        return False

def getLasValueDict(dictionary):
    for key, value in dictionary.items()[::-1]:
        ultimo_valor = value
        break
    return ultimo_valor

def es_equilibrada(expresion):
  pila = [] # Creamos una pila vacía
  for caracter in expresion:
    if caracter in "([{": # Si es una apertura, añadimos el carácter a la pila
      pila.append(caracter)
    elif caracter in ")]}": # Si es un cierre, eliminamos el último elemento de la pila
      if not pila:
        return False # Si la pila está vacía, entonces la expresión no es equilibrada
      if caracter == ")" and pila[-1] != "(":
        return False # Si el último elemento de la pila no es el carácter de apertura correspondiente, entonces la expresión no es equilibrada
      if caracter == "]" and pila[-1] != "[":
        return False
      if caracter == "}" and pila[-1] != "{":
        return False
      pila.pop() # Eliminamos el último elemento de la pila
  return not pila # Si la pila está vacía, entonces la expresión es equilibrada

# Probar la función con algunas expresiones
print(es_equilibrada("(1 + 2) * 3")) # True
print(es_equilibrada("))")) # False