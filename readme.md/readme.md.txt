# 🚴‍♂️ Sabor Express – Otimização Inteligente de Rotas e Entregas

## 🧩 1. Descrição do Problema

A empresa **Sabor Express** é um serviço local de delivery de alimentos que atua na região central da cidade.  
Durante horários de pico (almoço e jantar), a empresa enfrenta grandes dificuldades para gerenciar as entregas, pois os entregadores escolhem as rotas de forma manual, baseados apenas na experiência pessoal.

Esse processo gera:
- Atrasos nas entregas;
- Aumento do consumo de combustível;
- Insatisfação dos clientes.

O proprietário percebeu que, para se manter competitivo, seria necessário **tornar as entregas mais rápidas, econômicas e organizadas**.  
Por isso, foi desenvolvida uma solução de **Inteligência Artificial (IA)** para **sugerir automaticamente as melhores rotas e agrupar pedidos próximos**, otimizando todo o processo logístico.

---

## 🎯 2. Objetivos do Projeto

- Encontrar o **menor caminho** entre múltiplos pontos de entrega.  
- **Agrupar entregas próximas** para reduzir o deslocamento dos entregadores.  
- Diminuir o **tempo total de entrega** e o **custo com combustível**.  
- Aumentar a **eficiência operacional** e a **satisfação dos clientes**.  

---

## ⚙️ 3. Abordagem Adotada

A cidade foi representada como um **grafo**, onde:
- Cada **nó (vértice)** representa um bairro ou ponto de entrega;
- Cada **aresta (linha)** representa uma rua;
- Os **pesos** representam o tempo ou a distância entre os locais.

A partir dessa representação, dois tipos de algoritmos de IA foram utilizados:

1. **Algoritmos de Busca de Caminho**  
   Para encontrar as rotas mais curtas e eficientes (A*, BFS, DFS).

2. **Algoritmo de Agrupamento (Clustering)**  
   Para dividir os pedidos em zonas próximas (K-Means), facilitando a distribuição entre os entregadores.

---

## 🧠 4. Algoritmos Utilizados

### 🔹 A* (A-estrela)
O algoritmo **A*** encontra o caminho mais curto entre dois pontos.  
Ele combina o **custo real do percurso já feito** com uma **estimativa da distância restante** (chamada de *heurística*).  
Isso o torna mais rápido e eficiente que métodos tradicionais como BFS.

**Exemplo de uso:**  
Encontrar a melhor rota do restaurante até o cliente, evitando ruas mais longas.

---

### 🔹 BFS (Busca em Largura)
O **BFS** explora o grafo por níveis, analisando primeiro os caminhos mais curtos em número de passos (não necessariamente em distância real).  
É útil para comparar a eficiência do A*.

---

### 🔹 DFS (Busca em Profundidade)
O **DFS** segue um caminho até o final antes de tentar alternativas.  
Embora menos eficiente para encontrar o caminho mais curto, ajuda a explorar todas as rotas possíveis.

---

### 🔹 K-Means (Agrupamento)
O **K-Means** é um algoritmo de aprendizado não supervisionado usado para **agrupar entregas próximas**.  
Ele cria grupos (clusters) baseados na localização dos pedidos.  
Cada cluster representa uma “zona de entrega”, que pode ser atribuída a um entregador diferente.

**Exemplo:**  
Se houver 30 pedidos espalhados pela cidade, o algoritmo pode dividi-los em 3 grupos de 10 pedidos próximos.

---

## 🗺️ 5. Modelo em Grafo

A cidade foi modelada como um grafo, onde cada ponto é uma localidade e cada linha representa uma rua com um peso (distância ou tempo).

Exemplo simplificado:

Restaurante ----(2 km)---- Bairro A ----(3 km)---- Bairro B
\
(4 km) (2 km)
\
---- Bairro C ------------- Bairro D


Cada conexão tem um **peso** que indica a distância entre os pontos.  
O algoritmo A* é usado para achar o **menor caminho** entre eles, e o K-Means para **agrupar** locais próximos.

> 💡 A figura do grafo pode ser gerada em código usando bibliotecas como `networkx` e `matplotlib`, ou adicionada como uma imagem estática.

---

## 📊 6. Resultados e Análises

### ✅ Resultados Esperados
- O A* encontra rotas mais curtas e rápidas que a busca tradicional.
- O K-Means cria grupos de entregas lógicos e próximos entre si.
- O tempo total de entrega é reduzido.
- Há economia de combustível e maior produtividade dos entregadores.

### ⚡ Eficiência
- O **A*** tem alta eficiência porque usa uma “heurística” que orienta a busca.  
- O **K-Means** é rápido e simples, adequado para cenários com muitos pedidos.

### ⚠️ Limitações
- O sistema não considera o **trânsito em tempo real**.  
- O **K-Means** pode formar grupos desequilibrados se houver muitos pedidos em uma mesma região.  
- É necessário **atualizar os dados do grafo** periodicamente (novas ruas, obras, bloqueios, etc).

---

## 🚀 7. Sugestões de Melhorias

- Integrar dados de trânsito em tempo real (API do Google Maps ou Waze).  
- Utilizar algoritmos mais avançados de roteirização (como *Vehicle Routing Problem* – VRP).  
- Implementar uma interface visual que mostre os mapas e rotas para os entregadores.  
- Considerar condições climáticas, horários de pico e restrições de tráfego.


## 👨‍💻 8. Conclusão

A solução proposta para a **Sabor Express** combina **Inteligência Artificial e modelagem de grafos** para otimizar as entregas.  
Com a aplicação dos algoritmos **A*** e **K-Means**, é possível reduzir atrasos, economizar combustível e aumentar a satisfação dos clientes.  

Essa abordagem mostra como conceitos de IA podem ser aplicados de forma prática para resolver **problemas reais de logística urbana**.

---

📌 **Autor:** VITOR EUFLOSINO  
📅 **Data: 02 Novembro de 2025  
🎓 **Projeto:** Otimização de Rotas e Entregas Inteligentes – Sabor Express
