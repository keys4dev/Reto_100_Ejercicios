"""/*
 * Reto #5
 * ASPECT RATIO DE UNA IMAGEN
 * Fecha publicación enunciado: 01/02/22
 * Fecha publicación resolución: 07/02/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""

from PIL import Image
import requests
from io import BytesIO

#URL DE LA IMAGEN
url = "https://images.pexels.com/photos/462118/pexels-photo-462118.jpeg"
response = requests.get(url)
im = Image.open(BytesIO(response.content))
width, height = im.size

print("width",width)
print("height",height)


def mcd(a, b):
  # Si alguno de los números es 0, el MCD es el otro número
  if a == 0:
    return b
  if b == 0:
    return a

  # Mientras el resto de la división de a y b no sea 0,
  # asignar a b el valor de a mod b y a b el valor de b
  while a % b != 0:
    a, b = b, a % b

  # El MCD es el último valor de b
  return b

# Ejemplo de uso: calcular el MCD de 24 y 16
mcd_ratio = mcd(width,height)
print("aspect ratio " + str(int(width/mcd_ratio)) + ":"+ str(int(height/mcd_ratio)))

