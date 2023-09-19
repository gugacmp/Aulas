from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10
        self.size_hint = (None, None)
        self.size = (400, 500)

        # Campo "Produto"
        self.add_widget(Label(text="Produto:"))
        self.produto_entry = TextInput()
        self.add_widget(self.produto_entry)

        # Campo "Valor" (int)
        self.add_widget(Label(text="Valor (int):"))
        self.valor_entry = TextInput(input_filter="int")
        self.add_widget(self.valor_entry)

        # Campo "Quantidade" (int)
        self.add_widget(Label(text="Quantidade (int):"))
        self.quantidade_entry = TextInput(input_filter="int")
        self.add_widget(self.quantidade_entry)

        # Botão "Atualizar" (int)
        atualizar_button = Button(text="Atualizar (int)")
        atualizar_button.bind(on_release=self.atualizar)
        self.add_widget(atualizar_button)

        # Botão "Importar"
        importar_button = Button(text="Importar")
        importar_button.bind(on_release=self.importar)
        self.add_widget(importar_button)

        # Botão "Gravar"
        gravar_button = Button(text="Gravar")
        gravar_button.bind(on_release=self.gravar)
        self.add_widget(gravar_button)

    def atualizar(self, instance):
        produto = self.produto_entry.text
        valor = self.valor_entry.text
        quantidade = self.quantidade_entry.text
        
        total = valor_int * quantidade_int
        # Verifica se os campos de Valor e Quantidade estão vazios
        if valor and quantidade:
            # Faça algo com os dados inseridos, como exibir uma mensagem
            try:
                valor_int = int(valor)
                quantidade_int = int(quantidade)
                print(f"Produto: {produto}, Valor (int): {valor_int}, Quantidade (int): {quantidade_int}")
                print(f'Total : {total}')
            except ValueError:
                print("Valor ou Quantidade não são números inteiros.")
        else:
            print("Por favor, preencha os campos de Valor e Quantidade.")

    def importar(self, instance):
        # Implemente a ação desejada aqui
        pass

    def gravar(self, instance):
        # Implemente a ação desejada aqui
        pass

class MyApp(App):
    def build(self):
        return TelaCadastro()

if __name__ == "__main__":
    MyApp().run()
