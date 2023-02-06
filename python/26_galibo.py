"""Se conoce como el gálibo a la dimensión máxima que debe tener un vehículo para poder pasar por una zona de la vía de tamaño reducido como un túnel o un puente. 
Existen distintos tipos de gálibo y de formas de calcularlo que dependen del tipo de vehículo. Por ejemplo en los barcos el gálibo de un puente se mide teniendo en cuenta el nivel de la crecida más grande conocida. 
En trenes, el gálibo debe considerar no solo el alto sino también los anchos a distintas alturas.

En carretera el gálibo del que hay que preocuparse normalmente suele ser el vertical. 
En este caso la altura libre por debajo del puente debe tener en cuenta la altura máxima de los vehículos y un margen de seguridad relacionado con la amortiguación y cómo esta absorbe los movimientos verticales, 
así como cierta tolerancia por posibles imprecisiones a la hora de construir la estructura y por futuras operaciones de reasfaltado de la vía. Se puede incluso considerar, 
además, un margen de confort para que los conductores de los vehículos pesados se sientan cómodos (que dependerá de cómo se aproxime la vía al puente).

Para evitar problemas de gálibo para los vehículos más grandes, 
en algunas carreteras se colocan puentes de calibración que permiten a los conductores averiguar con tiempo suficiente si un puente próximo no tiene la altura mínima necesaria.

En ausencia de estos puentes de calibración, se puede confiar en la información que aparece en el propio puente. 
En algunos países hay pequeños carteles en el frontal del puente justo debajo de cada uno de los carriles para que los conductores puedan conocer su altura en cada uno de ellos.
Gracias a estos carteles si se quiere viajar seguro se puede hacer un primer trayecto en un vehículo más pequeño registrando esas alturas para conocer si el vehículo grande podrá pasar por debajo de todos ellos.

ENTRADA::

La entrada está compuesta de un número indeterminado de casos de prueba.

Cada caso de prueba comienza con una línea con un único número indicando el número de puentes (hasta 100) que hay en el trayecto que se desea hacer. 
Tras eso vendrá una línea por cada puente con su descripción. 
Esta comienza con el número de carriles que pasan por debajo del puente en el sentido de nuestro trayecto (como mucho 5) seguido de la altura del puente en cada uno de ellos en centímetros (un número entre 1 y 800).

Tras el último caso de prueba viene una línea con un 0 que no debe procesarse.


Por cada caso de prueba se escribirá la altura máxima que puede tener el camión para poder realizar el trayecto, teniendo en cuenta que este puede utilizar cualquiera de los carriles disponibles.

Ejemplo entrada:
2
3 300 300 250
2 325 300
2
1 450
1 400
0

Ejemplo salida:
300
400

"""

casos = []
caso = []
lineaEntrada = input()
#Hago una lista de casos por linea
while (lineaEntrada!='0'):
    for iterator in range(int(lineaEntrada)):
        lineaEntrada = input()
        splitLineEntrada = lineaEntrada.split(' ')
        numberOfWays = splitLineEntrada.pop(0)
        if int(numberOfWays) != len(splitLineEntrada):
            raise RuntimeError('You indicated ' + numberOfWays +' ways, but registered '+str(len(splitLineEntrada)))
        caso.append(splitLineEntrada)
    lineaEntrada = input()
    casos.append(caso)
    caso = []
# Miro por lista de lista cual es el carril de cada puente mas alto y me quedo con el mas alto, luego miro el mas bajo de los mas altos y me quedo con el
for entries in casos:
    entriesMaxHigh = None
    for entry in entries:
        intEntry = ''.join(entry)
        #Convierto primero los valores de la lista de str a int
        entry = list(map(int, entry))
        entryMaxHigh = 0
        for value in entry:
            intValue = int(value)
            if intValue > entryMaxHigh:
                entryMaxHigh = value
        if entriesMaxHigh == None or entryMaxHigh < entriesMaxHigh:
            entriesMaxHigh = entryMaxHigh
    print (entriesMaxHigh)