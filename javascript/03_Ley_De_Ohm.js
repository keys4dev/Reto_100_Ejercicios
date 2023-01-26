/*
 * Reto #41
 * LA LEY DE OHM
 * Fecha publicación enunciado: 10/10/22
 * Fecha publicación resolución: 17/10/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
 *
 */

//V = R*I   

//I = V/R

//R = V/I

const resultadoLeyOhm = (v='opcional', r='opcional', i='opcional') =>{

    if (v=='opcional' && r != 'opcional' && i!='opcional'){
        return `V = ${parseInt(r)*parseInt(i)}`
    }
    else if (v!='opcional' && r == 'opcional' && i!='opcional'){
        return `R = ${parseInt(v)/parseInt(i)}`
    }
    else if (v!='opcional' && r != 'opcional' && i=='opcional'){
        return `I = ${parseInt(v)/parseInt(r)}`
    }else{
        return 'Invalid Values'
    }
}

console.log(resultadoLeyOhm(6,undefined,4))
console.log(resultadoLeyOhm(6,4,undefined))
console.log(resultadoLeyOhm(undefined,6,4))