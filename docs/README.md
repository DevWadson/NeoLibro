# NeoLibro

## Sobre o Projeto

NeoLibro é um sistema para gerenciamento de obras literárias, desenvolvido para organizar coleções de HQs, Livros e Mangás.

O projeto surgiu inicialmente como uma necessidade pessoal de catalogação de obras e evoluiu gradualmente para um estudo prático de desenvolvimento de software, modelagem, arquitetura e boas práticas.

Atualmente o sistema encontra-se em sua quinta versão, resultado de diversas refatorações e evoluções realizadas ao longo do seu desenvolvimento.

## Funcionalidades

Atualmente o sistema permite:

- Cadastro de HQs;
- Cadastro de Livros;
- Cadastro de Mangás;
- Consulta de obras cadastradas;
- Persistência de dados utilizando MySQL;
- Geração automática de códigos de rastreabilidade.

### Funcionalidades Planejadas

- Atualização de obras;
- Exclusão de obras;
- Evolução da interface gráfica.

## Arquitetura

O NeoLibro utiliza Arquitetura em Camadas.

Estrutura principal:

```text
src/
├── application/
├── core/
├── gui/
└── infra/
```

A camada de aplicação coordena os casos de uso do sistema.

O domínio permanece isolado da interface e da infraestrutura, enquanto a persistência é realizada através da camada Repository.

A principal abstração do domínio é a Estante, responsável por centralizar regras e validações relacionadas às obras.

## Tecnologias Utilizadas

- Python
- MySQL
- CustomTkinter
- UV
- BRModelo

## Estrutura do Projeto

```text
src/
├── application/
├── core/
├── gui/
└── infra/
```

```text
docs/
├── arquitetura/
├── banco/
├── fluxo/
├── gui/
└── requisitos/
```

## Documentação

A documentação do projeto encontra-se no diretório `docs/`.

Principais tópicos documentados:

- Requisitos Funcionais;
- Regras de Negócio;
- Requisitos Não-Funcionais;
- Arquitetura;
- Fluxos de Uso;
- Banco de Dados;
- Decisões Arquiteturais.

## Status Atual

### Concluído

- Cadastro de obras;
- Consulta de obras;
- Persistência em MySQL;
- Documentação arquitetural.

### Em Desenvolvimento

- Interface gráfica.

### Planejado

- Atualização de obras;
- Exclusão de obras;
- Sistema de notificações.

## Histórico

O NeoLibro teve origem em uma versão desenvolvida em C para gerenciamento pessoal de obras.

Na época de sua criação, conceitos como modularização, arquitetura de software e separação de responsabilidades ainda não faziam parte do processo de desenvolvimento adotado no projeto.

Mesmo assim, diversas ideias presentes na arquitetura atual já existiam em sua forma inicial, especialmente a Estante, criada para representar uma biblioteca digital e organizar as diferentes mídias do sistema.

Posteriormente o projeto foi reescrito em Python e passou por diversas versões e refatorações.

Grande parte das decisões presentes na arquitetura atual surgiu inicialmente de forma prática durante o desenvolvimento do sistema.

Com o avanço dos estudos em desenvolvimento de software, esses conceitos passaram a ser compreendidos, refinados e formalizados arquiteturalmente nas versões posteriores do projeto.

Assim, a evolução do NeoLibro ocorreu seguindo o fluxo:

```text
Problema
↓
Implementação
↓
Estudo
↓
Descoberta do conceito formal
↓
Refatoração
```

e não o contrário.

## Autor

Desenvolvido por Marlon Wadson.

Contato: marlonwadson.dev@gmail.com

Para sugestões, dúvidas ou contribuições, utilize as Issues e Pull Requests do projeto.
