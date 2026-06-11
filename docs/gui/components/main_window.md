# MainWindow

## Responsabilidade

Janela principal da aplicação. Inicializa a interface e organiza os frames que compõem o layout.

## Estrutura

```text
MainWindow
├── MenuArea   (coluna 0, largura fixa)
└── MainArea   (coluna 1, expansível)
```

## Layout

O layout é gerenciado com `grid()`.

| Frame  | Coluna |     Comportamento     |
|--------|--------|-----------------------|
|MenuArea|   0    | Largura fixa          |
|MainArea|   1    | Expansível (weight=1) |

## Configurações

- Dimensões base: 1000x600
- Redimensionável: sim
- Título: NeoLibro
