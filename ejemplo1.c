#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definición de macros
#define PI 3.1416
#define SQUARE(x) ((x) * (x))

// Enumeración
typedef enum {
    RED,
    GREEN,
    BLUE
} Color;

// Estructura
typedef struct {
    int id;
    char name[50];
    float price;
} Product;

// Función principal
int main() {
    // Declaración de variables
    int a = 10, b = 20;
    float result = 0.0;
    char character = 'C';
    char str[] = "Hola, mundo!";
    
    // Operadores matemáticos
    result = (a + b) * PI / 2.0;
    
    // Estructuras de control
    if (result > 10) {
        printf("El resultado es mayor que 10\n");
    } else {
        printf("El resultado es menor o igual a 10\n");
    }

    // Bucle for
    for (int i = 0; i < 5; i++) {
        printf("Iteración %d\n", i);
    }

    // Bucle while
    while (a > 0) {
        a--;
    }

    // Switch case
    switch (character) {
        case 'A':
            printf("Es la letra A\n");
            break;
        case 'C':
            printf("Es la letra C\n");
            break;
        default:
            printf("Otra letra\n");
            break;
    }

    // Uso de punteros
    int *ptr = &b;
    *ptr = 30;

    // Uso de estructuras
    Product p1 = {1, "Laptop", 999.99};
    printf("Producto: %s, Precio: %.2f\n", p1.name, p1.price);

    // Archivo
    FILE *file = fopen("data.txt", "w");
    if (file) {
        fprintf(file, "Escribiendo en un archivo\n");
        fclose(file);
    }

    // Comentario de una línea
    /* Comentario de varias líneas
       Explicación del código */

    return 0;
}
