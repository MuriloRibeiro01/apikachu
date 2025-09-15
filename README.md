# Ϟ PokéAPI Explorer com Python Ϟ

![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/requests-library-orange.svg?style=for-the-badge)

Um simples e divertido script em Python que consome a [PokéAPI](https://pokeapi.co/) para buscar e exibir informações detalhadas sobre qualquer Pokémon.

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como um exercício prático para aprimorar as habilidades de consumo de APIs RESTful com Python. A aplicação permite que o usuário insira o nome de um Pokémon e retorna dados relevantes como número da Pokédex, altura, peso e habilidades, tratando os dados recebidos no formato JSON.

O foco foi criar um código limpo, com tratamento básico de erros (como Pokémon não encontrado) e uma interação amigável com o usuário via terminal.

## ✨ Funcionalidades

-   Busca de Pokémon por nome.
-   Exibição de dados formatados (Nome, ID, Altura, Peso, Habilidades).
-   Tratamento de resposta para casos de sucesso (`200 OK`) e de falha (`404 Not Found`).

## 🛠️ Tecnologias Utilizadas

-   **Python:** Linguagem principal do projeto.
-   **Biblioteca `requests`:** Para realizar as requisições HTTP de forma simples e eficiente.
-   **Biblioteca `json`:** Para manipulação e exibição dos dados recebidos da API.

## 🚀 Como Usar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MuriloRibeiro01/api-pokemon-python.git](https://github.com/MuriloRibeiro01/api-pokemon-python.git)
    cd api-pokemon-python
    ```

2.  **Instale as dependências:**
    ```bash
    pip install requests
    ```

3.  **Execute o script:**
    ```bash
    python app.py
    ```
4.  Siga as instruções no terminal e divirta-se capturando seus Pokémons!