import sys
import random

# =====================
# 1. DEFINIÇÃO DOS ALFABETOS
# =====================
# Apenas letras realmente usadas nos comandos e que têm sons equivalentes nos alfabetos
# Comandos usados: v, p, l, i, n, a, d, e, m
COMMON_LETTERS = "vplinadem"

ALPHABETS = {
    "greek":    dict(zip(COMMON_LETTERS, "υπλιναδεμ")),
    "cyrillic": dict(zip(COMMON_LETTERS, "вплинadem")),  
    "hebrew":   dict(zip(COMMON_LETTERS, "ואפלינאדם")),
}

# =====================
# 2. COMANDOS INTERNOS
# =====================
COMMANDS = {
    'v': 'var',     # declaração de variável
    'p': 'print',   # imprime valor
    'l': 'loop',    # while (loop)
    'i': 'if',      # condicional
    'n': 'input',   # entrada do usuário
    'a': 'add',     # soma
    'd': 'dec',     # decremento
    'e': 'eq',      # igualdade
    'm': 'mul',     # multiplicação
}

# =====================
# 3. TRANSPILEDOR
# =====================
def transpilar_linha(linha, reverse_map, debug=False):
    linha = linha.split('#')[0].strip()
    if not linha:
        return ""
    tokens = linha.strip().split(maxsplit=1)
    if not tokens:
        return ""
    cmd_symbol = tokens[0]
    arg = tokens[1] if len(tokens) > 1 else ""
    if debug:
        print(f"[DEBUG] cmd_symbol: {repr(cmd_symbol)}")
        print(f"[DEBUG] reverse_map: {reverse_map}")
    cmd_char = reverse_map.get(cmd_symbol, '?')
    if debug:
        print(f"[DEBUG] cmd_char: {cmd_char}")
    if cmd_char == 'p':
        py = f"print({arg})"
    elif cmd_char == 'v':
        parts = arg.split()
        if len(parts) == 2:
            var, val = parts
            if val == 'n':
                py = f"{var} = int(input())"
            else:
                py = f"{var} = {val}"
        elif len(parts) == 1:
            py = f"# Erro: declaração de variável sem valor: {arg}"
        else:
            py = f"# Erro de sintaxe na declaração: {arg}"
    elif cmd_char == 'a':
        var, val = arg.split()
        py = f"{var} = {var} + {val}"
    elif cmd_char == 'd':
        py = f"{arg} -= 1"
    elif cmd_char == 'm':
        var1, var2 = arg.split()
        py = f"{var1} = {var1} * {var2}"
    elif cmd_char == 'i':
        var, val = arg.split()
        py = f"if {var} == {val}:"
    elif cmd_char == 'l':
        var, val = arg.split()
        py = f"while {var} > {val}:"
    elif cmd_char == 'n':
        py = f"{arg} = int(input())"
    else:
        py = f"# Comando desconhecido: {cmd_symbol}"
    if debug:
        print(f"[TRANSPILE] {linha}  →  {py}")
    return py

def transpilar(codigo, reverse_map, debug=False):
    linhas = codigo.strip().split('\n')
    resultado = []
    indent = 0
    for linha in linhas:
        py = transpilar_linha(linha, reverse_map, debug)
        if py.endswith(':'):
            resultado.append("    " * indent + py)
            indent += 1
        elif py.strip() == "":
            indent = max(indent - 1, 0)
        else:
            resultado.append("    " * indent + py)
    return '\n'.join(resultado)

# =====================
# 4. EXECUÇÃO PRINCIPAL
# =====================
def main():
    if len(sys.argv) < 2:
        print("Uso: python BabelCode.py arquivo.babel [--debug]")
        return
    filename = sys.argv[1]
    debug = '--debug' in sys.argv
    with open(filename, "r", encoding="utf-8") as f:
        codigo_babel = f.read()
    nome_alfabeto, mapa = random.choice(list(ALPHABETS.items()))
    reverse_map = {v: k for k, v in mapa.items()}
    print(f"[BabelCode] Alfabeto sorteado: {nome_alfabeto.upper()}")
    #print(f"[BabelCode] Mapeamento de comandos:")
    #for k, v in mapa.items():
    #   print(f"  {k} → {v}")
    codigo_python = transpilar(codigo_babel, reverse_map, debug)
    print("\n>>> Código Python gerado:")
    print(codigo_python)
    print("\n>>> Saída da execução:")
    exec(codigo_python)
    print("\n>>> Fim da execução.\n")

if __name__ == "__main__":
    main()