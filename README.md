# 🍉 MelanCash – Otimização de Contribuições com Programação Dinâmica

Projeto desenvolvido como parte da disciplina **Dynamic Programming**, integrando o tema da **Global Solution**.  
A ideia baseia-se na **MelanCash**, uma melancia digital que as pessoas "preenchem" com contribuições financeiras (fatias).  

O objetivo é usar **programação dinâmica**, **recursão**, **memoização** e **métodos de ordenação** para encontrar a melhor combinação de contribuições para completar a melancia.

---

## 🎯 Formulação do Problema

Cada pessoa pode contribuir com um valor para ajudar a "encher" a melancia.  
Para cada contribuição temos:

- **nome**
- **valor da fatia (R$)**
- **confiabilidade (0.5 a 0.99)**

A melancia tem uma meta (ex: R$300).  
O sistema deve **selecionar contribuições que cheguem o mais próximo possível da meta**, sem ultrapassar, **maximizando também a confiabilidade total dos participantes**.

---

## 📌 Requisitos Atendidos

✔ Recursão  
✔ Memoização (via `lru_cache`)  
✔ Ordenação com **Merge Sort recursivo**  
✔ Solução com **Programação Dinâmica (mochila 0/1)**  
✔ Geração de **relatório final**  
✔ Pelo menos **20 contribuições**  
✔ Código totalmente comentado  
✔ Estrutura clara para ser apresentada na disciplina  

---

## 🧠 Técnicas Utilizadas

### 1. **Merge Sort (Recursivo)**
Usado para ordenar contribuições pelo valor.  
Importante para relatórios e iteração estruturada.

### 2. **Mochila (Knapsack 0/1)**
Adaptada ao contexto:
- Peso = valor da contribuição  
- Valor do item = confiabilidade + ponderação  
- Objetivo = maximizar confiabilidade sem ultrapassar a meta  

### 3. **Memoização**
Melhora desempenho guardando subproblemas já calculados.

### 4. **Relatórios**
O programa imprime automaticamente:
- Meta
- Valor alcançado
- Confiabilidade total
- Fatias escolhidas

---

## 🚀 Como Executar

1. Instale Python 3.10+
2. Clone o repositório
3. Execute:

