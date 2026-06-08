# Consulta de Obras

## Objetivo

Descrever o processo de consulta no sistema.

## Participantes

- Usuário
- Interface
- Serviço
- Estante
- Repositório
- Banco de Dados

## Fluxo Principal

1. Usuário solicita consulta;
2. Interface coleta os critérios;
3. Serviço coordena consulta, chamando repositório;
4. Repositório procura os dados persistidos;
5. O sistema retorna resultado para a interface;
6. Interface exibe as obras encontradas ao usuário.
