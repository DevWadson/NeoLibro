# Decisões Arquiteturais - NeoLibro

## DA01 - Utilização de Arquitetura em Camadas

### Contexto

Durante a evolução do projeto, tornou-se necessário organizar melhor as responsabilidades da aplicação e aproximar sua estrutura de softwares utilizados em ambientes profissionais.

### Decisão

Adotar uma arquitetura baseada em camadas, separando domínio, aplicação, interface e infraestrutura.

### Consequências

- Menor acoplamento entre componentes;
- Responsabilidades mais bem definidas;
- Maior facilidade de manutenção e evolução.

## DA02 - Estante como Abstração Central do Domínio

### Contexto

O NeoLibro nasceu como uma representação digital de uma biblioteca pessoal.

Desde as primeiras versões, a Estante foi concebida como a principal abstração da biblioteca representada pelo sistema.

### Decisão

Manter a Estante como elemento central do domínio, responsável pela organização e gerenciamento das obras.

### Consequências

- O domínio permanece independente da persistência;
- A modelagem reflete conceitos reais do problema;
- As regras relacionadas à coleção de obras permanecem centralizadas.

## DA03 - Separação entre Domínio e Persistência

### Contexto

As responsabilidades de domínio e armazenamento possuem naturezas distintas.

### Decisão

Separar a gestão das obras da responsabilidade de persistência.

### Consequências

- A Estante representa conceitos do domínio;
- O Repository representa mecanismos de persistência;
- As responsabilidades permanecem bem definidas.

## DA04 - Banco de Dados como Fonte Primária

### Contexto

A persistência em memória realizada pela Estante é volátil e não garante armazenamento permanente.

### Decisão

Utilizar o banco de dados como fonte primária dos dados do sistema.

### Consequências

- As consultas devem ser realizadas através do Repository;
- Os dados permanecem disponíveis entre execuções;
- A Estante deixa de ser a fonte primária dos dados persistidos.

## DA05 - Introdução da Camada Service

### Contexto

Durante a evolução do projeto, identificou-se que a coordenação dos casos de uso não pertencia ao domínio.

Nas versões anteriores parte dessa responsabilidade encontrava-se concentrada na Estante.

### Decisão

Introduzir uma camada Service responsável por coordenar as operações da aplicação.

### Consequências

- Redução do acoplamento entre camadas;
- Melhor separação de responsabilidades;
- Centralização dos casos de uso.

## DA06 - Isolamento do Domínio

### Contexto

Dependências desnecessárias entre camadas aumentam o custo de manutenção do sistema.

### Decisão

Impedir que o domínio dependa diretamente de interface gráfica, banco de dados, ORM ou infraestrutura.

### Consequências

- O domínio permanece independente;
- Mudanças tecnológicas possuem menor impacto;
- As regras de negócio permanecem concentradas no núcleo da aplicação.

## DA07 - Modelagem por Especialização de Obras

### Contexto

HQs, Livros e Mangás representam mídias distintas e possuem características próprias.

### Decisão

Modelar os diferentes tipos de obra por especialização a partir da entidade base Obra.

### Consequências

- Compartilhamento de atributos comuns;
- Redução de duplicação de código;
- Representação mais fiel do domínio.

## DA08 - Organização das Obras por Tipo

### Contexto

As diferentes mídias devem permanecer claramente separadas dentro da biblioteca.

### Decisão

Manter coleções específicas para cada tipo de obra dentro da Estante.

### Consequências

- Maior clareza organizacional;
- Facilidade de manutenção;
- Estrutura alinhada à modelagem do domínio.

## DA09 - Geração Automática de Códigos

### Contexto

O código de rastreamento é uma responsabilidade do sistema e não do usuário.

### Decisão

Gerar automaticamente os códigos das obras durante o processo de cadastro.

### Consequências

- Garantia de padronização;
- Menor chance de inconsistências;
- Simplificação do cadastro.

## DA10 - Utilização de Códigos Sequenciais Legíveis

### Contexto

Versões anteriores utilizaram identificadores baseados em UUID.

Com a evolução do sistema surgiu a necessidade de melhorar a legibilidade e rastreabilidade dos códigos.

### Decisão

Adotar códigos sequenciais identificados pelo tipo da obra.

#### Exemplos
- HQ-001
- MNG-001
- LVR-001

### Consequências

- Melhor legibilidade;
- Facilidade de memorização;
- Melhor rastreabilidade operacional.

## DA11 - Estratégias de Busca por Código e Título

### Contexto

Títulos podem se repetir ou apresentar semelhanças, enquanto códigos são únicos.

### Decisão

Permitir que buscas por título retornem múltiplas obras e que buscas por código retornem apenas uma obra.

### Consequências

- Comportamento alinhado ao domínio;
- Consultas mais previsíveis;
- Maior precisão na localização de obras.

## DA12 - Utilização do MySQL

### Contexto

Era necessário introduzir persistência permanente ao sistema.

### Decisão

Utilizar MySQL como mecanismo de armazenamento da aplicação.

### Consequências

- Persistência durável dos dados;
- Aproveitamento do conhecimento prévio da tecnologia;
- Possibilidade futura de substituição por outras engines.

## DA13 - Estante como Ponto de Entrada do Domínio

### Contexto

A Estante concentra as regras relacionadas à coleção de obras.

Permitir inserções diretas na persistência deslocaria responsabilidades de domínio para o Repository.

### Decisão

Toda inclusão de obras deve passar pela Estante antes de qualquer operação de persistência.

### Consequências

- Validações permanecem centralizadas no domínio;
- O Repository não assume responsabilidades de negócio;
- Objetos persistidos já chegam validados à camada de persistência.
