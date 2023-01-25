//Funcion recursiva que muestra por consola los numeros de 5 a 0

function fiveToZero(number){
if (number < 0){
    return
}else{
    console.log(number);
    fiveToZero(number-1);
}
    
};

fiveToZero(5);