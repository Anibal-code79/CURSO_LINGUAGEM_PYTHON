import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Meu Primeiro Programa Gráfico")
janela.geometry("400x250")

def exibir_mensagem():
    nome_usuario = caixa_texto.get()
    messagebox.showinfo("Boas-vindas", f"Olá, {nome_usuario}! Você saiu do console!")

rotulo = tk.Label(janela, text="Digite seu nome:", font=("Arial", 15))
rotulo.pack(pady=1)  

caixa_texto = tk.Entry(janela, font=("Arial", 12), width=30)
caixa_texto.pack(pady=10)

botao = tk.Button(janela, text="Clique Aqui", font=("Arial", 12), command=exibir_mensagem)
botao.pack(pady=50)

janela.mainloop()
