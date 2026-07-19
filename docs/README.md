# NeoLibro

## Sobre o Projeto

NeoLibro é um sistema para gerenciamento de obras literárias, desenvolvido para organizar coleções de HQs, Livros e Mangás. Atualmente, o sistema reflete a coleção do próprio autor.

O projeto surgiu inicialmente como uma necessidade pessoal de catalogação de obras e evoluiu gradualmente para um estudo prático de desenvolvimento de software, modelagem, arquitetura e boas práticas.

## Funcionalidades

Atualmente o sistema permite:

- Cadastro de obras;
- Consulta de obras cadastradas;
- Persistência de dados utilizando MySQL;
- Geração automática de códigos de rastreabilidade.

## Tecnologias Utilizadas

- uv
- Python
- BRModelo
- MySQL
- CustomTkinter

## Documentação

A documentação do projeto encontra-se no diretório `docs/`.

Principais tópicos documentados:

- [`Arquitetura`](arquitetura/);
- [`Decisões Arquiteturais`](arquitetura/decisoes.md);
- [`Banco de Dados`](banco/);
- [`Fluxos`](fluxos/);
- [`GUI`](gui/);
- [`Requisitos Funcionais`](requisitos/funcionais.md);
- [`Requisitos Não-Funcionais`](requisitos/nao_funcionais.md);
- [`Regras de Negócio`](requisitos/regras_negocio.md).

---

## Como Rodar Localmente

1. Clone o repositório

No terminal da sua máquina

```markdown
​git clone https://github.com/<seu-usuario>/NeoLibro.git

cd NeoLibro​
```

2. Instale as dependências com `uv`:

```markdown
uv sync
```

3. Configure o banco de dados: crie um arquivo `.env` na raiz do projeto com as credenciais do MySQL:

```markdown
​DEBUG=TRUE

ACTIVE_DB=mysql

USER=<seu-usuario-mysql>
PWRD=<sua-senha>
HOST=127.0.0.1
DB_NAME=neolibro_db
```

4. Execute o script `docs/banco/mysql/scripts/neolibro_db.sql` no seu cliente MySQL para criar o banco.

5. Rode a aplicação:

```markdown
uv run python -m src.main
```

## Como Contribuir

1. Clone o repositório do projeto.
2. Instale as dependências com `uv sync`.
3. Adicione novas funcionalidades ou corrija bugs, mantendo o padrão de documentação.
4. Envie um pull request para revisão.

## Autor

Desenvolvido por Marlon Wadson.

Contato: marlonwadson.dev@gmail.com
