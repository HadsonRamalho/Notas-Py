import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas")
        self.criar_interface()

    def criar_interface(self):
        self.texto_box = tk.Text(self.root, wrap="word", undo=True, width=80, height=20)
        self.texto_box.pack(expand=True, fill="both")

        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)

        self.criar_menu_arquivo()

    def criar_menu_arquivo(self):
        menu_arquivo = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
        menu_arquivo.add_command(label="Novo", command=self.novo_arquivo)
        menu_arquivo.add_command(label="Abrir", command=self.abrir_arquivo)
        menu_arquivo.add_command(label="Salvar", command=self.salvar_arquivo)
        menu_arquivo.add_command(label="Salvar Como", command=self.salvar_como_arquivo)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.sair)

    def novo_arquivo(self):
        self.texto_box.delete("1.0", "end")

    def abrir_arquivo(self):
        arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
        if arquivo:
            try:
                with open(arquivo, 'r') as f:
                    conteudo = f.read()
                    self.texto_box.delete("1.0", "end")
                    self.texto_box.insert("1.0", conteudo)
            except Exception as e:
                messagebox.showerror("Erro ao abrir arquivo", str(e))

    def salvar_arquivo(self):
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
        if arquivo:
            try:
                with open(arquivo, 'w') as f:
                    texto = self.texto_box.get("1.0", "end-1c")
                    f.write(texto)
            except Exception as e:
                messagebox.showerror("Erro ao salvar arquivo", str(e))

    def salvar_como_arquivo(self):
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
        if arquivo:
            try:
                with open(arquivo, 'w') as f:
                    texto = self.texto_box.get("1.0", "end-1c")
                    f.write(texto)
            except Exception as e:
                messagebox.showerror("Erro ao salvar arquivo", str(e))

    def sair(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlocoDeNotas(root)
    root.mainloop()
