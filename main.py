import math
#pip install customtkinter
from customtkinter import *
#pip install tkinter
from tkinter.messagebox import askyesno

#Função para Encerrar programa ao clicar no X da interface gráfica
def confirmar():
    ans = askyesno(title='Sair', message='Tem certeza que quer Sair?')
    if ans:
        sys.exit()

#Criação da tela base da calculadora
app = CTk()
app.title("Calculadora")
app.geometry("320x540")
app.configure(bg="#DCDCDC")

#Criação de Frame para mostrar a conta, junto com uma label
frame_tela = CTkFrame(master=app, width= 320, height= 180, fg_color="#DCDCDC")
frame_tela.pack(pady=(0, 0), padx=(0, 0))

label_tela = CTkLabel(master=frame_tela, text="", width=320, height=180, fg_color="#DCDCDC", font=("Arial", 24), text_color="#000000")
label_tela.pack(pady=(0, 0), padx=(0, 0), fill="both", expand=True)

#Funções para escrever os itens na tela
def escrever_0():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "0"
    label_tela.configure(text=novo_texto)

def escrever_1():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "1"
    label_tela.configure(text=novo_texto)

def escrever_2():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "2"
    label_tela.configure(text=novo_texto)

def escrever_3():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "3"
    label_tela.configure(text=novo_texto)

def escrever_4():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "4"
    label_tela.configure(text=novo_texto)

def escrever_5():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "5"
    label_tela.configure(text=novo_texto)

def escrever_6():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "6"
    label_tela.configure(text=novo_texto)

def escrever_7():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "7"
    label_tela.configure(text=novo_texto)

def escrever_8():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "8"
    label_tela.configure(text=novo_texto)

def escrever_9():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "9"
    label_tela.configure(text=novo_texto)

def escrever_pct():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "%"
    label_tela.configure(text=novo_texto)

def escrever_div():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "/"
    label_tela.configure(text=novo_texto)

def escrever_vez():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "*"
    label_tela.configure(text=novo_texto)

def escrever_men():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "-"
    label_tela.configure(text=novo_texto)

def escrever_mais():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "+"
    label_tela.configure(text=novo_texto)

def escrever_virg():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "."
    label_tela.configure(text=novo_texto)

def escrever_paren_esq():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + "("
    label_tela.configure(text=novo_texto)

def escrever_paren_dir():
    texto_atual = label_tela.cget("text")
    novo_texto = texto_atual + ")"
    label_tela.configure(text=novo_texto)

#Criação de funções para pegar a expressão numérica contida na Label, realizar e mostrar os cálculos
def calcular_resultado():
    expressao = label_tela.cget("text")
    try:
        resultado = eval(expressao)
        resultado_str = str(resultado)
        label_resultado.configure(text="Resultado: " + resultado_str)
    except Exception as e:
        label_resultado.configure(text="Erro ao calcular")

def calcular_frac():
    expressao = label_tela.cget("text")
    try:
        resultado = 1/(eval(expressao)) 
        resultado_str = str(resultado)
        label_resultado.configure(text="Resultado: " + resultado_str)
    except Exception as e:
        label_resultado.configure(text="Erro ao calcular")

def calcular_elev():
    expressao = label_tela.cget("text")
    try:
        resultado = (eval(expressao)) * (eval(expressao))
        resultado_str = str(resultado)
        label_resultado.configure(text="Resultado: " + resultado_str)
    except Exception as e:
        label_resultado.configure(text="Erro ao calcular")

def calcular_raiz():
    expressao = label_tela.cget("text")
    try:
        resultado = math.sqrt(eval(expressao))
        resultado_str = str(resultado)
        label_resultado.configure(text="Resultado: " + resultado_str)
    except Exception as e:
        label_resultado.configure(text="Erro ao calcular")

def excluir_ultimo_caractere():
    texto = label_tela.cget("text")
    novo_texto = texto[:-1]  # Remove o último caractere
    label_tela.configure(text=novo_texto)

def apagar_resultado():
    label_tela.configure(text="")
    label_resultado.configure(text="")

#Criação de label para mostrar o resultado abaixo da Conta
label_resultado = CTkLabel(master=frame_tela, text="", width=320, height=30, fg_color="#DCDCDC", font=("Arial", 16), text_color="#000000")
label_resultado.pack(pady=(10, 0), padx=(0, 0), fill="both", expand=True)

#Criação de Frame em formato de Grid para alocar os botões da Calculadora
frame_botoes = CTkFrame(master=app, width= 320, height= 320, fg_color="#DCDCDC")
frame_botoes.pack(padx=0, pady=10, fill="both", expand=True)
frame_botoes.grid_columnconfigure(0,weight=80)
frame_botoes.grid_columnconfigure(1,weight=80)
frame_botoes.grid_columnconfigure(2,weight=80)
frame_botoes.grid_columnconfigure(3,weight=80)

#Primeira Linha
btn_pct = CTkButton(master=frame_botoes, text="", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0)
btn_pct.grid(row=0, column=0, padx=0, pady=0)

btn_ce = CTkButton(master=frame_botoes, text="CE", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=apagar_resultado)
btn_ce.grid(row=0, column=1, padx=0, pady=0)

btn_c = CTkButton(master=frame_botoes, text="C", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=apagar_resultado)
btn_c.grid(row=0, column=2, padx=0, pady=0)

btn_del = CTkButton(master=frame_botoes, text="DEL", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=excluir_ultimo_caractere)
btn_del.grid(row=0, column=3, padx=0, pady=0)

#Segunda Linha
btn_frac = CTkButton(master=frame_botoes, text="1/", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=calcular_frac)
btn_frac.grid(row=1, column=0, padx=0, pady=0)

btn_elev = CTkButton(master=frame_botoes, text="^", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=calcular_elev)
btn_elev.grid(row=1, column=1, padx=0, pady=0)

btn_raiz = CTkButton(master=frame_botoes, text="√", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=calcular_raiz)
btn_raiz.grid(row=1, column=2, padx=0, pady=0)

btn_div = CTkButton(master=frame_botoes, text="÷", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_div)
btn_div.grid(row=1, column=3, padx=0, pady=0)

#Terceira Linha
btn_7 = CTkButton(master=frame_botoes, text="7", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_7)
btn_7.grid(row=2, column=0, padx=0, pady=0)

btn_8 = CTkButton(master=frame_botoes, text="8", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_8)
btn_8.grid(row=2, column=1, padx=0, pady=0)

btn_9 = CTkButton(master=frame_botoes, text="9", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_9)
btn_9.grid(row=2, column=2, padx=0, pady=0)

btn_vez = CTkButton(master=frame_botoes, text="X", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_vez)
btn_vez.grid(row=2, column=3, padx=0, pady=0)

#Quarta Linha
btn_4 = CTkButton(master=frame_botoes, text="4", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_4)
btn_4.grid(row=3, column=0, padx=0, pady=0)

btn_5 = CTkButton(master=frame_botoes, text="5", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_5)
btn_5.grid(row=3, column=1, padx=0, pady=0)

btn_6 = CTkButton(master=frame_botoes, text="6", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_6)
btn_6.grid(row=3, column=2, padx=0, pady=0)

btn_men = CTkButton(master=frame_botoes, text="-", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_men)
btn_men.grid(row=3, column=3, padx=0, pady=0)

#Quinta Linha
btn_1 = CTkButton(master=frame_botoes, text="1", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_1)
btn_1.grid(row=4, column=0, padx=0, pady=0)

btn_2 = CTkButton(master=frame_botoes, text="2", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_2)
btn_2.grid(row=4, column=1, padx=0, pady=0)

btn_3 = CTkButton(master=frame_botoes, text="3", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_3)
btn_3.grid(row=4, column=2, padx=0, pady=0)

btn_mais = CTkButton(master=frame_botoes, text="+", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_mais)
btn_mais.grid(row=4, column=3, padx=0, pady=0)

#Sexta Linha
btn_par_esq = CTkButton(master=frame_botoes, text="(", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_paren_esq)
btn_par_esq.grid(row=5, column=0, padx=0, pady=0)

btn_par_dir = CTkButton(master=frame_botoes, text=")", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_paren_dir)
btn_par_dir.grid(row=5, column=1, padx=0, pady=0)

btn_zer = CTkButton(master=frame_botoes, text="0", fg_color="#FFFFFF",  font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_0)
btn_zer.grid(row=5, column=2, padx=0, pady=0)

btn_virgula = CTkButton(master=frame_botoes, text=",", fg_color="#FFFFFF", font=("Arial Bold", 12), text_color="#000000", width=75, height=45, corner_radius=0, command=escrever_virg)
btn_virgula.grid(row=5, column=3, padx=0, pady=0)

#Setima Linha
btn_result = CTkButton(master=frame_botoes, text="=", fg_color="#FFFFFF", font=("Arial Bold", 12), text_color="#000000", corner_radius=0, command=calcular_resultado)
btn_result.grid(row=6, column=0, columnspan=4, padx=0, pady=5, sticky="nsew")

app.protocol("WM_DELETE_WINDOW", confirmar)
app.mainloop()