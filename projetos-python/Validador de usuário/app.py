import customtkinter as c

c.set_appearance_mode("dark")
c.set_default_color_theme("blue")

def validar_dados():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    if not nome.replace(" ", "").isalpha():
        visor.configure(text="Nome inválido. Use apenas letras.", text_color="red")
        return
    if not senha.isdigit() or len(senha) < 6:
        visor.configure(text="Senha inválida. Apenas números e no mínimo 6 dígitos.", text_color="red")
        return

    visor.configure(text=f"Bem-vindo, {nome.title()}!\nSenha aceita!", text_color="green")

janela = c.CTk()
janela.title("Validador de Usuário")
janela.geometry("320x280")

c.CTkLabel(janela, text="Digite seu nome:", font=("Arial", 14)).pack(pady=5)
entrada_nome = c.CTkEntry(janela, width=200)
entrada_nome.pack(pady=5)

c.CTkLabel(janela, text="Digite sua senha:", font=("Arial", 14)).pack(pady=5)
entrada_senha = c.CTkEntry(janela, show="*", width=200)
entrada_senha.pack(pady=5)

c.CTkButton(janela, text="Validar", command=validar_dados).pack(pady=10)

visor = c.CTkLabel(janela, text="", font=("Arial", 13))
visor.pack(pady=10)

janela.mainloop()
