# Forms

## Responsabilidade

Os formulários são responsáveis por capturar e expor os dados fornecidos pelo usuário.

Cada form corresponde a um tipo de obra: `HQForm`, `LivroForm` e `MangaForm`.

## Responsabilidades do Form

- Renderizar os campos correspondentes ao tipo de obra
- Validar formato básico de entrada (campo vazio, tipo incorreto, etc.)
- Coletar os dados preenchidos via `_extract_data()`
- Disparar o callback de submit ao confirmar

## Restrições

- Não deve conhecer o `NeoLibroService` ou qualquer camada de aplicação
- Não deve decidir o que fazer com os dados após a coleta
- Não deve saber como persistir ou processar informações

## Comportamento

O form recebe um callback de submit na inicialização.

Ao confirmar, chama o callback passando os dados coletados — sem saber quem vai processá-los.

A coordenação entre form e serviço é responsabilidade da `MainArea`.

## Campos por Tipo

### HQForm

- Título
- Indústria
- Edição
- Volume
- Preço

### LivroForm

- Título
- Autor
- Editora
- Publicação
- Páginas
- Preço

### MangaForm

- Título
- Autor
- Editora
- Publicação
- Capítulos
- Preço
