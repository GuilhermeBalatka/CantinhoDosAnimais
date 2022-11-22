from model import Model
from view import View



class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()


    def enviar_informacao(self, nome_funcao, *argumentos):
        return self.model.inserir(nome_funcao, *argumentos)



    def receber_animais(self):
        return self.model.visualisar('cadastro')

if __name__ == '__main__':
    aplicativo_animais = Controller()

    aplicativo_animais.main()
