# GUI - Visão Geral

## Objetivo

A interface gráfica do NeoLibro é responsável pela interação direta com o usuário.

Sua função é apresentar as ações disponíveis, coletar entradas e exibir os resultados das operações realizadas pelo sistema.

## Papel na Arquitetura

O NeoLibro adota uma Arquitetura em Camadas.

Nesse contexto, a interface pertence à camada de apresentação e atua como ponto de entrada das ações do usuário.

A interface não contém regras de negócio. Sua responsabilidade é exclusivamente capturar entradas, acionar a camada de aplicação e exibir os resultados.

## Tecnologia Usada

A interface foi desenvolvida com CustomTkinter.

A escolha foi motivada pela familiaridade prévia com a tecnologia e por sua adequação aos requisitos do projeto.

## Estrutura Geral

A janela principal é composta por dois frames:

- **MenuArea** — barra lateral com as ações disponíveis ao usuário
- **MainArea** — área de trabalho central, onde as ações são exibidas e executadas

O layout é gerenciado com `grid()`, garantindo posicionamento explícito e estável dos frames.
