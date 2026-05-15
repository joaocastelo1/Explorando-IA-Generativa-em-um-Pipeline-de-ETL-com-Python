# 🚀 Pipeline ETL com IA Generativa em Python

Este projeto foi desenvolvido como parte do desafio da plataforma **DIO (Digital Innovation One)**: *"Explorando IA Generativa em um Pipeline de ETL com Python"*.

O objetivo é demonstrar o ciclo de vida completo de um processo **ETL (Extract, Transform, Load)**, integrando o poder da Inteligência Artificial para gerar valor real aos dados.

## 📌 Objetivo do Projeto

Construir um pipeline funcional que realiza:
1.  **Extract (Extração):** Leitura de dados de clientes a partir de um arquivo CSV de forma eficiente.
2.  **Transform (Transformação):** Aplicação de lógica de IA Generativa para conceber mensagens de marketing personalizadas para cada cliente, adaptadas ao perfil do seu cartão de crédito.
3.  **Load (Carregamento):** Exportação dos dados enriquecidos para um arquivo JSON estruturado, pronto para consumo por outros sistemas.

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3.12+
-   **Manipulação de Dados:** `pandas`
-   **Ambiente:** `python-dotenv` para gestão segura de credenciais e chaves de API.
-   **IA Generativa:** Estrutura modular preparada para integração com OpenAI ou Gemini (atualmente utilizando Mock para testes de fluxo).

## 📂 Estrutura do Projeto

-   `etl_pipeline.py`: Implementação central contendo as funções de cada etapa do processo.
-   `users.csv`: Base de dados de entrada com perfis fictícios para demonstração.
-   `users_with_messages.json`: Output final contendo os dados processados e as mensagens geradas.
-   `requirements.txt`: Dependências necessárias para a execução do ambiente.

## 🚀 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/joaocastelo1/Explorando-IA-Generativa-em-um-Pipeline-de-ETL-com-Python.git](https://github.com/joaocastelo1/Explorando-IA-Generativa-em-um-Pipeline-de-ETL-com-Python.git)
    cd Explorando-IA-Generativa-em-um-Pipeline-de-ETL-com-Python
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure a API (Opcional):**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave:
    ```env
    OPENAI_API_KEY=sua_chave_aqui
    ```

4.  **Execute o pipeline:**
    ```bash
    python etl_pipeline.py
    ```

## 🤖 O Papel da IA Generativa

Na etapa de **Transformação**, o pipeline simula a interação com um modelo de linguagem (LLM). O sistema analisa o perfil de cada cliente e gera uma abordagem de marketing hiper-personalizada, demonstrando como a IA pode escalar a comunicação individualizada em grandes bases de dados.

---
⭐ **Diferenciais deste Portfólio:**
- **Código Limpo:** Modularização seguindo boas práticas de desenvolvimento.
- **Resiliência:** Tratamento de exceções para garantir a continuidade do pipeline.
- **Documentação:** Foco na clareza técnica para facilitar a revisão e o deploy.
- **Escalabilidade:** Estrutura preparada para integração com APIs de produção.

---
Desenvolvido por **João Castelo de Sousa Ferreira** no desafio da [DIO](https://www.dio.me/).
