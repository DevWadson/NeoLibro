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

## DA14 - Utilização de CustomTkinter

### Contexto
Era necessário escolher uma biblioteca para a interface gráfica.

### Decisão
Utilizar CustomTkinter como biblioteca de interface.

### Consequências

- Aproveitamento do conhecimento prévio;
- Interface moderna sem configuração adicional.

## DA15 - Layout com grid() na estrutura principal

### Contexto

Versões anteriores utilizavam pack() para estruturar o layout principal, criando dependência de ordem de empacotamento.

### Decisão

Utilizar grid() na janela principal e nos frames de layout. pack() permanece permitido dentro de componentes internos.

### Consequências

- Posicionamento explícito e estável;
- Layout previsível independente da ordem de declaração.

## DA16 - Remoção da ViewArea

### Contexto

Versões anteriores possuíam um terceiro frame (ViewArea) no rodapé sem responsabilidade clara.

### Decisão

Remover a ViewArea e centralizar todo o conteúdo dinâmico na MainArea.

### Consequências

- Estrutura mais simples;
- Responsabilidades mais bem definidas.

## DA17 - Paginação em Ver Estante

### Contexto

Exibir todas as obras de uma vez pode sobrecarregar a interface conforme o volume cresce.

### Decisão

Paginar a exibição da estante.

### Consequências

- Interface estável independente do volume de obras.

## DA18 - Botões do menu delegam renderização à MainArea

### Contexto

Os botões do menu precisam provocar mudanças no conteúdo exibido na MainArea. Na v5, o botão construía o conteúdo diretamente no frame de referência.

### Decisão

O botão não constrói conteúdo. Ao ser clicado, chama um método da MainArea via referência direta. A MainArea é responsável por construir e gerenciar o próprio conteúdo.

### Consequências

- MainArea cresce um método por ação do menu;
- O botão fica simples e sem conhecimento de layout.

## DA19 - Botões do menu herdam CTkButton

### Contexto

Cada botão do menu poderia ser uma instância direta de CTkButton criada por MenuArea, ou uma classe própria.

### Decisão

Botões do menu herdam CTkButton. A herança se justifica pela existência de função característica própria (_on_click), não apenas configuração.

### Consequências

- Cada botão do menu é uma classe em src/gui/components/;
- Botões sem comportamento próprio não justificam essa herança.

## DA20 - Referência à MainArea injetada via construtor

### Contexto

O botão precisa de uma referência à MainArea para disparar o método correspondente.

### Decisão

A referência é recebida no construtor. Window instancia o botão passando main_area explicitamente.

### Consequências

- O botão está pronto para uso desde a inicialização, sem necessidade de configuração posterior.

## DA21 - _available_map pertence ao __init__ da MainArea

### Contexto

MainArea mantém um mapeamento de tipos de obra para seus formulários correspondentes.

### Decisão

_available_map é inicializado no __init__, não recriado a cada chamada de método. É um mapeamento fixo do ciclo de vida da instância.

### Consequências

- O mapeamento é criado uma vez;
- Métodos que o utilizam apenas leem, não recriam.

## DA22 - Relação de imports entre camadas

### Contexto

Imports diretos a submódulos internos de outra camada criam acoplamento à organização interna do pacote. Qualquer refatoração interna — renomear um módulo, mover um arquivo — propaga quebras para quem importa. Sem uma regra explícita, esse padrão tende a se espalhar silenciosamente.

### Decisão

Imports entre camadas devem acessar somente a API pública da camada, exposta pelo __init__.py. Subpacote direto só é válido se declarado como API pública no __init__ do pacote pai. Import até o módulo sempre viola.

```python
from src.camada import X                    # correto
from src.camada.subpacote import X          # viola, exceto se declarado no __init__ do pacote pai
from src.camada.subpacote.modulo import X   # viola sempre
```

### Consequências

- Refatorações internas de uma camada não propagam para outras;
- A API pública de cada camada é explícita e controlada pelo __init__.py.
