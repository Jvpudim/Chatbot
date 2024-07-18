import ProjetoChatbot as pc
from tkinter import *

main_window = Tk()
main_window.title("Chatbot")
main_window.geometry("500x700")
main_window.grid()
main_window.config(background="grey")

frame = Frame(main_window)
frame.grid()
frame.config(background="grey")

l_identif = Label(frame, background="grey", text="Insira uma mensagem aqui: ")
l_identif.grid(row=0, column=0)
l_identif.config(background="grey")

e_mensagem = Entry(frame)
e_mensagem.grid(row=0, column=1)
e_mensagem.config(background="grey")

frame2 = Frame(main_window)
frame2.grid(row=1, column=0)
v = StringVar()
Label(frame2, textvariable=v).grid()
frame2.config(background="grey")

nome_maquina = "Val"
v.set("Qual seu nome?")
entrada_sugestao = False
entrada_nome_usuario = True
nome_usuario = ""

def roda_Chatbot():
    global entrada_sugestao
    global entrada_nome_usuario
    global historico_conversa
    global nome_usuario

    if entrada_nome_usuario:
        nome_usuario = e_mensagem.get()
        saudacao = pc.saudacao_GUI(nome_maquina)
        historico_conversa = nome_maquina + ": " + saudacao + "\n"
        v.set(historico_conversa)
        entrada_nome_usuario = False
    else:
        texto = e_mensagem.get()
        historico_conversa += "\n" + nome_usuario + ": " + texto
        v.set(historico_conversa)

    if entrada_sugestao:
        pc.salva_sugestao(texto)
        entrada_sugestao = False
        historico_conversa += "\n Agora aprendi! Vamos continuar nossa conversa... \n"
        v.set(historico_conversa)
    else:
        resposta = pc.buscaResposta_GUI("Cliente: " + texto + "\n")
        if resposta == "Me desculpe, não sei o que falar":
            historico_conversa += "\n Me desculpe, não sei o que falar. O que você esperava? \n"
            v.set(historico_conversa)
            entrada_sugestao = True
        else:
            historico_conversa += "\n" + pc.exibeResposta_GUI(texto, resposta, nome_maquina)
            v.set(historico_conversa)

    e_mensagem.delete(0, END)  # Limpar o campo de entrada

Button(frame, background="light yellow",text="Enviar Mensagem", command=roda_Chatbot).grid(row=0, column=2)
main_window.mainloop()