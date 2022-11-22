from database import Database


class Model:

    def __init__(self):
        self.database = Database()

    def inserir(self, nome_funcao, *argumentos):
        return self.database.executar_funcao(nome_funcao, 'inserir', *argumentos)

    def visualisar(self, nome_funcao, *argumentos):
        return self.database.executar_funcao(nome_funcao, 'visualizar', *argumentos)

    def update(self, nome_funcao, *argumentos):
        return self.database.executar_funcao(nome_funcao, 'update', *argumentos)

    def deletar(self, nome_funcao, *argumentos):
        return self.database.executar_funcao(nome_funcao, 'deletar', *argumentos)

