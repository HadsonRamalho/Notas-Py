import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas")
        self.criar_interface()
        self.arquivo_atual = None
        self.alterado = False

    def criar_interface(self):
        self.texto_box = tk.Text(self.root, wrap="word", undo=True, width=80, height=20)
        self.texto_box.pack(expand=True, fill="both")
        self.texto_box.bind("<Key>", self.atualizar_status)

        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)

        self.criar_menu_arquivo()
        self.criar_menu_edicao()

    def criar_menu_arquivo(self):
        menu_arquivo = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
        menu_arquivo.add_command(label="Novo", command=self.novo_arquivo, accelerator="Ctrl+N")
        menu_arquivo.add_command(label="Abrir", command=self.abrir_arquivo, accelerator="Ctrl+O")
        menu_arquivo.add_command(label="Salvar", command=self.salvar_arquivo, accelerator="Ctrl+S")
        menu_arquivo.add_command(label="Salvar Como", command=self.salvar_como_arquivo)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.sair, accelerator="Ctrl+Q")

        self.root.bind_all("<Control-n>", lambda event: self.novo_arquivo())
        self.root.bind_all("<Control-o>", lambda event: self.abrir_arquivo())
        self.root.bind_all("<Control-s>", lambda event: self.salvar_arquivo())
        self.root.bind_all("<Control-q>", lambda event: self.sair())

    def criar_menu_edicao(self):
        menu_edicao = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Editar", menu=menu_edicao)
        menu_edicao.add_command(label="Desfazer", command=self.texto_box.edit_undo, accelerator="Ctrl+Z")
        menu_edicao.add_command(label="Refazer", command=self.texto_box.edit_redo, accelerator="Ctrl+Shift+Z")
        menu_edicao.add_separator()
        menu_edicao.add_command(label="Copiar", command=self.copiar, accelerator="Ctrl+C")
        menu_edicao.add_command(label="Recortar", command=self.recortar, accelerator="Ctrl+X")
        menu_edicao.add_command(label="Colar", command=self.colar, accelerator="Ctrl+V")

        self.root.bind_all("<Control-z>", lambda event: self.texto_box.edit_undo())
        self.root.bind_all("<Control-Shift-Z>", lambda event: self.texto_box.edit_redo())
        self.root.bind_all("<Control-c>", lambda event: self.copiar())
        self.root.bind_all("<Control-x>", lambda event: self.recortar())
        self.root.bind_all("<Control-v>", lambda event: self.colar())

    def novo_arquivo(self):
        if self.verificar_mudancas_nao_salvas():
            self.texto_box.delete("1.0", "end")
            self.arquivo_atual = None
            self.alterado = False
            self.root.title("Bloco de Notas")

    def abrir_arquivo(self):
        if self.verificar_mudancas_nao_salvas():
            arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
            if arquivo:
                try:
                    with open(arquivo, 'r') as f:
                        conteudo = f.read()
                        self.texto_box.delete("1.0", "end")
                        self.texto_box.insert("1.0", conteudo)
                        self.arquivo_atual = arquivo
                        self.alterado = False
                        self.root.title(f"Bloco de Notas - {self.arquivo_atual}")
                except Exception as e:
                    messagebox.showerror("Erro ao abrir arquivo", str(e))

    def salvar_arquivo(self):
        if self.arquivo_atual:
            try:
                with open(self.arquivo_atual, 'w') as f:
                    texto = self.texto_box.get("1.0", "end-1c")
                    f.write(texto)
                    self.alterado = False
                    self.root.title(f"Bloco de Notas - {self.arquivo_atual}")
            except Exception as e:
                messagebox.showerror("Erro ao salvar arquivo", str(e))
        else:
            self.salvar_como_arquivo()

    def salvar_como_arquivo(self):
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
        if arquivo:
            try:
                with open(arquivo, 'w') as f:
                    texto = self.texto_box.get("1.0", "end-1c")
                    f.write(texto)
                    self.arquivo_atual = arquivo
                    self.alterado = False
                    self.root.title(f"Bloco de Notas - {self.arquivo_atual}")
            except Exception as e:
                messagebox.showerror("Erro ao salvar arquivo", str(e))

    def sair(self):
        if self.verificar_mudancas_nao_salvas():
            self.root.destroy()

    def verificar_mudancas_nao_salvas(self):
        if self.alterado:
            resposta = messagebox.askyesnocancel("Bloco de Notas", "Deseja salvar as alterações não salvas?")
            if resposta is None:
                return False
            elif resposta:
                self.salvar_arquivo()
        return True

    def atualizar_status(self, event=None):
        if not self.alterado:
            self.alterado = True
            self.root.title(f"Bloco de Notas - {self.arquivo_atual} (alterado)")

    def copiar(self):
        self.texto_box.clipboard_clear()
        self.texto_box.clipboard_append(self.texto_box.get(tk.SEL_FIRST, tk.SEL_LAST))

    def recortar(self):
        if self.texto_box.tag_ranges(tk.SEL):
            self.copiar()
            self.texto_box.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def colar(self):
        self.texto_box.insert(tk.INSERT, self.texto_box.clipboard_get())

if __name__ == "__main__":
    root = tk.Tk()
    app = BlocoDeNotas(root)
    root.mainloop()
