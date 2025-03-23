# lexer.py - Analizador léxico para C usando PLY
import ply.lex as lex
import os
import sys

# Tokens agrupados por familias
# 1. Directivas de preprocesador
tokens_preprocessor = (
    'INCLUDE', 'DEFINE', 'IFDEF', 'IFNDEF', 'ENDIF', 'PRAGMA',
)

# 2. Palabras reservadas
tokens_keywords = (
    'AUTO', 'BREAK', 'CASE', 'CHAR', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE',
    'ELSE', 'ENUM', 'EXTERN', 'FLOAT', 'FOR', 'GOTO', 'IF', 'INT', 'LONG',
    'REGISTER', 'RETURN', 'SHORT', 'SIGNED', 'SIZEOF', 'STATIC', 'STRUCT',
    'SWITCH', 'TYPEDEF', 'UNION', 'UNSIGNED', 'VOID', 'VOLATILE', 'WHILE',
)

# 3. Operadores matemáticos
tokens_math_operators = (
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
)

# 4. Operadores bit a bit
tokens_bitwise_operators = (
    'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
)

# 5. Operadores lógicos
tokens_logical_operators = (
    'LOR', 'LAND', 'LNOT',
)

# 6. Operadores relacionales
tokens_relational_operators = (
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
)

# 7. Operadores de asignación
tokens_assignment_operators = (
    'EQUALS', 'PLUSEQUAL', 'MINUSEQUAL', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL',
    'LSHIFTEQUAL', 'RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',
)

# 8. Operadores de incremento/decremento
tokens_inc_dec_operators = (
    'PLUSPLUS', 'MINUSMINUS',
)

# 9. Delimitadores
tokens_delimiters = (
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON', 'ELLIPSIS',
)

# 10. Literales
tokens_literals = (
    'ID', 'ICONST', 'FCONST', 'SCONST', 'CCONST',
)

# 11. Otros
tokens_others = (
    'ARROW', 'CONDOP',
)

# Unir todas las familias de tokens en una sola tupla
tokens = (
    tokens_preprocessor +
    tokens_keywords +
    tokens_math_operators +
    tokens_bitwise_operators +
    tokens_logical_operators +
    tokens_relational_operators +
    tokens_assignment_operators +
    tokens_inc_dec_operators +
    tokens_delimiters +
    tokens_literals +
    tokens_others
)

# Diccionario de palabras reservadas
reserved = {
    'auto': 'AUTO',
    'break': 'BREAK',
    'case': 'CASE',
    'char': 'CHAR',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'default': 'DEFAULT',
    'do': 'DO',
    'double': 'DOUBLE',
    'else': 'ELSE',
    'enum': 'ENUM',
    'extern': 'EXTERN',
    'float': 'FLOAT',
    'for': 'FOR',
    'goto': 'GOTO',
    'if': 'IF',
    'int': 'INT',
    'long': 'LONG',
    'register': 'REGISTER',
    'return': 'RETURN',
    'short': 'SHORT',
    'signed': 'SIGNED',
    'sizeof': 'SIZEOF',
    'static': 'STATIC',
    'struct': 'STRUCT',
    'switch': 'SWITCH',
    'typedef': 'TYPEDEF',
    'union': 'UNION',
    'unsigned': 'UNSIGNED',
    'void': 'VOID',
    'volatile': 'VOLATILE',
    'while': 'WHILE',
}

# Reglas para directivas de preprocesador
def t_INCLUDE(t):
    r'\#include'
    return t

def t_DEFINE(t):
    r'\#define'
    return t

def t_IFDEF(t):
    r'\#ifdef'
    return t

def t_IFNDEF(t):
    r'\#ifndef'
    return t

def t_ENDIF(t):
    r'\#endif'
    return t

def t_PRAGMA(t):
    r'\#pragma'
    return t

# Reglas léxicas para tokens simples

# Operadores matemáticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'

# Operadores bit a bit
t_OR = r'\|'
t_AND = r'&'
t_NOT = r'~'
t_XOR = r'\^'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'

# Operadores lógicos
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LNOT = r'!'

# Operadores relacionales
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

