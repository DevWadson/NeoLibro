# Visão Geral da Arquitetura

## Objetivo

O NeoLibro é um sistema de gerenciamento de obras literárias,
composto por várias camadas com responsabilidades específicas.

## Estrutura Geral

O sistema está dividido em 4 níveis:

- Domínio;
- Infraestrutura;
- Aplicação;
- Interface.

```text
src/
├── application/
├── core/
├── gui/
└── infra/
```

Ver [`docs/arquitetura/camadas.md`](docs/arquitetura/camadas.md) para mais detalhes.

## Fluxo Geral

Usuário → Interface → Serviço → Domínio → Infraestrutura.

## Princípios

- Separação de responsabilidades;
- Desacoplamento entre camadas;
- Centralização das regras de negócio no domínio;
- Persistência isolada da interface.
