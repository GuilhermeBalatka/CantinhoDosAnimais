import tkinter as tk


class Animal:
    def __init__(self, view):
        self.view = view

    def criar_tela_adicionar_animal(self):
        labels = [
            'Cor',
            'Tipo',
            'Nome',
            'Pelagem',
            'Data de nascimento',
            'Raça',
            'Sexo',
            'Vacinação'
        ]

        entries = []
        for indice, label in enumerate(labels):
            tk.Label(
                self.view.frame_adicionar_animal,
                text=label,
                fg=self.view.color['texto'],
                font=(self.view.font_name, self.view.font_size['texto'])
                # bw=self.view.border_width
            ).grid(row=indice, column=0, padx=20)

            entries.append(
                tk.Entry(
                    self.view.frame_adicionar_animal, width=30, fg=self.view.color['texto'], font=(self.view.font_name, self.view.font_size['texto']),  relief='groove'

                )
            )
            entries[indice].grid(row=indice, column=1, padx=20)

        def enviar_informacoes():
            resultado = self.view.controller.enviar_informacao('inserir_cadastro', entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get(), entries[5].get(), entries[6].get(), entries[7].get())
            if resultado:
                for entry in entries:
                    entry.delete(0, 'end')
                print('oi')
            print(resultado)
        botao = tk.Button(self.view.frame_adicionar_animal, text='enviar', command=enviar_informacoes, background=self.view.color['texto'], fg='white', font=(self.view.font_name, self.view.font_size['texto']), relief='flat')
        botao.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=75)

    def visualizar_animais(self):
        lista_elementos = self.view.remover_elementos(self.view.frame_adicionar_animal)
        for elemento in lista_elementos:
            elemento.pack_forget()

        valores = self.view.controller.receber_animais()
        textos = [
                'Cor',
                'Tipo',
                'Nome',
                'Pelagem',
                'Data de nascimento',
                'Raça',
                'Sexo',
                'Vacinação'
        ]

        for indice, texto in enumerate(textos):
            tk.Label(self.view.frame_visualizar_animais, text=texto, fg=self.view.color['texto'], font=(self.view.font_name, self.view.font_size['texto'])).grid(row=0, column=indice)

        for linha in range(len(valores)):
            for elemento in range(len(valores[0])):
                tk.Label(self.view.frame_visualizar_animais, text=valores[linha][elemento], fg=self.view.color['texto'], font=(self.view.font_name, self.view.font_size['texto'])).grid(row=linha+1, column=elemento)

    def criar_tela_update_animal(self):
        pass

    def criar_tela_remover_animal(self):
        pass

