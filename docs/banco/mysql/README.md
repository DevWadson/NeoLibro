# MySQL

Esta pasta contém os artefatos relacionados à implementação física do banco de dados do NeoLibro.

A implementação foi realizada utilizando MySQL, tecnologia adotada como mecanismo de persistência do sistema.

## Estrutura

mysql/

>>├── diagramas/

>> └── scripts/

## `diagramas/`

Contém diagramas exportados para consulta rápida da estrutura do banco de dados.

Esses diagramas possuem finalidade documental e auxiliam na compreensão da modelagem sem a necessidade de abrir os arquivos do BRModelo.

## `scripts/`

Contém os scripts SQL utilizados na criação e manutenção da estrutura do banco de dados.

### Exemplos

- Criação de tabelas;
- Alterações de esquema;
- Carga de dados para teste;
- Scripts auxiliares.

## Relação com a Arquitetura

O MySQL atua como mecanismo de persistência da aplicação.

O acesso ao banco ocorre exclusivamente através da camada Repository, mantendo o domínio isolado dos detalhes de infraestrutura.
