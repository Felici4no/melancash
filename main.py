# ------------------------------------------------------------------------------
# MELANCASH - Otimização de Contribuições para Completar uma Melancia Digital
# Dynamic Programming + Recursion + Memoization + Merge Sort
# ------------------------------------------------------------------------------

import random
from functools import lru_cache

# ---------------------------------------------------------------------
# 1. FORMULAÇÃO DO PROBLEMA
# ---------------------------------------------------------------------
"""
Entrada:
 - Lista de contribuintes da MelanCash, cada um contendo:
      nome, valor que deseja contribuir, confiabilidade (0 a 1)
 - Meta total da melancia (R$)

Objetivo:
 - Escolher a melhor combinação de contribuições que:
       (a) Chegue o mais próximo possível da meta (sem ultrapassar)
       (b) Maximize a soma da confiabilidade dos usuários selecionados

Saída:
 - Lista otimizada de contribuintes
 - Relatório final da solução
"""

# Criamos pelo menos *20 contribuições* para cumprir o requisito da atividade.
NOMES = [
    "Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel", "Helena", "Igor", "Júlia", "Kleber", "Larissa",
    "Marcos", "Natália", "Otávio", "Patrícia", "Quintino", "Renata",
    "Samuel", "Talita", "Uéliton", "Vitória", "Wesley", "Xênia",
    "Yuri", "Zuleica"
]

def gerar_contribuicoes():
    """Gera automaticamente 20+ contribuições aleatórias."""
    contribs = []
    for nome in NOMES:
        contribs.append({
            "nome": nome,
            "valor": random.randint(10, 120),
            "confiabilidade": round(random.uniform(0.50, 0.99), 2)
        })
    return contribs


# ---------------------------------------------------------------------
# 2. MERGE SORT (recursivo) para ordenar por valor
# ---------------------------------------------------------------------
def merge_sort(lista):
    """Ordena a lista de contribuições pelo valor usando Merge Sort recursivo."""
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)


def merge(left, right):
    """Função auxiliar que intercalará as listas."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["valor"] < right[j]["valor"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------------------------------------------------------------------
# 3. MOCHILA (recursiva com memoização)
# ---------------------------------------------------------------------
"""
Função de mochila:
 - Capacidade = meta total da melancia
 - Pesos = valores das contribuições
 - Valor do item = confiabilidade + valor (para dar prioridade mista)
"""

def resolver_melancia(contribs, meta):
    # Memoização via decorator
    @lru_cache(maxsize=None)
    def dp(i, restante):
        """Retorna (confiabilidade_total, valor_total, itens_selecionados)."""

        # Caso base: fim da lista
        if i == len(contribs):
            return (0, 0, ())

        nome = contribs[i]["nome"]
        valor = contribs[i]["valor"]
        conf = contribs[i]["confiabilidade"]

        # 1. Pular item
        sem_item = dp(i + 1, restante)

        # 2. Incluir item (se couber)
        if valor <= restante:
            com_item = dp(i + 1, restante - valor)
            # Adiciona valores
            com_item = (
                com_item[0] + conf,
                com_item[1] + valor,
                com_item[2] + (i,)
            )
        else:
            com_item = (-1, -1, ())  # opção inválida

        # Critério de escolha:
        # 1º maior confiabilidade — 2º maior valor total
        if com_item[0] > sem_item[0]:
            return com_item
        if com_item[0] == sem_item[0] and com_item[1] > sem_item[1]:
            return com_item
        return sem_item

    return dp(0, meta)


# ---------------------------------------------------------------------
# 4. RELATÓRIO
# ---------------------------------------------------------------------
def gerar_relatorio(contribs, meta, solucao):
    conf_total, valor_total, indices = solucao

    print("\n================= RELATÓRIO FINAL - MELANCASH =================")
    print(f"META DA MELANCIA: R$ {meta}")
    print(f"TOTAL ALCANÇADO:  R$ {valor_total}")
    print(f"CONFIABILIDADE TOTAL: {round(conf_total, 2)}")
    print(f"FALTANDO: R$ {meta - valor_total}")
    print("\nLISTA OTIMIZADA DE FATIAS:")

    for idx in indices:
        c = contribs[idx]
        print(f" - {c['nome']}: R$ {c['valor']} (conf: {c['confiabilidade']})")

    print("===============================================================\n")


# ---------------------------------------------------------------------
# 5. PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------

if __name__ == "__main__":
    random.seed(42)

    contribs = gerar_contribuicoes()

    print("Ordenando contribuições por valor com Merge Sort recursivo...")
    contribs = merge_sort(contribs)

    META = 300  # meta da melancia

    solucao = resolver_melancia(contribs, META)

    gerar_relatorio(contribs, META, solucao)

