# MenuArea

## Responsabilidade

Barra lateral fixa com as ações disponíveis ao usuário.

## Estrutura

Contém 5 botões de ação, exibidos verticalmente:

1. Cadastrar
2. Procurar
3. Ver Estante
4. Atualizar
5. Excluir

## Comportamento

Cada botão aciona a `MainArea`, substituindo o conteúdo atual pelo estado correspondente à ação escolhida.

## Layout

Posicionada na coluna 0 da `Window` com largura fixa.

Os botões internos são organizados com `pack()`.
