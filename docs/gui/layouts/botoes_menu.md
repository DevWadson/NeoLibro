# Botões do Menu

## Responsabilidade

Os botões do menu são responsáveis exclusivamente por disparar a ação correspondente ao serem clicados.

## Comportamento

Cada botão recebe um callback na inicialização. Ao ser clicado, chama esse callback sem saber o que ele faz.

O `MenuArea` cria os botões dinamicamente a partir de um dicionário de callbacks recebido da `MainWindow`.

## Coordenação

A `MainWindow` é responsável por definir os callbacks e coordenar a comunicação entre `MenuArea` e `MainArea`.

## Ações disponíveis

|    Botão    |                     Ação na MainArea                        |
|-------------|-------------------------------------------------------------|
| Cadastrar   | Seleção de tipo → formulário de cadastro                    |
| Procurar    | Formulário de busca + resultados                            |
| Ver Estante | Lista paginada de obras                                     |
| Editar      | Busca por título ou código → formulário de edição por campo |
| Excluir     | Formulário similar ao Procurar                              |
