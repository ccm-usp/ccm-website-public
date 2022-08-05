# Dados públicos para [cecm.usp.br](http://www.cecm.usp.br)

## Propósito
Entregar dados dinâmicos para [cecm.usp.br](http://www.cecm.usp.br) utilizando GitHub CDN Pages.

## Acesso
Todos estudantes do Curso de Ciências Moleculares estão convidados a contribuir com as informações deste repositório, que é moderado por estudantes voluntários para garantir a qualidade dos dados e imagens.

## Como contribuir?
Basta criar seu próprio fork do repositório, incluir seus dados e efetuar um [Pull Request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

## Especificações dos Dados
Os dados neste repositório devem ser incluídos em um formato pré-definido para que sejam corretamente exibidos em [cecm.usp.br](http://www.cecm.usp.br). Pull Requests só serão aceitos se seguirem _todas_ as especificações abaixo.

### Páginas Pessoais

**Imagem da Página Pessoal:** São dois arquivos `.jpg`, seguindo as seguintes regras:
| Nome  | Resolução | Tamanho Máximo |
| -------------  | ------------- | ------------- |
| `nome-sem-espacos-e-acentos.jpg` | 272 × 272 pixels | 50kb |
| `nome-sem-espacos-e-acentos@2x.jpg` | 544 × 544 pixels  | 100kb |

Você pode usar ferramentas gratuitas como o [Gimp ](https://www.gimp.org/) (Linux | OS X | Windows) ou o [PhotoPea ](https://www.photopea.com/) (Online) para garantir o tamanho e resolução.

**Dados da Página Pessoal:**  Um `.json` nomeado pelo nome do estudante, onde os espacos sao substituidos por "-" (`nome-sem-espaco.json`) e sem acentos com os seguintes objetos:
```
nome - string
turma - string (ANO)
especializacao - array of strings
concentracao - array of strings
origem - string (CURSO)
conteudo - array of strings
avancado - array of strings
extracurricular - array of objects
    title - string
    link - string
conquistas - array of strings
avancado - array of strings
contato - object
    email - string
    lattes - string
    linkedin - string
    github - string
    site - string
    behance - string
    telefone - string
hasPhoto - bool
```

*Nota:* Você pode deixar qualquer campo em branco, exceto pelo seu nome e turma. O site irá dinamicamente adaptar o design da página de acordo com as informações que você fornecer. Remova as linhas não utilizadas do seu .json.

*Nota 2:* Área de Concetração deve seguir [areas-concentracao.md](/areas-concentracao.md).

*Nota 3:* Tem um template chamado [template.json](/template.json) na raiz do repositório para facilitar sua vida!

**PDFs do Avançado:** Devem ser incluídos em formato .pdf, com nome seguindo a regra `nome-sem-espaco-0.pdf`. O número no final do arquivo indica a ordem dos arquivos que serão associados à lista de projetos do avançado que você forneceu no `.json`acima.

**Importante:** Seu nome em seus arquivos pessoais deve ser o mesmo especificado na lista `.json` de estudantes da sua turma, porém, todo minúsculo e com espaços substitutidos por `-`.

### Filtros
**Assim que o seu pull request for commitado, uma action será executada automaticamente e te adicionará nos resultados dos filtros.**

Se você deseje fazer isso manualmente, você deve adicionar seu nome na área correspondente em `./filtros/especializacao/results` ou `./filtros/concentracao/results`.

Caso sua área não exista ainda, basta criar um arquivo `nome-sem-espaco-e-acento.json`, incluir seu nome. Em seguida, adicione o nome da área no arquivo `especializacao.json` ou ` concentracao.json` (em ordem alfabética).

### Páginas das Turmas
**Turma Ingressante:** Os dados da turma ingressante devem ser incluídos somente após o fim da exibição da página de aprovados, que é removida após 1 mês da última `date_active` em `datas_selecao.json`

**Imagem Principal:** São dois arquivos `.jpg`, seguindo as seguintes regras:
| Nome  | Resolução | Tamanho Máximo |
| -------------  | ------------- | ------------- |
| `ANO_DA_TURMA.jpg` | 876 × 300 pixels | 100kb |
| `ANO_DA_TURMA@2x.jpg` | 1751 × 600 pixels  | 360kb |

Você pode usar ferramentas gratuitas como o [Gimp ](https://www.gimp.org/) (Linux | OS X | Windows) ou o [PhotoPea ](https://www.photopea.com/) (Online) para garantir o tamanho e resolução.
 
**Lista de Estudantes:** Um `.json` nomeado pelo ano de ingresso da turma com os seguintes objetos:

```
estudantes - array of objects
    nome - string
    hasPage - bool
hasPhotos - bool
hasMainPhoto - bool
institutos - bool
```

### Datas do Processo Seletivo
As datas do processo seletivo são governadas por `datas_selecao.json`. O website atualiza seu conteúdo dinâmicamente de acordo com as datas registradas neste arquivo.

`date_active` _data em que o estado será ativado no website_

`date_content` _data da fase do processo em questão para ser utilizada na redação do site_

### Lista de Aprovados
Localizada no endereço [cecm.usp.br/aprovados ](http://cecm.usp.br/aprovados/). Basta carregar o arquivo aprovados.json com as informações dos estudantes. A página entra no ar no último `date_active` em `datas_selecao.json` e sai do ar automáticamente após 1 mês.
