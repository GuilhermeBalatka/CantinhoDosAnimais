
from tkinter import *

class Menu:
    def __init__(self, view):
        self.view = view

    def criar_tela_menu(self):
        label_titulo = Label(self.view.frame_mostrar_menu, text='Cantinho do Animal', anchor=NE, font=('Ivy 70'))
        label_titulo.place(x=500, y=10)

        # criar botao
        bt_coor = Button(self.view.frame_mostrar_menu, background="#403d3d", font= ('Ivy 25'), text='Coordenador', command=lambda: self.view.iniciar_tela('login_coordenador'))
        bt_coor.place(width=400, height=100, x=750, y=400)

        bt_usu = Button(self.view.frame_mostrar_menu, background="#403d3d", font= ('Ivy 25'), text='Usuario', command=lambda: self.view.iniciar_tela('cadastro_pessoa'))
        bt_usu.place(width=400, height=100, x=750, y=700)

