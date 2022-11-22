import tkinter as tk
from paginas.coordenador import Coordenador
from paginas.pessoa import Pessoa
from paginas.menu import Menu
from paginas.animais import Animal
from paginas.funcionarios import Funcionario

frames = [
    'mostrar_menu',
    'login_coordenador',
    'menu_coordenador',
    'adicionar_animal',
    'visualizar_animais',
    'update_animal',
    'remover_animal',
    'adicionar_funcionario',
    'visualizar_funcionarios',
    'update_funcionario',
    'remover_funcionario',
    'visualizar_pessoas',
    'login_pessoa',
    'cadastro_pessoa',

]


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.title('Cantinho do animal')
        self.state('zoomed')

        self.font_name = 'Arial'
        self.font_size = {
            'titulo': 40,
            'texto': 20
        }
        self.color = {
            'titulo': 'black',
            'texto': 'black'
        }
        self.controller = controller

        self.menu = Menu(self)
        self.coordenador = Coordenador(self)
        self.pessoa = Pessoa(self)
        self.animal = Animal(self)
        self.funcionario = Funcionario(self)

        self.criar_telas()
        self.iniciar_telas()
        self.iniciar_menu()


    def main(self):
        self.mainloop()

    def iniciar_menu(self):
        self.iniciar_tela('mostrar_menu')


    def iniciar_telas(self):
        self.menu.criar_tela_menu()
        self.coordenador.criar_tela_login_coordenador()

        self.coordenador.criar_tela_menu_coordenador()
        self.animal.criar_tela_adicionar_animal()
        self.animal.criar_tela_update_animal()
        self.animal.criar_tela_remover_animal()
        self.funcionario.criar_tela_adicionar_funcionario()
        self.funcionario.criar_tela_update_funcionario()
        self.funcionario.criar_tela_remover_funcionario()
        self.pessoa.criar_tela_login_pessoa()
        self.pessoa.criar_tela_adicionar_pessoa()

    def visualizar_animais(self):
        self.iniciar_tela('visualizar_animais')
        self.animal.visualizar_animais()

    def criar_telas(self):
        self.frame_mostrar_menu = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_login_coordenador = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_menu_coordenador = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_adicionar_animal = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_visualizar_animais = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_update_animal = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_remover_animal = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_visualizar_funcionarios = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_adicionar_funcionario = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_update_funcionario = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_remover_funcionario = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_visualizar_pessoas = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_login_pessoa = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())
        self.frame_cadastro_pessoa = tk.Frame(self, width=self.winfo_width(), height=self.winfo_height())


    def remover_elementos(self, frame):
        list = frame.winfo_children()

        for item in list:
            if item.winfo_children():
                list.extend(item.winfo_children())

        return list

    def iniciar_tela(self, nome_tela):
        for frame in frames:
            eval('self.frame_'+frame+'.pack_forget()')
        eval('self.frame_'+nome_tela+".pack(fill='both', expand=1)")



#
#     janela_Coordenador = Tk()
#     janela_Coordenador.title("Cantinho do animal")
#     janela_Coordenador.geometry("490x560+610+153")
#
#
# img_fundo = PhotoImage(file="imagens\\fundo.png")
# img_coor = PhotoImage(file="imagens\\Coordenador.png")
# img_usu = PhotoImage(file="imagens\\Usuario.png")
#
# lab_fundo = Label(janela, image=img_fundo)
# lab_fundo.pack()
#
#
#
# #criar botao
# bt_coor = Button(janela, bd=0, image=img_coor, command=janela_coor)
# bt_coor.place(width=241, height=57, x=120, y=150)
#
# bt_usu = Button(janela, bd=0, image=img_usu)
# bt_usu.place(width=241, height=57, x=130, y=400)
# janela.mainloop()