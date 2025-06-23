# Projeto: Lista de Tarefas (Todo List) com Django

[cite_start]Este é um projeto de uma aplicação web de Lista de Tarefas (Todo List) desenvolvido como parte da avaliação de aprendizado. A aplicação permite ao usuário gerenciar suas tarefas diárias de forma simples e intuitiva.

## Funcionalidades Implementadas

[cite_start]O projeto cumpre com todos os requisitos obrigatórios:

* [cite_start]**Adicionar Novas Tarefas:** Funcionalidade implementada para que o usuário possa inserir novas tarefas na lista.
* **Visualizar Todas as Tarefas:** A página principal exibe todas as tarefas pendentes e concluídas.
* [cite_start]**Editar Tarefas:** Permite que o usuário modifique o título e o status (concluída ou não) de uma tarefa existente.
* [cite_start]**Atualizar Tarefas:** As edições são salvas e refletidas no banco de dados e na interface.
* [cite_start]**Deletar Tarefas:** O usuário pode remover permanentemente uma tarefa da lista.
* [cite_start]**Interface Agradável:** A interface foi estilizada com **Bootstrap** [cite: 8][cite_start], garantindo uma experiência de uso clara e organizada em diferentes dispositivos.

---

## Tecnologias Utilizadas

* **Backend:** Python 3, Django 4+
* [cite_start]**Frontend:** HTML5, CSS3, Bootstrap 5 
* **Banco de Dados:** SQLite 3 (padrão de desenvolvimento do Django)
* **Controle de Versão:** Git & GitHub

---

## Como Executar o Projeto Localmente

Siga as instruções abaixo para rodar o projeto em sua máquina.

### Pré-requisitos

* Python 3.8 ou superior
* Git

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/JoaoGln/TodoList_Django
    cd TodoList_Django
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas Python necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    Este comando cria as tabelas no arquivo `db.sqlite3`.
    ```bash
    python manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

6.  **Acesse a aplicação:**
    Abra seu navegador e acesse: `http://127.0.0.1:8000/`

---

## Autor

**[João Gabriel Leite Neirelli]**