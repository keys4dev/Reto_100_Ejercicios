// Escribe un programa que pida al usuario ingrese su animal favorito, 
// si coloca ‘Tortuga’, ‘tortuga’, ‘TORTUGA’ o 
// cualquier otra variante de la palabra entonces mostrar en pantalla 
// “También me gustan las tortugas”. En caso contrario mostrar el 
// mensaje “Ese animal es genial, pero prefiero las tortugas”.

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.question('¿Cual es tu animal favorito?', function(animal){
    if (animal.toLowerCase() == 'tortuga'){
        console.log("También me gustan las tortugas");

    }else{
        console.log("Ese animal es genial, pero prefiero las tortugas");
    }
    rl.close();
});