# MainArea

## Responsabilidade

Área de trabalho central da aplicação. Exibe o conteúdo correspondente à ação escolhida pelo usuário no menu.

## Estados

|    Ação    |                   Conteúdo exibido                     |
|------------|--------------------------------------------------------|
|   Início   | Tela de boas-vindas                                    |
| Cadastrar  | Seleção de tipo → formulário de cadastro               |
|  Procurar  | Formulário de busca + resultados                       |
| Ver Estante| Lista paginada de obras                                |
|  Atualizar | Busca por título ou código → formulário de atualização |
|  Excluir   | Formulário similar ao Procurar                         |

## Comportamento

O conteúdo é substituído via `_clear_frame()` a cada nova ação acionada pelo menu.

## Layout

Posicionada na coluna 1 da `Window`, expansível em ambos os eixos.
