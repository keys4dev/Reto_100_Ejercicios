import SwiftUI
import PlaygroundSupport
/*
 * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

 collar
 mojar
 
 salida
 cll
 mj
 
 */

func eliminaCaracteres(str1:String, str2:String)->(out1:String, out2:String){
    var out1 = String()
    var out2 = String()
    for char in str1{
        if !str2.contains(char){
            out1.append(char)
        }
        
    }
    for char in str2{
        if !str1.contains(char){
            out2.append(char)
        }
    }
    print(out1)
    print(out2)
    return (out1, out2)
}


eliminaCaracteres(str1: "collar", str2: "mojar")