# Operadores de asignación
t_EQUALS = r'='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVEQUAL = r'/='
t_MODEQUAL = r'%='
t_LSHIFTEQUAL = r'<<='
t_RSHIFTEQUAL = r'>>='
t_ANDEQUAL = r'&='
t_XOREQUAL = r'\^='
t_OREQUAL = r'\|='

# Incremento/decremento
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'

# Delimitadores
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'
t_COLON = r':'
t_ELLIPSIS = r'\.\.\.'
t_ARROW = r'->'
t_CONDOP = r'\?'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Ignorar comentarios
def t_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    t.lexer.lineno += t.value.count('\n')
    pass

# Reconocer nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Literales
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FCONST(t):
    r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
    return t

def t_ICONST(t):
    r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
    return t

def t_CCONST(t):
    r'\'([^\\\n]|(\\.))*?\''
    return t

def t_SCONST(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Manejo de errores
def t_error(t):
    print(f"Error léxico: Carácter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)

# Implementación del doble buffer
class LexerBuffer:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.buffer_size = 1024
        self.buffer_1 = ''
        self.buffer_2 = ''
        self.current_buffer = 1
        self.pos = 0
        
    def open(self):
        try:
            self.file = open(self.filename, 'r')
            self.fill_buffer()
            return True
        except FileNotFoundError:
            print(f"Error: No se pudo abrir el archivo '{self.filename}'")
            return False
    
    def fill_buffer(self):
        if self.current_buffer == 1:
            self.buffer_1 = self.file.read(self.buffer_size)
            self.current_buffer = 2
            self.pos = 0
        else:
            self.buffer_2 = self.file.read(self.buffer_size)
            self.current_buffer = 1
            self.pos = 0
    
    def get_char(self):
        if self.current_buffer == 1:
            if self.pos >= len(self.buffer_1):
                self.fill_buffer()
                if not self.buffer_2:
                    return ''
                return self.buffer_2[self.pos]
            else:
                char = self.buffer_1[self.pos]
                self.pos += 1
                return char
        else:
            if self.pos >= len(self.buffer_2):
                self.fill_buffer()
                if not self.buffer_1:
                    return ''
                return self.buffer_1[self.pos]
            else:
                char = self.buffer_2[self.pos]
                self.pos += 1
                return char
    
    def close(self):
        if self.file:
            self.file.close()

# Función para leer un archivo y analizarlo
def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            
        lexer = lex.lex()
        lexer.input(data)
        
        # Generar tabla de tokens
        token_table = []
        for tok in lexer:
            token_table.append({
                'type': tok.type,
                'value': tok.value,
                'line': tok.lineno,
                'position': tok.lexpos,
                'family': get_token_family(tok.type)
            })
        
        return token_table
    except FileNotFoundError:
        print(f"Error: No se pudo abrir el archivo '{filename}'")
        return None

# Función para determinar la familia de un token
def get_token_family(token_type):
    if token_type in tokens_preprocessor:
        return "Directiva de Preprocesador"
    elif token_type in tokens_keywords:
        return "Palabra Reservada"
    elif token_type in tokens_math_operators:
        return "Operador Matemático"
    elif token_type in tokens_bitwise_operators:
        return "Operador Bit a Bit"
    elif token_type in tokens_logical_operators:
        return "Operador Lógico"
    elif token_type in tokens_relational_operators:
        return "Operador Relacional"
    elif token_type in tokens_assignment_operators:
        return "Operador de Asignación"
    elif token_type in tokens_inc_dec_operators:
        return "Operador Incremento/Decremento"
    elif token_type in tokens_delimiters:
        return "Delimitador"
    elif token_type in tokens_literals:
        return "Literal"
    else:
        return "Otro"

# Función principal
def main():
    if len(sys.argv) != 2:
        print("Uso: python lexer.py <archivo.c>")
        return
    
    filename = sys.argv[1]
    tokens = analyze_file(filename)
    
    if tokens:
        print("\nTabla de Tokens:")
        print("-" * 100)
        print(f"{'Token':<5}{'Tipo':<20}{'Familia':<25}{'Valor':<20}{'Línea':<10}{'Posición'}")
        print("-" * 100)
        
        for i, token in enumerate(tokens):
            print(f"{i+1:<5}{token['type']:<20}{token['family']:<25}{str(token['value']):<20}{token['line']:<10}{token['position']}")


if __name__ == "__main__":
    main()