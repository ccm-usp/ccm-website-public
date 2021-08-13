# Dados públicos para [cecm.usp.br](cecm.usp.br)

## Propósito
Entregar dados dinâmicos para [cecm.usp.br](cecm.usp.br) utilizando GitHub CDN Pages.

## Acesso
Todos estudantes do Curso de Ciências Moleculares estão convidados a contribuir com as informações alimentadas por este repositório, que é moderado por estudantes atuais voluntários para garantir a qualidade dos dados e imagens.

## Como contribuir?
Basta criar seu próprio fork do repositório, incluir seus dados e efetuar um [Pull Request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

## Especificações dos Dados
Os dados neste repositório devem ser incluídos em um formato pré-definido para que sejam corretamente exibidos em [cecm.usp.br](cecm.usp.br). Pull Requests só serão aceitos se seguirem _todas_ as especificações abaixo.

### Datas do Processo Seletivo
As datas do processo seletivo são governadas por `datas_selecao.json`. O website atualiza seu conteúdo dinâmicamente de acordo com as datas registradas neste arquivo.
`date_active` _data em que o estado será ativado no website_
`date_content` _data da fase do processo em questão para ser utilizada na redação do site_

### Páginas das Turmas
**Turma Ingressante:** Os dados da turma ingressante devem ser incluídos somente após o fim da exibição da página de aprovados, que é removida após 1 mês da última `date_active` em `datas_selecao.json`

**Imagem Principal:** São dois arquivos `.jpg`, seguindo as seguintes regras:
| Nome  | Resolução | Tamanho Máximo |
| -------------  | ------------- | ------------- |
| `XXXX.jpg` | 876 × 300 pixels | 100kb |
| `XXXX@2x.jpg` | 1751 × 600 pixels  | 360kb |

Você pode usar ferramentas gratuitas como o [Gimp ](https://www.gimp.org/) (Linux | OS X | Microsoft Windows) ou o [PhotoPea ](https://www.photopea.com/) (Online) para garantir o tamanho e resolução.
 
**Lista de Estudantes:** Um `.json` nomeado pelo ano de ingresso da turma com os seguintes objetos:

`estudantes` - _array of objects_

> `nome` - _string_
> 
> `hasPage` - _bool_

`hasPhotos` - _bool_

`hasMainPhoto` - _bool_

`institutos` - _bool_

### Páginas Pessoais

**Imagem da Página Pessoal:** São dois arquivos `.jpg`, seguindo as seguintes regras:
| Nome  | Resolução | Tamanho Máximo |
| -------------  | ------------- | ------------- |
| `nome-sem-espacos.jpg` | 272 × 272 pixels | 100kb |
| `nome-sem-espacos@2x.jpg` | 544 × 544 pixels  | 100kb |

Você pode usar ferramentas gratuitas como o [Gimp ](https://www.gimp.org/) (Linux | OS X | Microsoft Windows) ou o [PhotoPea ](https://www.photopea.com/) (Online) para garantir o tamanho e resolução.

**Dados da Página Pessoal:**  Um `.json` nomeado pelo nome do estudante, onde os espacos sao substituidos por "-" com os seguintes objetos:

`nome` - _string_

`turma` - _string_

`especializacao` - _array of strings_

`concentracao` - _array of strings_

`origem` - _string_

`conteudo` - _array of strings_

`avancado` - _array of strings_

`extracurricular` - _array of objects_

> `title` - _string_ 
> 
> `link` - _string_ 

`avancado` - _array of strings_

`extracurricular` - _object_

> `email` - _string_ 
> 
> `lattes` - _string_ 
> 
> `linkedin` - _string_ 
> 
> `github` - _string_ 
> 
> `site` - _string_ 
> 
> `behance` - _string_ 
> 
> `telefone` - _string_ 

`hasPhoto` - _bool_
