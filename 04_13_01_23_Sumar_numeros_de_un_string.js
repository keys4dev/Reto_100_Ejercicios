/*Crea un programa capaz de calcular la suma de los números 
que se indicarán en la entrada estándar, separados por espacios, 
y mostrar los resultados en pantalla. Los números pueden ser negativos, 
grandes y las líneas pueden contener espacios adicionales, por lo que el 
programa debe ser robusto.

(Cuidado: no debe ser "amigable", sino estricto: no debe decir nada como 
"introduce los datos" ni responder con nada como "la suma es..."; debe tomar 
cada línea de datos de la entrada estándar, analizarla y mostrar los resultados en 
la salida estándar).*/
let entrada = "-3 4 5   6  9  -8"

//Se divide a partir de " " -> se filtra y convierten a numeros -> se suman mediante reduce.
const result = entrada.split(" ").map(Number).reduce((a,b) => a+b);
//array.reduce((a,b) => a+b);
console.log(result)