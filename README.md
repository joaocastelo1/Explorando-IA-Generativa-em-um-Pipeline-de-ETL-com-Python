# 🚀 Pipeline ETL com IA Generativa em Python

Este projeto foi desenvolvido como parte do desafio da plataforma **DIO (Digital Innovation One)**: *"Explorando IA Generativa em um Pipeline de ETL com Python"*.

O objetivo é demonstrar o ciclo de vida completo de um processo **ETL (Extract, Transform, Load)**, integrando o poder da Inteligência Artificial para gerar valor aos dados.

## 📌 Objetivo do Projeto

Construir um pipeline que:
1.  **Extract (Extração):** Lê dados de clientes a partir de um arquivo CSV.
2.  **Transform (Transformação):** Utiliza lógica de IA Generativa para criar mensagens de marketing personalizadas para cada cliente, baseando-se no tipo de cartão de crédito.
3.  **Load (Carregamento):** Salva os dados enriquecidos em um arquivo JSON estruturado.

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3.12+
-   **Manipulação de Dados:** `pandas`
-   **Ambiente:** `python-dotenv` para gestão de chaves de API.
-   **IA Generativa:** Mock de IA (com estrutura pronta para integração com OpenAI/Gemini).

## 📂 Estrutura do Projeto

-   `etl_pipeline.py`: O "coração" do projeto, contendo as funções de cada etapa do ETL.
-   `users.csv`: Arquivo de entrada com dados fictícios de clientes.
-   `users_with_messages.json`: O resultado final após o processamento.
-   `requirements.txt`: Lista de dependências do projeto.

## 🚀 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure a API (Opcional):**
    Crie um arquivo `.env` e adicione sua chave:
    ```env
    OPENAI_API_KEY=sua_chave_aqui
    ```

4.  **Execute o pipeline:**
    ```bash
    python etl_pipeline.py
    ```

## 🤖 O Papel da IA Generativa

Na etapa de **Transformação**, o script simula uma chamada a um modelo de linguagem (LLM). Dependendo do perfil do cliente (tipo de cartão), a "IA" gera uma mensagem única e atrativa, simulando uma campanha de marketing hiper-personalizada.

---
⭐ **Diferenciais deste Portfolio:**
- Código limpo e modularizado em funções.
- Tratamento de exceções robusto.
- Documentação clara e profissional.
- Estrutura pronta para produção.

---
Desenvolvido por [Seu Nome](https://github.com/seu-usuario) no desafio da DIO.