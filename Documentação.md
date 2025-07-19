# 📚 BabelLang — Documentação

Documentação oficial da **BabelLang**  
Uma linguagem esotérica com suporte a múltiplos alfabetos e comandos simples, inspirada na torre de Babel.

---

## ✨ Visão Geral

- O alfabeto dos comandos é sorteado a cada execução, tornando o código visualmente diferente, mas semanticamente igual.
- Ideal para estudar transpilação, internacionalização e criatividade em programação.

---

## 📦 Estrutura dos Arquivos

- Os arquivos BabelLang devem ter a extensão `.babel`.
- Exemplo: `meuprograma.babel`

---

## 📝 Sintaxe Básica

### Atribuição de Variáveis

```plaintext
x = 5           # Atribui 5 à variável x
r = 1           # Atribui 1 à variável r
```

### Comandos Especiais (usando símbolo do alfabeto sorteado)

| Comando | Descrição              | Exemplo      | Python gerado         |
|---------|------------------------|--------------|-----------------------|
| π x     | Imprime valor          | π x          | print(x)              |
| λ x 0   | Enquanto x > 0         | λ x 0        | while x > 0:          |
| δ x     | Decrementa x           | δ x          | x -= 1                |
| α x 1   | Incrementa x           | α x 1        | x = x + 1             |
| μ r x   | Multiplica r por x     | μ r x        | r = r * x             |
| ε x y   | Igualdade (bool)       | ε x y        | x == y                |
| ι x y   | Condicional (if x==y)  | ι x y        | if x == y:            |
| n x     | Entrada do usuário     | n x          | x = int(input())      |

> **Nota:** Os símbolos mudam conforme o alfabeto sorteado  
> (por exemplo: `π` para print no grego, `п` no cirílico, `פ` no hebraico etc).

---

## 💬 Comentários

- Qualquer texto após `#` em uma linha é ignorado pelo interpretador.

---

## 🧩 Exemplo de Código

```plaintext
x = 5
r = 1
λ x 1
    μ r x
    δ x
π r
```

---

## 🚀 Execução

Para executar um programa BabelLang, use:

No Windows:
```sh
python BabelCode.py programa.babel [--debug]
```
No Linux:
```sh
python3 BabelCode.py programa.babel [--debug]
```

- Use o parâmetro `--debug` para ver o passo a passo da transpilação.

---

## 🌐 Alfabetos Suportados

- Latino
- Grego
- Cirílico
- Hebraico
- Árabe
- Devanágari
- Armênio
- Georgiano
- Tailandês

O alfabeto é sorteado a cada execução.

---

## ⚠️ Observações

- Indentação é feita por espaços, como em Python.
- Os comandos especiais devem ser escritos com os símbolos dos alfabetos suportados.
- O arquivo `BabelCode.py` deve estar na mesma pasta dos arquivos `.babel`.
- A saída mostrará o resultado do código executado caso o alfabeto usado tenha sido o mesmo do sorteado.

---

## 👀 Observação Final

Aproveite para aprender e explorar diferentes alfabetos usando a BabelLang!  
Dúvidas ou sugestões? Contribua com o projeto no GitHub!

---
