import pandas as pd
import json
import os
import requests
from dotenv import load_dotenv

# Carrega variáveis de ambiente (como a chave da API do OpenAI se houver)
load_dotenv()

def extract_data(file_path):
    """
    [E] EXTRAÇÃO: Obtém dados de um arquivo CSV.
    Poderia ser adaptado para uma API (requests.get(url)).
    """
    print(f"\n[EXTRACT] Lendo arquivo: {file_path}")
    try:
        # Lendo o CSV simulando a extração de dados brutos
        df = pd.read_csv(file_path)
        print(f"[EXTRACT] Sucesso! {len(df)} registros extraídos.")
        return df
    except FileNotFoundError:
        print(f"[EXTRACT] Erro: Arquivo {file_path} não encontrado.")
        return None
    except Exception as e:
        print(f"[EXTRACT] Erro inesperado: {e}")
        return None

def generate_ai_message(user_name, card_type):
    """
    [T] TRANSFORMAÇÃO: Simula o uso de IA Generativa.
    No mundo real, aqui chamaríamos a API da OpenAI ou Google Gemini.
    """
    # Lógica de "IA" simulada para mensagens personalizadas
    # Se você tiver uma chave da OpenAI, descomente o bloco abaixo e use a biblioteca openai
    
    # import openai
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "system", "content": "Você é um assistente de marketing bancário."},
    #               {"role": "user", "content": f"Crie uma frase de 1 linha para o cliente {user_name} sobre o cartão {card_type}."}]
    # )
    # return response.choices[0].message.content

    # Simulação local (Demonstrativo para o desafio DIO)
    mensagens = {
        "Gold": f"Olá {user_name}, seu cartão Gold te dá 1.5% de cashback hoje!",
        "Platinum": f"Olá {user_name}, o acesso à Sala VIP está liberado para o seu Platinum.",
        "Black": f"Olá {user_name}, o limite do seu cartão Black foi expandido. Aproveite!",
        "Silver": f"Olá {user_name}, confira os descontos exclusivos no Shopping com seu Silver.",
        "Basic": f"Olá {user_name}, que tal fazer um upgrade do seu cartão Basic hoje?"
    }
    
    return mensagens.get(card_type, f"Olá {user_name}, temos ofertas especiais para você!")

def transform_data(df):
    """
    [T] TRANSFORMAÇÃO: Processa os dados e gera as mensagens.
    """
    print("[TRANSFORM] Iniciando processamento com IA Generativa...")
    if df is None:
        return None
    
    # Aplicando a função de geração de mensagem para cada linha do DataFrame
    df['Message'] = df.apply(lambda row: generate_ai_message(row['Name'], row['CardType']), axis=1)
    
    print("[TRANSFORM] Transformação concluída.")
    return df

def load_data(df, output_path):
    """
    [L] CARREGAMENTO: Salva os dados transformados em um arquivo JSON/CSV.
    """
    print(f"[LOAD] Salvando dados processados em: {output_path}")
    if df is None:
        return
    
    try:
        # Salvando em formato JSON para um resultado mais estruturado
        result = df.to_dict(orient='records')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        
        # Também poderíamos salvar em CSV se preferir:
        # df.to_csv('users_with_messages.csv', index=False)
        
        print(f"[LOAD] Arquivo final gerado com sucesso!")
    except Exception as e:
        print(f"[LOAD] Erro ao salvar arquivo: {e}")

def main():
    """
    Função principal que orquestra o pipeline ETL.
    """
    print("="*40)
    print("      PIPELINE ETL COM IA - DIO")
    print("="*40)
    
    # 1. Extração
    users_df = extract_data('users.csv')
    
    # 2. Transformação
    transformed_df = transform_data(users_df)
    
    # 3. Carregamento
    load_data(transformed_df, 'users_with_messages.json')
    
    print("\n[DONE] Projeto finalizado!")

if __name__ == "__main__":
    main()