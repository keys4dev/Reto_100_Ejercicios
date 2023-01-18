/*
En este reto partimos de un conjunto de enteros positivos (le llamaremos lista) y un entero (le llamaremos suma). Se trata de encontar esi existe algún subconjunto de lista suyos componentes sumen el valor de suma

La idea es resolverlo mediante una función recursiva. Echa un vistazo a la solución dinámica si necesitas orientarte.

Ejemplos de la función:

existeSuma([3,4,2,8,7], 6)   -> true   

existeSuma([3,4,2,8,7], 26)   -> false   

existeSuma([4],  4)   -> true   

*/

lista = [4];
suma = 4;

function existeSuma(lista, suma){
    buffer = 0;
    for (let i = 0; i < lista.length; i++) {
        const numero1 = lista[i];
        if (numero1==suma){
            return true
        }else if(numero1<suma){
            buffer = numero1;
            for (let j = i+1; j < lista.length; j++) {
                const numero2 = lista[j];
                if(buffer+numero2==suma) {
                    return true
                }else if(buffer+numero2<suma){
                    buffer = buffer+numero2
                }
            }    
        } 
    }
    return false
}
console.log(existeSuma(lista, suma));