#include <iostream>
using namespace std;

int main() {
    const int INTENTOS_MAX = 5;
    char palabra_secreta[] = "programar"; // La palabra se maneja como un array de caracteres
    char letras_adivinadas[20];           // Array para almacenar las letras adivinadas
    int intentos = 0;
    bool palabra_completada = false;

    // Contar manualmente el número de caracteres de la palabra secreta
    int longitud_palabra = 0;
    while (palabra_secreta[longitud_palabra] != '\0') {
        longitud_palabra++;
    }

    // Inicializamos el array de letras adivinadas con guiones bajos '_'
    for (int i = 0; i < longitud_palabra; i++) {
        letras_adivinadas[i] = '_';
    }

    // Iniciamos el juego
    cout << "¡Bienvenido al juego del Ahorcado!" << endl;
    cout << "Tienes " << INTENTOS_MAX << " intentos para adivinar la palabra." << endl;

    // Bucle del juego
    while (intentos < INTENTOS_MAX && !palabra_completada) {
        char letra;
        bool acierto = false;

        // Mostramos el progreso de la palabra
        cout << "\nPalabra: ";
        for (int i = 0; i < longitud_palabra; i++) {
            cout << letras_adivinadas[i] << " ";
        }
        cout << endl;

        // Pedimos una letra al jugador
        cout << "Introduce una letra: ";
        cin >> letra;

        // Comprobamos si la letra está en la palabra secreta
        for (int i = 0; i < longitud_palabra; i++) {
            if (palabra_secreta[i] == letra) {
                letras_adivinadas[i] = letra;  // Reemplazamos el guion bajo por la letra adivinada
                acierto = true;
            }
        }

        // Si la letra no está en la palabra, aumentamos los intentos fallidos
        if (!acierto) {
            intentos++;
            cout << "¡Letra incorrecta! Te quedan " << (INTENTOS_MAX - intentos) << " intentos." << endl;
        }

        // Comprobamos si el jugador ha completado la palabra
        palabra_completada = true;
        for (int i = 0; i < longitud_palabra; i++) {
            if (letras_adivinadas[i] == '_') {
                palabra_completada = false;
                break;
            }
        }
    }

    // Resultado del juego
    if (palabra_completada) {
        cout << "\n¡Felicidades! Has adivinado la palabra: " << palabra_secreta << endl;
    } else {
        cout << "\n¡Has perdido! La palabra correcta era: " << palabra_secreta << endl;
    }

    return 0;
}
