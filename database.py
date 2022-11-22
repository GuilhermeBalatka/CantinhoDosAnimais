import psycopg2 as pg


class Database:
    def __init__(self):
        self.informacoes_conexao = {
            'nome_bd': 'trab',
            'usuario_bd': 'postgres',
            'senha_bd': 'gui',
            'host_bd': 'localhost'
        }

        self.conexao = pg.connect(
            dbname=self.informacoes_conexao['nome_bd'],
            user=self.informacoes_conexao['usuario_bd'],
            password=self.informacoes_conexao['senha_bd'],
            host=self.informacoes_conexao['host_bd']
        )

        self.cursor = self.conexao.cursor()

    def executar_funcao(self, nome_funcao, tipo='inserir', *argumentos_funcao):

        if tipo == 'visualizar':
            comando = f'select * from {nome_funcao}'
            self.cursor.execute(comando)
            return self.cursor.fetchall()
        else:
            comando = f'select {nome_funcao}('
            for argumento in argumentos_funcao:
                comando += f"'{argumento}', "
            comando = comando[:-2]
            comando += ')'
            self.cursor.execute(comando)
            self.conexao.commit()
            return True

    def encerrar_conexao(self):
        self.conexao.close()

