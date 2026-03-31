from pathlib import Path

# Caminho da pasta
folder_path = input("Digite o caminho da pasta: ")
folder = Path(folder_path)
print(f"O caminho escolhido foi: {folder}")

# Validar a pasta
if not folder.exists():
    print("O caminho não existe")

elif not folder.is_dir():
    print("Isso não é uma pasta")

else: 
    print("Pasta válida")

counter = 1

    # Listar os arquivos
for file in folder.iterdir():
        if file.is_file():

            new_name = f"file_{counter}{file.suffix}"

            print(f"Antigo: {file.name}")
            print(f"Novo: {new_name}")

            counter += 1
