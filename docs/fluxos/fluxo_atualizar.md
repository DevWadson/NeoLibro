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
2. Interface coleta os dados a serem atualizados;
3. Serviço coordena a atualização, chamando a Estante;
4. Estante localiza a obra na coleção;
5. Estante valida e aplica os novos dados;
6. Repositório persiste as alterações;
7. O resultado é retornado ao serviço;
8. Interface exibe o resultado ao usuário.
