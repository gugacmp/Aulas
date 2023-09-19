from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 8
        self.spacing = 8
        self.size_hint = (None, None)
        self.size = (450, 450)

        # Campo "Produto"
        self.add_widget(Label(text="Produto:"))
        self.produto_entry = TextInput()
        self.add_widget(self.produto_entry)

        # Campo "Valor"
        self.add_widget(Label(text="Valor:"))
        self.valor_entry = TextInput()
        self.add_widget(self.valor_entry)

        # Campo "Quantidade"
        self.add_widget(Label(text="Quantidade:"))
        self.quantidade_entry = TextInput()
        self.add_widget(self.quantidade_entry)

        # Botão "Atualizar"
        atualizar_button = Button(text="Atualizar")
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
        # Faça algo com os dados inseridos, como exibir uma mensagem
        print(f"Produto: {produto}, Valor: {valor}, Quantidade: {quantidade}")

    def importar(self, instance):
        produto = self.produto_entry.text
        valor = self.valor_entry.text
        quantidade = self.quantidade_entry.text
        # Faça algo com os dados inseridos, como exibir uma mensagem
        print(f"Produto: {produto}, Valor: {valor}, Quantidade: {quantidade}")

    def gravar(self, instance):
        # Implemente a ação desejada aqui
        pass

class MyApp(App):
    def build(self):
        return TelaCadastro()

if __name__ == "__main__":
    MyApp().run()
