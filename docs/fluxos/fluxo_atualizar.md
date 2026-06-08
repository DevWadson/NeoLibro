# Atualizar Obras

## Objetivo

Descrever o processo da atualização de dados das obras no sistema.

## Participantes

- Usuário
- Interface
- Serviço
- Estante
- Repositório
- Banco de Dados

## Fluxo Principal

1. Usuário solicita atualização de uma obra;
2. Interface coleta os dados inseridos;
3. Serviço coordena a atualização, chamando repositório;
4. Repositório localiza a obra;
5. Repositório atualiza os dados persistidos;
6. O resultado é retornado ao serviço;
7. Interface exibe o resultado ao usuário.
