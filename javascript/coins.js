//Given an amount of money and an array of coins
//write a method that computes the number of ways to make the 
//amount of money with coins of the available coins.

//Example 1

//getCoins(4, listOf(1, 2, 3)) // 4

//Ways to make 4 with those denominations :
//1¢, 1¢, 1¢, 1¢
//1¢, 1¢, 2¢
//1¢, 3¢
//2¢, 2¢

// Cantidad a pagar
const amount = 4;

// Monedas disponibles
const coins = [1, 2, 3];

// Array donde se almacenarán las combinaciones de monedas
const result = [];

// Función recursiva que encuentra todas las combinaciones de monedas que suman "remaining"
function findCombinations(remaining, current) {
  // Si no queda más dinero por pagar, añadimos la combinación actual al array de resultados
  if (remaining === 0) {
    result.push(current);
    return;
  }
  // Si el dinero por pagar es menor que cero, terminamos la recursión
  if (remaining < 0) {
    return;
  }
  // Probar cada moneda disponible
  for (const coin of coins) {
    // Llamar recursivamente a la función con el dinero restante y la combinación actual con la moneda añadida
    findCombinations(remaining - coin, current.concat(coin));
  }
}

// Iniciar la búsqueda con el total a pagar y una combinación vacía
findCombinations(amount, []);

// Imprimir el array de resultados
console.log(result);  // imprime [[1, 1, 2]]