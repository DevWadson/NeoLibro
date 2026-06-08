# Camadas da Aplicação

## GUI

Responsável pela interação com o usuário.

### Responsabilidades

- Receber a entrada do usuário;
- Exibir informações solicitadas;
- Conversar com o Serviço.

### Componentes

- Components
- Forms
- Layout

## Application

Responsável pela orquestração dos casos de uso.

### Responsabilidades

- Coordenar as operações;
- Validar fluxos;
- Intermediar Domínio e Infraestrutura.

### Componentes

- services

## Core

Responsável pelo Domínio.

### Responsabilidades

- Manter integridade do domínio;
- Aplicar regras de negócio;
- Representar entidades.

### Componentes

- models

## Infra

Responsável pela persistência.

### Responsabilidades

- Armazenar os dados;
- Recuperar os dados.

### Componentes

- Database
- Repository
