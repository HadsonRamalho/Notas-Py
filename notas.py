import tkinter as tk
from tkinter import filedialog

def salvar_arquivo():
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
    with open(arquivo, 'w') as f:
        texto = texto_box.get("1.0", "end-1c")
        f.write(texto)

def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
    with open(arquivo, 'r') as f:
        conteudo = f.read()
        texto_box.delete("1.0", "end")
        texto_box.insert("1.0", conteudo)

# interface gráfica
root = tk.Tk()
root.title("Bloco de Notas")

texto_box = tk.Text(root, wrap="word", undo=True, width=80, height=20)
texto_box.pack(expand=True, fill="both")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu_arquivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Novo")
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.destroy)

root.mainloop()
