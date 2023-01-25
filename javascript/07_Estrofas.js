/*
Historial ayer borrado,
anteayer hubo pecado.
El texto anterior es un pareado: una estrofa con dos versos que riman entre sí con rima consonante. ¿Sabrías hacer un programa que identifique distintos tipos de estrofa?

En concreto, nos bastará con identificar las rimas (no tendremos en cuenta el número de sílabas de cada verso), existiendo dos rimas distintas:

Rima consonante: se dice que entre dos versos hay rima consonante cuando todos los sonidos, tanto vocales como consonantes, riman. 
Para las comparaciones se tienen en cuenta todos los sonidos a partir de la última vocal acentuada.
Rima asonante: similar a la anterior pero únicamente riman las vocales.
Por ejemplo, el siguiente cuarteto de Diego de Silva y Mendoza:

Una, dos, tres estrellas, veinte, ciento,	(A)
mil, un millón, millares de millares,	(B)
¡válgame Dios, que tienen mis pesares	(B)
su retrato en el alto firmamento!	(A)
tiene esquema ABBA consonante, pues coinciden las vocales y consontantes del primer y último verso, así como las del segundo y tercero.

Nos piden ser capaces de identificar los siguientes tipos de estrofa:

De dos versos:
Pareado: rima consonante AA.
De tres versos:
Terceto: rima consonante en el primer y último verso (A-A). Ten en cuenta que AAA no se considerará terceto.
De cuatro versos:
Cuarteto: rima consonante ABBA.
Cuarteta: rima consonante ABAB.
Seguidilla: rima asonante en los pares (-a-a). Ten en cuenta que otras combinaciones con más rimas o con rima consonante en lugar de asonante (por ejemplo -aaa o -A-A) no se consideran seguidillas.
Cuaderna via: rima consonante igual en todos los versos (AAAA).
Entrada

La entrada estará formada por un número indeterminado de casos de prueba. Cada caso de prueba comienza con una línea que contiene un único entero con el número de versos del siguiente poema. 
A continuación aparecen tantas líneas como versos contiene la estrofa a analizar. Podemos asumir que la última palabra de cada verso es llana (la vocal acentuada está en la penúltima sílaba), 
y que ninguno tendrá más de 70 letras. La entrada no contendrá tildes para facilitar la programación, aunque esto signifique cometer errores ortográficos. Tampoco tendremos en cuenta que distintos
elementos gráficos pueden tener el mismo sonido. Es decir, un verso terminado en -aba, no rimará de forma consonante con un verso terminado en -ava.

La entrada termina cuando el siguiente caso de prueba contiene 0 versos. Para ese caso de prueba no se generará ninguna salida.

Salida

Para cada caso de prueba el programa indicará el nombre de la estrofa, utilizando mayúsculas (PAREADO, TERCETO, CUARTETO, CUARTETA, SEGUIDILLA, CUADERNA VIA) o la palabra DESCONOCIDO si no conoce la estrofa dada.

Notas

El enunciado ha hecho simplificaciones en las definiciones de las estrofas encaminadas a hacer el ejercicio más sencillo; ejemplos de esto son no considerar el número de sílabas, manejar sólo palabras llanas, 
tener faltas de ortografía, etc. El resultado ha sido unas definiciones que poco tienen que ver con las aceptadas en la literatura. Por favor, no utilices el programa final delante de un experto en poesía.

(Asegúrate de que has leído las preguntas frecuentes antes de plantear tu solución)
*/
const regex = /[.,;]/g;
const vocalsRegex = /[^aeiou]/g;

const entrada = function(){/*
    2
    Historial ayer borrado
    anteayer hubo pecado
    2
    Esto no pega
    ni con cola.
    4
    La pila de agua bendita
    que está en el rincón umbrío,
    es silvestre margarita
    llena de fresco rocío.
    3
    Un manotazo duro, un golpe helado,
    un hachazo invisible y homicida,
    un empujon brutal te ha derribado.
    0
    */
}.toString().slice(14,-4).replace(regex, '')

//Meto en un array por cada numero encontrado otra array par tener una array por estrofa. Asi obtengo un array con las estrofas separadas por arrays con sus terminaciones.
/*
Ejemplo:  Al terminar el array.forEach en terminaciones tendriamos esto:
[
  [ 'ado', 'ado' ], --> Estrofa 1
  [ 'ega', 'ola' ], --> Estrofa 2
  [ 'ita', 'río', 'ita', 'cío' ], --> Estrofa 3
  [ 'ado', 'ida', 'ado' ] --> Estrofa 4
]
*/
let arrayEntrada = entrada.split("\n");;
let buffer = []
let terminaciones = []
arrayEntrada.forEach(element => {
    if (isNaN(element)){
        buffer.push(element.slice(-3))
    }
    if ((element > 0 && buffer.length > 0) || (element == 0 && buffer.length > 0)){
        terminaciones.push(buffer)
        buffer = []
    }
});
terminaciones.forEach(element => {
    /*
    Ahora dependiendo de las lineas que tengamos en la estrofa saltaremos a un case u otro
    Si cumple con las normas de cada tipo de estrofa se retornara su tipo.
    Sino se encuentra se retorna que No es una rima
    */
    switch (element.length) {
        case 2:
            if (element[0]==element[1]){
                console.log("Es un Pareado Consonante");
                break; 
            }
            if (element[0].replace(vocalsRegex,'').slice(-2) == element[1].replace(vocalsRegex,'').slice(-2)){
                console.log("Es un Pareado Asonante");    
            }else{
                console.log("Este pareado no Rima");
            } 
            break;
        case 3:
            if (element[0]==element[2]){
                console.log("Es un Terceto");    
            }
            break;
        case 4:
       /* Cuaderna via: rima consonante igual en todos los versos (AAAA).*/
            if ((element[0]==element[3]) && (element[1]==element[2])){
                console.log("Es un Cuarteto");    
            }
            if ((element[0].slice(-2)==element[2].slice(-2)) && (element[1].slice(-2)==element[3].slice(-2))){
                console.log("Es una Cuarteta");    
            }
            if ((element[0].replace(vocalsRegex,'').slice(-2)!=element[1].replace(vocalsRegex,'').slice(-2)) && (element[1]!=element[3]) && ((element[1].replace(vocalsRegex,'').slice(-2)==element[3].replace(vocalsRegex,'').slice(-2))) ){
                console.log("Es una Seguidilla");    
            }
            if (element[0]==element[1] && element[0]==element[2] && element[0]==element[3]){
                console.log("Es una Cuaderna Via Rima Consonante");    
            }
            break;
        default:
            console.log("No es una rima");
            break;
    }
});