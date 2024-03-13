ˆ Coincide con el comienzo de la línea.
$ Coincide con el final de la línea
. Coincide con cualquier carácter (un comodín).
\s Coincide con un espacio en blanco.
\S Coincide con un carácter que no sea un espacio en blanco (el opuesto a \s).
* Se aplica al carácter o caracteres inmediatamente anteriores, indicando que
pueden coincidir cero o más veces.
+ Se aplica al carácter o caracteres inmediatamente anteriores, indicando que
pueden coincidir una o más veces.

*? Se aplica al carácter o caracteres inmediatamente anteriores, indicando que
coinciden cero o más veces en modo “no ambicioso”.
+? Se aplica al carácter o caracteres inmediatamente anteriores, indicando que
pueden coincidir una o más veces en modo “no ambicioso”.

#EJEMPLO AMBICIOSO Y NO AMBICIOSO
#Por ejemplo, considera el siguiente patrón de expresión regular: [a*?b]
#Si se aplica a la cadena "aabab", la coincidencia para .*? será "aab", ya que es la secuencia más corta que satisface la expresión regular completa.
#Si usamos /a.*b/ en la misma cadena, la coincidencia para .* será "aabab", ya que es la secuencia más larga que satisface la expresión regular completa.



? Se aplica al carácter o caracteres inmediatamente anteriores, indicando que
puede coincidir cero o una vez.
?? Se aplica al carácter o caracteres inmediatamente anteriores, indicando que
puede coincidir cero o una vez en modo “no ambicioso”.
[aeiou] Coincide con un solo carácter, siempre que éste se encuentre dentro del
conjunto especificado. En este caso, coincidiría con “a”, “e”, “i”, “o”, o “u”, pero
no con otros caracteres.
[a-z0-9] Se pueden especificar rangos de caracteres utilizando el signo menos. En
este caso, sería un solo carácter que debe ser una letra minúscula o un dígito.
[ˆA-Za-z] Cuando el primer carácter en la notación del conjunto es “ˆ”, invierte
la lógica. En este ejemplo, habría coincidencia con un solo carácter que no sea una
letra mayúscula o una letra minúscula. ###osea digitos o caracteres simbolos

( ) Cuando se agregan paréntesis a una expresión regular, son ignorados para
propósitos de encontrar coincidencias, pero permiten extraer un subconjunto de-
terminado de la cadena en que se encuentra la coincidencia, en lugar de toda la
cadena como cuando se utiliza findall().

\b Coincide con una cadena vacía, pero solo al comienzo o al final de una palabra.
\B Concide con una cadena vacía, pero no al comienzo o al final de una palabra.
\d Coincide con cualquier dígito decimal; equivalente al conjunto [0-9].
\D Coincide con cualquier carácter que no sea un dígito; equivalente al conjunto
[ˆ0-9].