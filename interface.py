import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pandas as pd
from pathlib import Path

# Importamos o motor que você criou
from rename_files import executar_processo_renomeacao

class RenomeadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Renomeador Pro - Engenharia")
        self.root.geometry("500x250")

        tk.Label(root, text="Caminho da Pasta:", font=("Arial", 10, "bold")).pack(pady=10)
        
        self.frame_busca = tk.Frame(root)
        self.frame_busca.pack(padx=20, fill='x')

        self.entrada_caminho = tk.Entry(self.frame_busca)
        self.entrada_caminho.pack(side='left', expand=True, fill='x', padx=(0, 5))

        self.btn_buscar = tk.Button(self.frame_busca, text="Buscar", command=self.selecionar_pasta)
        self.btn_buscar.pack(side='right')

        self.btn_gerar = tk.Button(root, text="1. GERAR LISTA NO EXCEL", bg="#28a745", fg="white", 
                                   font=("Arial", 10, "bold"), command=self.gerar_excel)
        self.btn_gerar.pack(pady=20)

        self.btn_renomear = tk.Button(root, text="2. EXECUTAR RENOMEAÇÃO AGORA", bg="#007bff", fg="white", 
                                      font=("Arial", 10, "bold"), command=self.finalizar)
        # O botão começa escondido

    def selecionar_pasta(self):
        caminho = filedialog.askdirectory()
        if caminho:
            self.entrada_caminho.delete(0, tk.END)
            self.entrada_caminho.insert(0, caminho)

    def gerar_excel(self):
        diretorio = self.entrada_caminho.get()
        if not os.path.isdir(diretorio):
            messagebox.showerror("Erro", "Selecione uma pasta válida.")
            return

        folder = Path(diretorio)
        arquivos = [f.name for f in folder.iterdir() if f.is_file() and f.name != "_lista_para_renomear.xlsx"]
        
        df = pd.DataFrame({'Nome Atual': arquivos, 'Novo Nome': arquivos})
        self.caminho_excel = folder / "_lista_para_renomear.xlsx"
        
        try:
            df.to_excel(self.caminho_excel, index=False)
            os.startfile(self.caminho_excel)
            self.btn_renomear.pack(pady=10)
            messagebox.showinfo("Excel Gerado", "Edite, salve e feche o Excel antes de prosseguir.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")

    def finalizar(self):
        try:
            # 1. Tenta ler o arquivo Excel que o usuário editou
            df = pd.read_excel(self.caminho_excel)
            
            # 2. Chama o motor para renomear os arquivos reais
            sucessos, erros = executar_processo_renomeacao(self.entrada_caminho.get(), df)
            
            # 3. MENSAGEM DE SUCESSO
            messagebox.showinfo("Fim", f"Concluído!\nSucessos: {sucessos}\nErros: {erros}")
            
            # 4. DELEÇÃO AUTOMÁTICA: O Python apaga o arquivo temporário aqui
            if self.caminho_excel.exists():
                os.remove(self.caminho_excel)
                print(f"Arquivo temporário {self.caminho_excel.name} removido.")

            self.btn_renomear.pack_forget()
            
        except PermissionError:
            # Se o usuário clicar no botão mas o Excel ainda estiver aberto, 
            # o Windows não deixa o Python ler nem deletar o arquivo.
            messagebox.showerror("Erro de Permissão", "O Excel ainda está aberto! Salve e feche o arquivo antes de clicar em Renomear.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um problema: {e}")