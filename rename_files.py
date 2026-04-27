import pandas as pd
from pathlib import Path

def executar_processo_renomeacao(caminho_pasta, dataframe):
    sucessos = 0
    erros = 0
    caminho_pasta = Path(caminho_pasta)

    for _, linha in dataframe.iterrows():
        antigo = linha['Nome Atual']
        novo = linha['Novo Nome']
        
        if pd.notna(novo) and antigo != novo:
            p_antigo = caminho_pasta / antigo
            p_novo = caminho_pasta / novo
            
            try:
                if p_antigo.exists():
                    p_antigo.rename(p_novo)
                    sucessos += 1
            except Exception as e:
                print(f"Erro ao renomear {antigo}: {e}")
                erros += 1
                
    return sucessos, erros