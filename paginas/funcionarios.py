import tkinter as tk


class Funcionario:
    def __init__(self, view):
        self.view = view

    def criar_tela_adicionar_funcionario(self):
        labels = [
            'Nome',
            'Endereço',
            'Cargo',
            'Horario',
            'Data de nascimento',
            'CNPJ'

        ]

        entries = []
        for indice, label in enumerate(labels):
            tk.Label(
                self.view.frame_adicionar_funcionario,
                text=label,
                fg=self.view.color['texto'],
                font=(self.view.font_name, self.view.font_size['texto'])
            ).grid(row=indice, column=0, padx=20)

            entries.append(
                tk.Entry(
                    self.view.frame_adicionar_funcionario, width=30, fg=self.view.color['texto'],
                    font=(self.view.font_name, self.view.font_size['texto']),  relief='groove'

                ).grid(row=indice, column=1, padx=20)
            )

            def enviar_informacoes():
                resultado = self.view.controller.enviar_informacao(entries[0].get(), entries[1].get(), entries[2].get(),
                                                                   entries[3].get(), entries[4].get(), entries[5].get(),
                                                                  )
                if resultado:
                    for entry in entries:
                        entry.delete(0, 'end')

            botao = tk.Button(self.view.frame_adicionar_funcionario, text='enviar', command=enviar_informacoes,
                              background=self.view.color['texto'], fg='white', font=(self.view.font_name, self.view.font_size['texto']),
                              relief='flat')
            botao.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=75)

    def visualizar_tela_funcionario(self):
        lista_elementos = self.view.remover_elementos(self.view.frame_adicionar_funcionario)
        for elemento in lista_elementos:
            elemento.pack_forget()

        valores = self.view.controller.receber_funcionario
        textos = [
            'Nome',
            'Endereço',
            'Cargo',
            'Horario',
            'Data de nascimento',
            'CNPJ'
        ]

        for indice, texto in enumerate(textos):
            tk.Label(self.view.frame_visualizar_funcionario, text=texto, fg=self.view.color,
                     font=(self.view.font_name, self.view.font_size), borderwidth=self.view.border_width).grid(
                row=0, column=indice)

        for linha in range(len(valores)):
            for elemento in range(len(valores[0])):
                tk.Label(self.view.frame_visualizar_funcionario, text=valores[linha][elemento], fg=self.view.color,
                         font=(self.view.font_name, self.view.font_size), borderwidth=self.view.border_width).grid(
                    row=linha + 1, column=elemento)

    def criar_tela_update_funcionario(self):
        pass

    def criar_tela_remover_funcionario(self):
        pass

