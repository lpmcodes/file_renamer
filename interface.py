import tkinter as tk
from tkinter import filedialog, messagebox
import os

def selecionar_pasta():
    # Abre o seletor de pastas do Windows
    caminho = filedialog.askdirectory()
    if caminho:
        entrada_caminho.delete(0, tk.END)
        entrada_caminho.insert(0, caminho)

def confirmar():
    caminho = entrada_caminho.get()
    if os.path.isdir(caminho):
        print(f"Pasta validada: {caminho}")
        root.destroy() # Fecha a janela para seguir com o código do Excel
        # Aqui você chamaria sua função de gerar o Excel
    else:
        messagebox.showerror("Erro", "Caminho inválido ou pasta não encontrada.")

# --- Configuração da Janela Principal ---
root = tk.Tk()
root.title("Renomeador de Documentos")
root.geometry("500x150")

# Label de instrução
tk.Label(root, text="Cole o caminho da pasta ou clique em Buscar:", font=("Arial", 10)).pack(pady=10)

# Frame para agrupar o campo de texto e o botão de busca
frame_busca = tk.Frame(root)
frame_busca.pack(padx=20, fill='x')

entrada_caminho = tk.Entry(frame_busca)
entrada_caminho.pack(side='left', expand=True, fill='x', padx=(0, 5))

btn_buscar = tk.Button(frame_busca, text="Buscar...", command=selecionar_pasta)
btn_buscar.pack(side='right')

# Botão de Confirmação Final
btn_confirmar = tk.Button(root, text="GERAR PLANILHA DE NOMES", bg="#4CAF50", fg="white", 
                          font=("Arial", 10, "bold"), command=confirmar)
btn_confirmar.pack(pady=20)

root.mainloop()