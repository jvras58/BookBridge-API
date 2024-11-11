## 📖 Sobre o Projeto
Este projeto é uma API desenvolvida com flask, focada no estudo e implementação dos princípios da RestFul. A documentação detalhada do que é a API pode ser encontrada [aqui](docs/docs.md).


## 🚀 Tecnologias e Ferramentas
O projeto foi criado para aprimorar conhecimentos em python, explorando suas capacidades e integração com flask e dynaconf.

### Stack do Projeto
Esta API simples utiliza python, uma linguagem multiparadigma, de tipagem dinâmica e forte, com gerenciamento automático de memória. O objetivo é demonstrar e aprender como estruturar um projeto seguindo os princípios da API RestFul.

|  Lib      | Versão    |
|-----------|-----------|
| **Runtime**           |
| Python    | v3.12.x   |
| **Devtime**           |
| Ruff                          | v0.4.x    |
| Docker Engine                 | vx.x.x    |

### Organização do projeto
```
/
├─📁 .devcontainer     ->  [Configurações do devcontainer]
├─📁 .vscode           ->  [Definições de ambiente para o VSCode]
├─📁 .secrets          ->  [Repo para artefatos de segredos da app]
├─📁 docs              ->  [Artefatos para documentação do repo]
├─📁 migrations        ->  [Artefatos de gerenciamento do banco de dados com o alembic]
├─📁 app               ->  [Implementação da aplicação]
│ │ ├─🐍 startup.py              -> Entrypoint
│ │ ├─📁 commons        ->  [Funções Auxiliares]
│ │ │  ├─🐍 utils.py             -> Arquivos utils para aplicação
│ │ │  ├─🐍 swagger.py             -> Arquivos de configuração e Documentação do Swagger
│ │ │    ...
│ │ ├─📁 config        ->  [configurações para aplicação]
│ │ │  ├─🐍 base.py              -> Arquivos de Inicialização para aplicação
│ │ │  ├─🐍 settings.py            -> Módulo de configurações do sistema
│ │ │    ...
│ │ ├─📁 database      ->  [configurações para o banco de dados]
│ │ │  ├─🐍 session.py              -> Módulo para gerenciar a sessão do banco de dados
│ │ │    ...
│ │ ├─📁 models        ->  [Modelos para o banco de dados]
│ │ │  ├─🐍 user.py              -> Módulo para modelo User
│ │ │    ...
│ │ ├─📁 resources     ->  [Contém as classes com as logicas da API]
│ │    ├─🐍 user.py              -> contêm a lógica de manipulação de usuarios
│ │    ├─🐍 user_router.py       -> contêm a lógica das rotas que define o Blueprint
│ │ ...
├─📄 .gitignore
├─📄 Makefile          ->  Automações para o ambiente
├─📄 pyproject.toml    ->  Definições para o projeto
├─📄 settings.toml     ->  Configurações do ambiente com o FlaskDynaconf
├─📄 README.MD
```

## Montando o ambiente

Este repositório esta organizando em um devcontainer.
E para instacia-lo no VSCODE é recomendado as seguintes configurações:

#### Extenções recomendadas

- Name: Remote Development
- Id: ms-vscode-remote.vscode-remote-extensionpack
- Description: An extension pack that lets you open any folder in a container, on a remote machine, or in WSL and take advantage of VS Code's full feature set.
- Version: 0.25.0
- Publisher: Microsoft
- VSCode Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack

#### Docker Engine

É obrigatório ter o Docker Engine já instalado e cunfigurado. Para mais informações de como instalar o Docker Engine em seu SO, ver em:

- Instruções para instalação do Docker Engine: [Ver o link](https://docs.docker.com/engine/install/)

#### Procedimento para instanciar o projeto no VSCODE
1. Com o pack de extenções instalado,
1. Realize o clone/fork deste repositório,
1. Abra o diretorio deste repositorio no VSCODE como um projeto,
1. Use o Comando _Dev Containers: Reopen in Container_ da paleta de comandos do VSCODE. _(F1, Ctrl+Shift+P)_.

Depois da compilação do container o VSCode abrirá o repositório em um ambiente encapsulado e executando diretamente de dentro do container como configurado nas definições do **/.devconainer**.

#### Procedimento para iniciar
1. inicie o ambiente virtual do poetry && instale as dependencias definidas no pyproject.toml
```
$> make venv
```

- Pronto agora voce esta pronto para começar a usar!

### Principais comandos:

### iniciar banco:
```
$> make upgrade 
```

#### Levantar a aplicação
```
$> make dev 
```

#### Adcionar novas dependencias
```
# Adicionar uma nova lib para o runtime do projeto
$> poetry add <<nome_da_lib>>

# Adicionar uma nova lib para o ambiente de desenvolvimento
$> poetry add <<nome_da_lib>> --group dev
```

### Alguns comandos interessantes no Makefile se precisar:
Para ver todos os comandos disponíveis no Makefile, clique [aqui](Makefile).
