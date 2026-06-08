# Cadastro de Obras

## Objetivo

Descrever o processo de cadastro de uma obra no sistema.

## Participantes

- Usuário
- Interface
- Serviço
- Estante
- Repositório
- Banco de Dados

## Fluxo Principal

1. Usuário insere os dados;
2. Interface coleta os dados inseridos;
3. Serviço coordena a adição, chamando estante;
4. Estante valida os dados coletados pela Interface;
5. É gerado um codigo de rastreio para a obra;
6. A obra é adicionada na sua coleção;
7. Repositório persiste a obra;
8. O sistema retorna mensagem ao usuário.
