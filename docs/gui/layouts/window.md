# Window

## Responsabilidade

Janela principal da aplicação. Inicializa a interface, organiza os frames que compõem o layout e instancia os botões do menu.

## Estrutura

```text
Window
├── MenuArea   (coluna 0, largura fixa)
├── MainArea   (coluna 1, expansível)
├── CadastrarMenuOptionButton  (empacotado dentro de MenuArea, recebe MainArea via construtor)
├── ProcurarMenuOptionButton   (empacotado dentro de MenuArea, recebe MainArea via construtor)
├── VerEstanteMenuOptionButton (empacotado dentro de MenuArea, recebe MainArea via construtor)
├── AtualizarMenuOptionButton  (empacotado dentro de MenuArea, recebe MainArea via construtor)
└── ExcluirMenuOptionButton    (empacotado dentro de MenuArea, recebe MainArea via construtor)
```

## Layout

O layout é gerenciado com `grid()`.

|   Frame   |Coluna|   Comportamento    |
|-----------|------|--------------------|
|  MenuArea |   0  |    Largura fixa    |
|  MainArea |   1  |Expansível(weight=1)|

## Configurações

- Dimensões base: 1000x600
- Redimensionável: sim
- Título: NeoLibro
