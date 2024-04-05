# Ejercicio del Bootcamp de Ciencias de la Computación - Interprete

## fiso language
Es un pequeño lenguaje de consola que permite evaluar operaciones aritméticas básicas: __+, -, *, /__

Soporta el uso de __parentésis__ y de __variables__

## Uso
Requerimos de un archivo de texto que contenga el código a evaluar como el del siguiente ejemplo:

**Programa de ejemplo (archivo code.txt)**
```js
a = 2 + ( 12 / 4 )
b = a * a - 10
c = ( b - 5 ) * 2.5
d = ( c * 4 / 5 ) + ( 10 - 20 )
```

Puedes modificar las líneas de código y agrupar expresiones entre parentésis.
__Si usas parentésis deja un espacio después de abrirlos y antes de cerrarlos.__

Para ejecutar el código desde la consola usa el siguiente comando:
```sh
py program.py code.txt
```

La salida será la siguiente:
```sh
['a', '=', ['2', '+', ['12', '/', '4']]]
['b', '=', [[['2', '+', ['12', '/', '4']], '*', ['2', '+', ['12', '/', '4']]], '-', '10']]
['c', '=', [[[[['2', '+', ['12', '/', '4']], '*', ['2', '+', ['12', '/', '4']]], '-', '10'], '-', '5'], '*', '2.5']]
['d', '=', [[[[[[[['2', '+', ['12', '/', '4']], '*', ['2', '+', ['12', '/', '4']]], '-', '10'], '-', '5'], '*', '2.5'], '*', '4'], '/', '5'], '+', ['10', '-', '20']]]
a = 5.0
b = 15.0
c = 25.0
d = 10.0
```

Las primeras líneas son el **Abstract Sintax Tree AST** y las demás son la interpretación de dicho AST.

## Funcionamiento

### LEXER
Toma un archivo de texto plano y genera los **tokens** que pueden ser de los siguientes tipos:
- **INT**:      123, 78, 8, 9
- **FLOAT**:    4.5, 89.23
- **VAR**:      'mi_var', 'a', 'x_1'
- **OP**:       +, -, *, /, ()
- **ASSIGN**:   =

Cada token tiene una representación así: <type, value, line, column>

La línea de código **a = 2 + ( 12 / 4 )** generará los siguientes tokens:

```sh
[
    <VAR, a, 0, 0>, 
    <ASSIGN, =, 0, 2>, 
    <INT, 2, 0, 4>, 
    <OP, +, 0, 6>, 
    <OP, (, 0, 8>, 
    <INT, 12, 0, 10>, 
    <OP, /, 0, 13>, 
    <INT, 4, 0, 15>, 
    <OP, ), 0, 17>
]
```
### PARSER
El parser es el encargado de generar a partir de los tokens el **Abstract Sintax Tree AST** que indicará el orden en que se realizarán las operaciones.

```sh
['a', '=', ['2', '+', ['12', '/', '4']]]
['b', '=', [[['2', '+', ['12', '/', '4']], '*', ['2', '+', ['12', '/', '4']]], '-', '10']]
['c', '=', [[[[['2', '+', ['12', '/', '4']], '*', ['2', '+', ['12', '/', '4']]], '-', '10'], '-', '5'], '*', '2.5']]
['d', '=', [[[[[[[['2', '+', ['12', '/', '4']], '*', ['2', '+', ['12', '/', '4']]], '-', '10'], '-', '5'], '*', '2.5'], '*', '4'], '/', '5'], '+', ['10', '-', '20']]]
```

Cada lista representa una línea de código y por lo tanto un ast.

__Ejemplo de un ast__

Está línea de código __c = ( b - 5 ) * 2__ generará el siguiente ast:

```
        =
       / \
      c   *
         / \
       -    2
      / \
     b   5
```

### INTERPRETE
Es el responsable de evaluar el ast, en nuestro caso cada línea de código se corresponde con un ast, así que el interprete evaluará uno por uno.

El siguiente código:

```sh
a = 2 + ( 12 / 4 )
b = a * a - 10
c = ( b - 5 ) * 2.5
d = ( c * 4 / 5 ) + ( 10 - 20 )
```

Al ser evaluado generará la siguiente salida:

```sh
a = 5.0
b = 15.0
c = 25.0
d = 10.0
```
