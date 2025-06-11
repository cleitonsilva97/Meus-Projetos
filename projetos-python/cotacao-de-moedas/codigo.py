import requests
from tkinter import *

def coletar_cotacoes():
    try:
        requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")
        requisicao.raise_for_status()
        dados = requisicao.json()

        cotacao_dolar = dados['USDBRL']['bid']
        cotacao_euro = dados['EURBRL']['bid']
        texto = f"Dólar: R$ {cotacao_dolar}\nEuro: R$ {cotacao_euro}"
    except:
        texto = "Erro ao buscar cotações.\nVerifique sua conexão."
    
    visor.config(text=texto)

janela = Tk()
janela.title('Cotação de Moedas')
janela.geometry("320x220")
janela.resizable(False, False)
janela.configure(bg="#f0f0f0")

frame_central = Frame(janela, bg="#f0f0f0")
frame_central.pack(expand=True)

texto1 = Label(
    frame_central,
    text='Seja bem-vindo!',
    font=("Arial", 11, "bold"),
    justify="center",
    bg="#f0f0f0"
)
texto1.pack(pady=10)

botao = Button(
    frame_central,
    text='buscar cotações',
    font=("Arial", 12),
    command=coletar_cotacoes
)
botao.pack(pady=10)

visor = Label(
    frame_central,
    text='',
    font=("Arial", 11),
    justify="center",
    bg="#f0f0f0"
)
visor.pack(pady=10)

janela.mainloop()
