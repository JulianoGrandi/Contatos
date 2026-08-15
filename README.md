# 📇 Contatos

Um gerenciador de contatos simples, feito em Python e executado via linha de comando (CLI).

## 📌 Sobre o projeto

Este é um script Python que permite cadastrar, visualizar, editar e excluir contatos diretamente pelo terminal, com suporte para marcar contatos como favoritos (exibidos com ★ e listados primeiro).

> ⚠️ Os contatos ficam armazenados apenas em memória durante a execução do programa. Ao fechar o script, os dados são perdidos — não há persistência em arquivo ou banco de dados.

## ✨ Funcionalidades

- ➕ Adicionar um novo contato (nome, telefone, email e se é favorito)
- ⭐ Visualizar apenas os contatos favoritos
- 📋 Visualizar todos os contatos (favoritos aparecem no topo da lista)
- ✏️ Editar um contato existente (nome, telefone, email, status de favorito ou tudo de uma vez)
- 🗑️ Excluir um contato

## 🛠️ Tecnologias

- [Python](https://www.python.org/) 3.12+

## ✅ Pré-requisitos

- Python 3.12 ou superior instalado na máquina (o script usa aspas aninhadas dentro de f-strings, um recurso disponível a partir do Python 3.12).

## 🚀 Como executar

```bash
# Clone o repositório
git clone https://github.com/JulianoGrandi/Contatos.git

# Acesse a pasta do projeto
cd Contatos

# Execute o script
python gerenciador.py
```

## 📖 Como usar

Ao rodar o script, um menu interativo é exibido no terminal:

```
lista de Contatos

1. Adcionar contatos
2. Ver contatos Favoritos
3. Ver contatos
4. Editar contatos
5. Excluir contatos
0. Sair
```

Basta digitar o número da opção desejada e seguir as instruções exibidas. O programa já inicia com alguns contatos de exemplo cadastrados.

## 📁 Estrutura do projeto

```
Contatos/
└── gerenciador.py   # script único com toda a lógica do gerenciador
```

## 🔧 Possíveis melhorias futuras

- Persistir os contatos em um arquivo (JSON/CSV) ou banco de dados
- Validar as entradas do usuário (ex.: formato de telefone e email)
- Adicionar tratamento de exceções para entradas inválidas
- Separar o código em módulos/funções organizadas em um pacote

## 👤 Autor

Desenvolvido por [Juliano Grandi](https://github.com/JulianoGrandi).
