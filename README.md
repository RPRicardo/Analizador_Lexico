# Analizador Léxico para C en Python

##  Descripción del Proyecto

Este proyecto implementa un analizador léxico completo para el lenguaje de programación C, desarrollado en Python utilizando la biblioteca PLY (Python Lex-Yacc). El analizador es capaz de descomponer código fuente en C en tokens, clasificándolos y proporcionando un análisis detallado de su estructura léxica.

## Características Principales

- Análisis léxico completo de archivos en C
- Clasificación de tokens en 11 categorías funcionales
- Implementación de técnica de doble buffer para procesamiento eficiente
- Manejo de errores léxicos

## Requisitos Previos

- Python 3.7+
- Biblioteca PLY (`pip install ply`)

## 🚀 Instalación

1. Clonar el repositorio:
git clone https://github.com/RPRicardo/Analizador_Lexico
cd analizador-lexico-c

2. Instalar dependencias:
pip install ply

## Uso

Ejecutar el analizador léxico:
python3 Analizador_Lexico_v1_3.py <archivo.c>

##  Categorías de Tokens

1. Directivas de preprocesador
2. Palabras reservadas
3. Operadores matemáticos
4. Operadores bit a bit
5. Operadores lógicos
6. Operadores relacionales
7. Operadores de asignación
8. Operadores de incremento/decremento
9. Delimitadores
10. Literales
11. Otros operadores especiales

## Reconocimientos

- [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/)
- Inspirado en técnicas de compiladores clásicos
