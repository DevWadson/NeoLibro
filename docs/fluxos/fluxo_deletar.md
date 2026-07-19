# Deletar Obras

## Objetivo

Descrever o processo de deleção no sistema.

## Participantes

- Usuário
- Interface
- Serviço
- Estante
- Repositório
- Banco de Dados

## Fluxo Principal

1. Usuário solicita deleção de obra;
2. Interface coleta os critérios;
3. Serviço coordena a deleção, chamando a Estante;
4. Estante localiza a obra na coleção;
5. Estante remove a obra da coleção;
6. Repositório exclui os dados persistidos;
7. O resultado é retornado ao serviço;
8. Interface exibe mensagem ao usuário.
