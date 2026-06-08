# Visão Geral da Arquitetura

## Objetivo

O NeoLibro é um sistema de gerenciamento de obras literárias,
composto por várias camadas com responsabilidades específicas.

## Estrutura Geral

O sistema está dividido em x níveis:

- Domínio;
- Infraestrutura;
- Aplicação;
- Interface.

## Fluxo Geral

Usuário → Interface → Serviço → Domínio → Infraestrutura.

## Princípios

- Separação de responsabilidades;
- Desacoplamento entre camadas;
- Centralização das regras de negócio no domínio;
- Persistência isolada da interface.
