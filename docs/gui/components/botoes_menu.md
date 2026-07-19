# Botões do Menu

## Responsabilidade

Botões de ação disponíveis na MenuArea: Cadastrar, Procurar, Ver Estante, Atualizar e Excluir.

## Comportamento

Cada botão recebe a instância de `MainArea` diretamente no construtor. Ao ser clicado, chama um método específico e nomeado da `MainArea` (ex.: `main_area.mostrar_opcoes_cadastro()`) — não um callback genérico.

Quem cria e instancia os botões é a `Window`, não a `MenuArea`. A `MenuArea` apenas serve de container visual (`parent`) onde os botões são empacotados.

## Ações disponíveis

|    Botão    |                    Ação na MainArea                    |
|-------------|--------------------------------------------------------|
|  Cadastrar  | Seleção de tipo → formulário de cadastro               |
|   Procurar  | Formulário de busca + resultados                       |
| Ver Estante | Lista paginada de obras                                |
|  Atualizar  | Busca por título ou código → formulário de atualização |
|   Excluir   | Formulário similar ao Procurar                         |
