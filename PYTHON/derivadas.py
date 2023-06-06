# Para iniciar, vamos considerar uma função bem simples:
# f(x)=x^3
# Das simples regras de derivação que são estudadas em disciplinas introdutórias de cálculo, sabemos que:
# f(x)=3x^2     f(x)=6x     f (x)=6

# configuração para outputs melhores no artigo, pode ser ignorado
from sympy import init_printing
init_printing(use_latex='png', scale=1.05, order='grlex',
              forecolor='Black', backcolor='White', fontsize=10)

from sympy import diff, Symbol

# 3x^2
x = Symbol('x')
f = x**3
diff(f, x)

# 6x
diff(f, x, 2)

# 6
diff(f, x, 3) 

from sympy import sin, cos, exp

# regra do produto
diff(x**2 * sin(x), x)

# regra da cadeia
diff(sin(x**2))

# regra do quociente
diff(x**2 / sin(x), x)

diff(x**2 / sin(x), x).factor()

