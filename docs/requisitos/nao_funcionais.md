# Requisitos Não-Funcionais - NeoLibro

## RNF 01 - Modularidade

O sistema deve possuir separação de responsabilidade entre os módulos do sistema.

### Módulos

- Domínio;
- Interface;
- Infraestrutura;
- Serviço.
- ...

## RNF 02 - Desacoplamento

O sistema não pode permitir vazamento inadequado entre camadas, como:

- Interface não deve acessar a Persistência diretamente;
- Serviço não deve fazer nada além de orquestrar acões;
- Domínio não deve depender de Interface.
- ...

## RNF 03 - Persistência

O ambiente de produção deve coletar os dados das obras usando MySQL.

## RNF 04 - Estrutura

O sistema deve ser organizado seguindo o padrão de design em camadas.
