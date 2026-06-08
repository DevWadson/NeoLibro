# Banco de Dados - Visão Geral

## Objetivo

O banco de dados do NeoLibro é reponsável pela persistência permanente das informações do sistema.

Sua função é armazenar os dados das obras cadastradas, garantindo que as informações permaneçam disponíveis entre diferentes execuções da aplicação.

## Papel na Arquitetura

O NeoLibro adota uma Arquitetura em Camadas.

Nesse contexto, o banco de dados pertence à camada de infraestrutura e atua como mecanismo de persistência do sistema.

O domínio permanece isolado dos detalhes de implementação da persistência, não possuindo conhecimento sobre MySQL, consultas SQL ou infraestrutura.

O acesso aos dados ocorre por meio da camada Repository.

## Fonte Primária dos Dados

O banco de dados é considerado a fonte primária das informações do sistema.

Embora a Estante seja a principal abstração do domínio, ela não é responsável pelo armazenamento permanente dos dados.

Essa decisão foi adotada para:

- Garantir persistência entre execuções;
- Evitar concentração excessiva de responsabilidades na Estante;
- Promover separação adequada entre domínio e infraestrutura.

## Fluxo de Persistência

Usuário

↓

Interface

↓

Aplicação

↓

Estante

├─ Validação - Falha → Interrompe execução

└─ Validação - Aprovada → Repositório  → Banco de Dados.

Dessa forma, apenas objetos considerados válidos pelo domínio são encaminhados para persistência.

## Fluxo de Consulta

Nas operações de consulta, o banco de dados é acessado diretamente através do Repository.

Usuário

↓

Interface

↓

Aplicação

↓

Repositório

↓

Banco de Dados

↓

Hydration Model → Domain

↓

Aplicação

↓

Interface

↓

Usuário

A consulta não passa pela Estante, uma vez que o banco de dados é a fonte primária das informações do sistema.

## Tecnologia Usada

O NeoLibro utiliza MySQL como sistema gerenciador de banco de dados.

A escolha foi motivada pela familiaridade prévia com a tecnologia e por sua adequação aos requisitos do projeto.

## Modelagem

A modelagem do banco foi elaborada utilizando o BRModelo e posteriormente implementada em MySQL.

Os arquivos de modelagem encontram-se no diretório `brmodelo/`.

Os scripts SQL utilizados pela aplicação encontram-se em `mysql/scripts/`.

Os diagramas exportados para consulta e documentação encontram-se em `mysql/diagramas/`.

## Relação com o Domínio

O banco de dados não define regras de negócio.

As regras e validações permanecem concentradas no domínio, especialmente na Estante, que atua como principal abstração do sistema.

O papel do banco de dados é exclusivamente persistir e recuperar informações utilizadas pela aplicação.
