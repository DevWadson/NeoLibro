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
3. Serviço coordena a deleção, chamando repositório;
4. Repositório localiza a obra;
5. Repositório exclui os dados persistidos;
6. O sistema retorna resultado para a interface;
7. Interface exibe mensagem ao usuário.
