import tkinter as tk
from tkinter import messagebox 

def converter():
    binario = entrada_binario.get() 

    try:
        decimal = int(binario, 2)       
        octal = oct(decimal)[2:]           
        hexadecimal = hex(decimal)[2:].upper()    

        
        label_decimal.config(text=f"Decimal: {decimal}")
        label_octal.config(text=f"Octal: {octal}")
        label_hexadecimal.config(text=f"Hexadecimal: {hexadecimal.upper()}")

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas 0 e 1!")
        entrada_binario.delete(0, tk.END)  


janela = tk.Tk()
janela.title("Conversor Binário")
janela.geometry("320x250")
janela.resizable(False, False)


titulo = tk.Label(janela, text="Conversor de Binário", font=("Arial", 16, "bold"))
titulo.pack(pady=10)


entrada_binario = tk.Entry(janela, font=("Arial", 14), justify="center")
entrada_binario.pack(pady=5)


btn_converter = tk.Button(janela, text="Converter", font=("Arial", 12), command=converter)
btn_converter.pack(pady=10)


label_decimal = tk.Label(janela, text="Decimal: ", font=("Arial", 12))
label_decimal.pack()

label_octal = tk.Label(janela, text="Octal: ", font=("Arial", 12))
label_octal.pack()

label_hexadecimal = tk.Label(janela, text="Hexadecimal: ", font=("Arial", 12))
label_hexadecimal.pack()


janela.mainloop()
