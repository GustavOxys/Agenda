markdown
Copiar código
# Agenda de Contatos

Este é um projeto de agenda de contatos desenvolvido com Django, como parte do curso do Luiz Otávio Miranda. O objetivo do projeto é permitir que os usuários se registrem, façam login e gerenciem seus contatos de forma simples e eficiente.

## Funcionalidades

- **Registro e Login**: Os usuários podem se registrar e fazer login na aplicação.
- **Gerenciamento de Contatos**: Os usuários podem criar, editar e excluir contatos.
- **Informações do Contato**:
  - Nome
  - Sobrenome
  - Telefone
  - Email
  - Foto do contato
- **Sistema de Pesquisa**: Os usuários podem pesquisar contatos pelo nome, telefone ou email.
- **Compartilhamento de Dados**: Todos os contatos são compartilhados entre os usuários que fizerem login.

## Tecnologias Utilizadas

- Django
- Python
- HTML/CSS
- Banco de dados (PostgreSQL)

## Instalação

Para rodar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/GustavOxys/Agenda.git
Navegue até o diretório do projeto:

bash
Copiar código
cd agenda
Crie um ambiente virtual e ative-o:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Faça as migrações do banco de dados:

bash
Copiar código
python manage.py migrate
Inicie o servidor:

bash
Copiar código
python manage.py runserver
Acesse a aplicação em http://127.0.0.1:8000

Contribuições
Sinta-se à vontade para fazer um fork do projeto e contribuir com melhorias!

Licença
Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

Agradecimentos
Agradeço ao Luiz Otávio Miranda pelo excelente curso que me ajudou a desenvolver este projeto.