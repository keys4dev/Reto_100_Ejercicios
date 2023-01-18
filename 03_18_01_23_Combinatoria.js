/*
Usted es empresario en Madrid, y tiene la brillante idea de abrir una tienda de la leche en la Plaza Mayor. 
Como es una persona muy prudente, desea que la leche que venderá sea perfectamente natural y fresca, 
y por esa razón, va a traer unas sanísimas vacas de la región de Zaragoza a Madrid. 
Tiene a su disposición un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta.
Cada vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.

Su objetivo como empresario es elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de leche, observando el límite de peso del camión.

Entrada: Número total de vacas en la zona de Zaragoza que están a la venta.
Entrada: Peso total que el camión puede llevar.
Entrada: Lista de pesos de las vacas.
Entrada: Lista de la producción de leche por vaca, en litros por día.
Salida: Cantidad máxima de producción de leche se puede obtener.
(Asegúrate de que has leído las preguntas frecuentes antes de plantear tu solución)
*/

const TOTAL_COWS_ORIGIN = 100;
const MAX_WEIGHT_TRAILER = 3000; //kg
const COWS_WEIGHT_LIST = {
    1: 650,
    2: 720,
    3: 780,
    4: 680,
    5: 745,
    6: 700,
    7: 800,
    8: 710,
    9: 600
}
const MAX_COW_PRODUCTION = {    
    1: 28,
    2: 33,
    3: 50,
    4: 35,
    5: 55,
    6: 48,
    7: 60,
    8: 43,
    9: 30
}

function getCombinations (arrayList){
    let combination = [];
    let temp = [];
    //Calcular el numero de combinaciones posibles que es arraylist.length elevado a 2
    let numberOfCombinations =  Math.pow(2, arrayList.length);
    
    //Generar todas las combinaciones posibles
    for (let i = 0; i < numberOfCombinations; i++){
        temp = [];
        for (let j=0; j < arrayList.length; j++ ){
            if((i & Math.pow(2,j))){
                temp.push(arrayList[j]);
            }
        }
        if (temp.length > 0){
            combination.push(temp);
        }
    }
    combination.sort((a, b) => a.length - b.length);
    return combination;
}

//Funcion que retorna un array de arrays de las vacas con su peso y produccion
function createArrayOfCows(cows_weight_list, max_cow_production){
    array = [];
    keys = Object.keys(cows_weight_list);
    keys.forEach(key => {
        array.push([key, cows_weight_list[key], max_cow_production[key]]);
    });
    return array;
}

function fill_trailer(total_cows_origin, max_weight_trailer, cows_weight_list, max_cow_production){
    
    cows = createArrayOfCows(cows_weight_list, max_cow_production)
    
    //Sacamos la combinacion de todas la vacas
    let cowsCombinedByWeight = getCombinations(cows);
    //console.log(cowsCombinedByWeight);

    //Limpiamos Arrays mas pequeñas del peso maximo del camion y generamos un array de array con la com
    //combinacion de vacas  mas el peso sumado de la combinacion mas la produccion sumada.
    let possibleCowsCombined = () => {
        let array = []
        for (index in cowsCombinedByWeight){
            let combination = cowsCombinedByWeight[index];
            let sumWeight = 0;
            let sumProduction = 0;
            for (values in combination){
                sumWeight = sumWeight + combination[values[0]][1];
                sumProduction = sumProduction + combination[values[0]][2];
            } 
            if (sumWeight <= MAX_WEIGHT_TRAILER){
                array.push([combination, sumWeight, sumProduction])
            } 
        }
        return array;
    };

    array = possibleCowsCombined();
    
    //Buscamos dentro del array de las posibles combinaciones que cumplen con el peso mas pequeño
    //o igual que el del camión la que mas produccíon tenga
    let result = []
    let production = 0;
    array.forEach(element => {
        if (element[2] > production){
            result = element;
            production = element[2]
        } 
    });


    //Retornamos el resultado.
    console.log(`El lechero debe llevar las vacas ${result[0][0]}, con lo que llevarà un peso de ${result[1]} y generará una producción de ${result[2]} litros diarios`);
    return result;
}

fill_trailer(TOTAL_COWS_ORIGIN,MAX_WEIGHT_TRAILER, COWS_WEIGHT_LIST, MAX_COW_PRODUCTION);