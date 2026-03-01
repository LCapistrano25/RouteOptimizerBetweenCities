# Route Optimizer Between Cities

ℹ️ Este projeto é uma implementação em Python de um sistema de gerenciamento de grafos voltado para cidades e rotas. O código utiliza estruturas de dados eficientes como dicionários e classes para representar a conectividade entre localidades.

## 🚀 Funcionalidades

- **Gerenciamento de Cidades**: Adição de nós (cidades) ao grafo com identificação única.
- **Criação de Rotas**: Estabelecimento de conexões entre cidades com custos (distâncias) associados.
- **Caminho Mais Curto**: Algoritmo para encontrar a rota menos custosa entre dois pontos.
- **Listagem de Rotas**: Visualização de todas as rotas possíveis entre cidades selecionadas.
- **Interface Interativa**: Menu via terminal para fácil interação com o sistema.

## 🛠️ Detalhes Técnicos

O código foi desenvolvido com foco em legibilidade e está totalmente em **inglês**, utilizando as seguintes classes principais:

- `Node` ([node.py](node.py)): Representa cada cidade e seus vizinhos.
- `Graph` ([graph.py](graph.py)): Gerencia a lógica do grafo e algoritmos de busca.
- `main` ([main.py](main.py)): Ponto de entrada que executa o menu interativo.

## 🔧 Como Executar

Certifique-se de ter o Python instalado e a biblioteca `colorama` (utilizada para cores no terminal).

```bash
python main.py
```

---
*Este projeto demonstra conceitos fundamentais de teoria dos grafos e algoritmos de busca.*
