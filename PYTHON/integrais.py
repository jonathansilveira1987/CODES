import sympy as sy
from sympy.interactive import init_printing
init_printing(pretty_print=True)

# Declara a variável simbólica
x = sy.Symbol('x')
# Explicita a função
funcao = x**10

# Resolve a função
resultado = sy.diff(funcao)
resultado

import sympy as sy
from sympy.interactive import init_printing
init_printing(pretty_print=True)

# Declara as variaveis simbolicas
x, y, z = sy.symbols('x y z')

# Funcao a ser resolvida
funcao = x**10 * y**3 * z**8

# Calcula o resultado da derivada parcial em funcao de X
resultadoRelativoX = sy.diff(funcao, x)
resultadoRelativoX