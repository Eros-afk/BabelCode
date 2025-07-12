# =====================
# DOCUMENTAÇÃO INTERNA
# =====================

"""
Extensão dos arquivos BabelCode: .babel

Comandos suportados:
    ν x 5        → var x = 5
    π x          → print(x)
    λ x 0        → while x > 0
    δ x          → x -= 1
    α x 1        → x = x + 1
    μ r x        → r = r * x
    ε x y        → if x == y:
    π            → fim de bloco

Comentários:
    Qualquer texto após '#' é ignorado pelo interpretador.

Execução:
    python BabelCode.py programa.babel [--debug]

Debug:
    Use --debug para ver passo a passo da transpilação.
"""
