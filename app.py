import tkinter as tk
import math

def calcular_tabuada():
    numero = int(numero_entry.get())
    mult = mult_entry.get()

    if mult:
        mult = int(mult)
    else:
        mult = 0

    escolha = escolha_var.get()

    if escolha == 1:
        resultados = tabuada_multiplicacao(numero, mult)
    elif escolha == 2:
        resultados = tabuada_divisao(numero, mult)
    elif escolha == 3:
        resultados = tabuada_adicao(numero, mult)
    elif escolha == 4:
        resultados = tabuada_subtracao(numero, mult)
    elif escolha == 5:
        resultados = tabuada_potencia(numero, mult)
    elif escolha == 6:
        resultados = tabuada_raiz_quadrada(numero)
    else:
        resultados = ['Opção inválida']

    resultados_text.delete('1.0', tk.END)
    resultados_text.insert(tk.END, '\n'.join(resultados))

# Funções
def tabuada_multiplicacao(numero, mult):
    return [f'{numero} x {i} = {numero * i}' for i in range(1, mult + 1)]


def tabuada_divisao(numero, mult):
    return [f'{numero} / {i} = {numero / i:.2f}' for i in range(1, mult + 1)]


def tabuada_adicao(numero, mult):
    return [f'{numero} + {i} = {numero + i}' for i in range(1, mult + 1)]


def tabuada_subtracao(numero, mult):
    return [f'{numero} - {i} = {abs(numero - i)}' for i in range(1, mult + 1)]

def tabuada_potencia(numero, mult):
    return [f'{numero} ** {i} = {math.pow(numero, i)}' for i in range(1, mult + 1)]


def tabuada_raiz_quadrada(numero):
    resultados = []
    resultado = math.sqrt(numero)
    resultados.append(f'Raíz quadrada de {numero} = {resultado:.2f}')
    return resultados

# Configuração da interface
root = tk.Tk()
root.title("Tabuada MultiTool")
root.geometry("400x600")
root.configure(background="light gray")

# Label e Entry para o número
numero_label = tk.Label(root, text="Digite o número:", background="light gray")
numero_label.pack()
numero_entry = tk.Entry(root)
numero_entry.pack()

# Label e Entry para o multiplicador
mult_label = tk.Label(root, text="Digite até qual número:", background="light gray")
mult_label.pack()
mult_entry = tk.Entry(root)
mult_entry.pack()

# Radiobuttons para escolher a operação
escolha_label = tk.Label(root, text="Escolha uma opção:",background="light gray")
escolha_label.pack()
escolha_var = tk.IntVar()
escolha_var.set(1)
multiplicacao_radiobutton = tk.Radiobutton(root, text="Multiplicação", variable=escolha_var, value=1, background="light gray", justify=tk.LEFT)
multiplicacao_radiobutton.pack(anchor=tk.W)
divisao_radiobutton = tk.Radiobutton(root, text="Divisão", variable=escolha_var, value=2, background="light gray", justify=tk.LEFT)
divisao_radiobutton.pack(anchor=tk.W)
adicao_radiobuttom = tk.Radiobutton(root, text="Adição", variable=escolha_var, value=3, background="light gray", justify=tk.LEFT)
adicao_radiobuttom.pack
subtracao_radiobutton = tk.Radiobutton(root, text="Subtração", variable=escolha_var, value=4, background="light gray", justify=tk.LEFT)
subtracao_radiobutton.pack(anchor=tk.W)
potencia_radiobutton = tk.Radiobutton(root, text="Potência", variable=escolha_var, value=5, background="light gray", justify=tk.LEFT)
potencia_radiobutton.pack(anchor=tk.W)
raizquadrada_radiobutton = tk.Radiobutton(root, text="Raiz Quadrada", variable=escolha_var, value=6, background="light gray", justify=tk.LEFT)
raizquadrada_radiobutton.pack(anchor=tk.W)

# Botão para calcular
calcular_button = tk.Button(root, text="Calcular", command=calcular_tabuada,  width=25, background="blue", fg="white")
calcular_button.pack()

# Configuração do panel
resultados_text = tk.Text(root, height=40, width=60)
resultados_text.pack()

# Execução da interface gráfica
root.mainloop()
