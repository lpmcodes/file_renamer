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

confirm = input("Renomear? (s/n): ")

if confirm != "s":
    print("Operação cancelada.")

else:
    counter = 1

    # Listar os arquivos
for file in folder.iterdir():
        if file.is_file():

            new_name = f"file_{counter}{file.suffix}"
            new_file = folder / new_name
            
            print(f"{file.name} => {new_name}")

            file.rename(new_file)

            counter += 1
