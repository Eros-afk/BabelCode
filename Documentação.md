# =====================
# DOCUMENTAÇÃO INTERNA
# =====================

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

# BabelLang — Documentação

## Visão Geral

BabelLang é uma linguagem de programação didática e minimalista, inspirada em comandos simples e com suporte a múltiplos alfabetos (latino, grego, cirílico, hebraico, árabe, devanágari, armênio, georgiano, tailandês, etc). Seu objetivo é demonstrar conceitos de transpilação e internacionalização de sintaxe.

---

## Extensão dos Arquivos

- Os arquivos BabelLang devem ter a extensão: `.babel`

---

## Sintaxe Básica

### Atribuição de Variáveis

```plaintext
x = 5          # Atribui 5 à variável x
r = 1          # Atribui 1 à variável r
```

### Comandos Especiais (usando símbolos do alfabeto sorteado)

| Comando | Descrição                        | Exemplo                | Python gerado           |
|---------|----------------------------------|------------------------|-------------------------|
| π x     | Imprime valor                    | π x                    | print(x)                |
| λ x 0   | Loop enquanto x > 0              | λ x 0                  | while x > 0:            |
| δ x     | Decrementa x                     | δ x                    | x -= 1                  |
| α x 1   | Incrementa x                     | α x 1                  | x = x + 1               |
| μ r x   | Multiplica r por x               | μ r x                  | r = r * x               |
| ε x y   | Condicional (if x == y)          | ε x y                  | if x == y:              |
| n x     | Entrada do usuário em x          | n x                    | x = int(input())        |

> **Nota:** Os símbolos mudam conforme o alfabeto sorteado (ex: π para print no grego, п no cirílico, פ no hebraico, etc).

---

## Comentários

- Qualquer texto após `#` em uma linha é ignorado pelo interpretador.

---

## Execução

Para executar um programa BabelLang:

```sh
python BabelCode.py programa.babel [--debug]
```

- Use `--debug` para ver o passo a passo da transpilação.

---

## Alfabetos Suportados

- Latino
- Grego
- Cirílico
- Hebraico
- Árabe
- Devanágari
- Armênio
- Georgiano
- Tailandês

O alfabeto é sorteado a cada execução, tornando o código visualmente diferente, mas semanticamente igual.

---

## Exemplo

```plaintext
x = 5
r = 1
λ x 1
    μ r x
    δ x
π r
```

---

## Observações

- Indentação é feita por espaços (como em Python).
- O sinal `=` pode ser usado para atribuição direta, sem necessidade de comando especial.
- Os comandos especiais devem ser escritos com o símbolo do alfabeto sorteado correspondente.
