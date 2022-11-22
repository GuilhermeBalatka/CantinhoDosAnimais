from tkinter import *
from tkinter import Tk

# cores -----------------------------
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra





class Coordenador:
    def __init__(self, view):
        self.view = view

    def criar_tela_login_coordenador(self):
        # dividindo a janela
        frame_cima = Frame(self.view.frame_login_coordenador, width=2000, height=100, background=co1, relief='flat')
        frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        frame_baixo = Frame(self.view.frame_login_coordenador, width=2000, height=1000, background=co4, relief='flat')
        frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        # Config frame cima
        label_nome = Label(frame_cima, text='Coordenador', anchor=NE, font=('Ivy 70'), background=co1, foreground=co4)
        label_nome.place(x=650, y=0)

        label_linha = Label(frame_cima, text='', width=5000, anchor=NW, font=('Ivy 3'), background=co2, foreground=co4)
        label_linha.place(x=0, y=90)

        # Config frame baixo
        label_nome = Label(frame_baixo, text='Nome', anchor=NW, font=('Ivy 50'), background=co4, foreground=co1)
        label_nome.place(x=550, y=100)

        receber_nome = Entry(frame_baixo, width=50, justify='left', font=("", 30), highlightthickness=1, relief='solid')
        receber_nome.place(x=100, y=200)

        label_senha = Label(frame_baixo, text='Senha', anchor=NW, font=('Ivy 50'), background=co4, foreground=co1)
        label_senha.place(x=550, y=400)

        receber_senha = Entry(frame_baixo, width=50, justify='left', font=("", 30), highlightthickness=1,
                              relief='solid', show='*')
        receber_senha.place(x=100, y=500)

        def verificar_login():
            if receber_nome.get()=='jorge' and receber_senha.get()== '123':
                print('ok')
                self.view.iniciar_tela('menu_coordenador')
            else:
                print('ko')

        botao_confirmar = Button(frame_baixo, text='Logar', width=25, height=1, font=('Ivy 25'), background='#696969',
                                 foreground=co1, relief=RAISED, overrelief=RIDGE, command=verificar_login)
        botao_confirmar.place(x=550, y=800)



    def criar_tela_menu_coordenador(self):
        botao_adicionar_animal = Button(self.view.frame_menu_coordenador, text='Adicionar Animal', width=25, height=1, font=('Ivy 25'), background=co4,
                                    command=lambda: self.view.iniciar_tela('adicionar_animal'))
        botao_adicionar_animal.place(x=55, y=250)

        botao_visualizar_animais = Button(self.view.frame_menu_coordenador, text='Visualizar Animais', width=25, height=1,
                                        font=('Ivy 25'), background=co4,
                                        command=lambda: self.view.visualizar_animais())
        botao_visualizar_animais.place(x=55, y=350)

        botao_update_animal = Button(self.view.frame_menu_coordenador, text='Atualizar Animal', width=25,
                                          height=1,
                                          font=('Ivy 25'), background=co4,
                                          command=lambda: self.view.iniciar_tela('update_animal'))
        botao_update_animal.place(x=55, y=450)

        botao_remover_animal = Button(self.view.frame_menu_coordenador, text='Remover animal', width=25,
                                     height=1,
                                     font=('Ivy 25'), background=co4,
                                     command=lambda: self.view.iniciar_tela('remover_animal'))
        botao_remover_animal.place(x=55, y=550)

        botao_adicionar_funcionario = Button(self.view.frame_menu_coordenador, text='Adicionar Funcionario', width=25,
                                      height=1,
                                      font=('Ivy 25'), background=co4,
                                      command=lambda: self.view.iniciar_tela('adicionar_funcionario'))
        botao_adicionar_funcionario.place(x=605, y=250)

        botao_visualizar_funcionarios = Button(self.view.frame_menu_coordenador, text='Adicionar Funcionario', width=25,
                                             height=1,
                                             font=('Ivy 25'), background=co4,
                                             command=lambda: self.view.iniciar_tela('visualizar_funcionarios'))
        botao_visualizar_funcionarios.place(x=605, y=350)

        botao_update_funcionario = Button(self.view.frame_menu_coordenador, text='Atualizar Funcionario', width=25,
                                               height=1,
                                               font=('Ivy 25'), background=co4,
                                               command=lambda: self.view.iniciar_tela('update_funcionario'))
        botao_update_funcionario.place(x=605, y=450)

        botao_remover_funcionario = Button(self.view.frame_menu_coordenador, text='Remover Funcionario', width=25,
                                          height=1,
                                          font=('Ivy 25'), background=co4,
                                          command=lambda: self.view.iniciar_tela('remover_funcionario'))
        botao_remover_funcionario.place(x=605, y=550)

        botao_visualizar_pessoas = Button(self.view.frame_menu_coordenador, text='Visualizar Pessoas', width=25,
                                           height=1,
                                           font=('Ivy 25'), background=co4,
                                           command=lambda: self.view.iniciar_tela('visualizar_pessoas'))
        botao_visualizar_pessoas.place(x=250, y=750)









