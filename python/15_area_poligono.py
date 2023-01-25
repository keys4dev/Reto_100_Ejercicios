"""
/*
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

class Cuadrado():
    def __init__(self, side) -> None:
        self.side = side
    def area(self):
        return self.side*self.side

class Rectangulo():
    def __init__(self, high, width) -> None:
        self.high = high
        self.width = width
    def area(self):
        return self.high*self.width

class Triangulo():
    def __init__(self, high, width) -> None:
        self.high = high
        self.width = width
    def area(self):
        return self.high*self.width/2

def area(poligono):
    if(poligono == "Triangulo"):
        print(triangulo.area())
    if(poligono == "Cuadrado"):
        print(cuadrado.area())
    if(poligono == "Rectangulo"):
        print(rectangulo.area())


cuadrado = Cuadrado(3)
triangulo = Rectangulo(2,3)
rectangulo = Triangulo(3,8)
area("Triangulo")
area("Cuadrado")
area("Rectangulo")
