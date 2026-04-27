import tkinter as tk
from interface import RenomeadorApp

def main():
    root = tk.Tk()
    # Inicializa a interface passando o root
    app = RenomeadorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()