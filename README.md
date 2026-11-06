# Sistema de multas de biblioteca

Autor: Ángel Miguel Valdez
Grupo: 3ro E
Escuela: CECyTES Sonora, Plantel La Manga

## Descripción
Programa escolar en Python que calcula multas por entrega tardía de libros.

## Regla de cálculo
Cada día de retraso genera una multa de $2 por libro.

Multa = días de retraso × cantidad de libros × 2

## Funcionamiento
El programa solicita días y libros como números enteros.
Acepta valores de cero o más y rechaza números negativos o texto.

## Ejemplo
Con 3 días de retraso y 2 libros, la multa es de $12.00.

## Cómo ejecutarlo
Guardar multas.py y pruebas.py en la misma carpeta.
Con Python 3 instalado, ejecutar: python multas.py

## Pruebas
Ejecutar: python pruebas.py

Se comprueban siete casos: sin retraso, retraso normal, un libro,
días negativos, texto, cero libros y libros negativos.

El resultado esperado es: 7 de 7 pruebas correctas.

## Alcance
El programa calcula importes. No registra préstamos ni pagos.
