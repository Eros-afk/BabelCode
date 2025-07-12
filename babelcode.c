// babelcode.c - Interpretador BabelCode em C (versão com suporte a strings)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_LINE 256
#define MAX_CODE 1024
#define MAX_VARS 64

// Variáveis simples
typedef struct {
    char nome[32];
    int valor;
} Variavel;

Variavel variaveis[MAX_VARS];
int var_count = 0;

int get_var_index(const char* nome) {
    for (int i = 0; i < var_count; i++) {
        if (strcmp(variaveis[i].nome, nome) == 0)
            return i;
    }
    strcpy(variaveis[var_count].nome, nome);
    variaveis[var_count].valor = 0;
    return var_count++;
}

int get_val(char* token) {
    if (token[0] >= 'a' && token[0] <= 'z') {
        return variaveis[get_var_index(token)].valor;
    }
    return atoi(token);
}

void interpretar(const char* caminho) {
    FILE* f = fopen(caminho, "r");
    if (!f) {
        printf("Erro ao abrir o arquivo BabelCode.\n");
        return;
    }

    char linha[MAX_LINE];
    char simbolo[8], resto[MAX_LINE];
    while (fgets(linha, sizeof(linha), f)) {
        if (linha[0] == '#' || strlen(linha) < 2) continue;
        simbolo[0] = resto[0] = '\0';
        sscanf(linha, "%s %[^]", simbolo, resto);

        // Remover espaços extras
        while (*resto == ' ') memmove(resto, resto+1, strlen(resto));

        if (strcmp(simbolo, "ν") == 0) {  // var
            char var[32], val[32];
            sscanf(resto, "%s %s", var, val);
            int idx = get_var_index(var);
            variaveis[idx].valor = get_val(val);
        } else if (strcmp(simbolo, "π") == 0) {  // print
            if (resto[0] == '\"') {
                printf("%s\n", resto);
            } else {
                int idx = get_var_index(resto);
                printf("%d\n", variaveis[idx].valor);
            }
        } else if (strcmp(simbolo, "α") == 0) {  // add
            char var[32], val[32];
            sscanf(resto, "%s %s", var, val);
            int idx = get_var_index(var);
            variaveis[idx].valor += get_val(val);
        } else if (strcmp(simbolo, "δ") == 0) {  // dec
            int idx = get_var_index(resto);
            variaveis[idx].valor -= 1;
        } else if (strcmp(simbolo, "μ") == 0) {  // mul
            char var1[32], var2[32];
            sscanf(resto, "%s %s", var1, var2);
            int idx = get_var_index(var1);
            variaveis[idx].valor *= get_val(var2);
        } else if (strcmp(simbolo, "λ") == 0) {  // loop
            char var[32], limite_str[32];
            sscanf(resto, "%s %s", var, limite_str);
            int idx = get_var_index(var);
            int limite = get_val(limite_str);
            long pos = ftell(f);
            while (variaveis[idx].valor > limite) {
                fseek(f, pos, SEEK_SET);
            }
        }
        // Nota: if/eq e blocos não implementados
    }

    fclose(f);
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Uso: ./babelcode arquivo.babel\n");
        return 1;
    }
    interpretar(argv[1]);
    return 0;
}
