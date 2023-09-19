import wx

class TelaCadastro(wx.Frame):
    def __init__(self, parent, title):
        super(TelaCadastro, self).__init__(parent, title=title, size=(400, 500))

        panel = wx.Panel(self)

        # Campo "Produto"
        produto_label = wx.StaticText(panel, label="Produto:")
        self.produto_entry = wx.TextCtrl(panel)
        
        # Campo "Valor"
        valor_label = wx.StaticText(panel, label="Valor:")
        self.valor_entry = wx.TextCtrl(panel)
        
        # Campo "Quantidade"
        quantidade_label = wx.StaticText(panel, label="Quantidade:")
        self.quantidade_entry = wx.TextCtrl(panel)
        
        # Botão "Atualizar"
        atualizar_button = wx.Button(panel, label="Atualizar")
        self.Bind(wx.EVT_BUTTON, self.atualizar, atualizar_button)

        # Botão "Importar"
        importar_button = wx.Button(panel, label="Importar")
        self.Bind(wx.EVT_BUTTON, self.importar, importar_button)

        # Botão "Gravar"
        gravar_button = wx.Button(panel, label="Gravar")
        self.Bind(wx.EVT_BUTTON, self.gravar, gravar_button)

        # Layout
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(produto_label, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(self.produto_entry, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(valor_label, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(self.valor_entry, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(quantidade_label, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(self.quantidade_entry, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(atualizar_button, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(importar_button, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(gravar_button, 0, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(vbox)

        self.Centre()
        self.Show(True)

    def atualizar(self, event):
        produto = self.produto_entry.GetValue()
        valor = self.valor_entry.GetValue()
        quantidade = self.quantidade_entry.GetValue()
        # Faça algo com os dados inseridos, como exibir uma mensagem
        print(f"Produto: {produto}, Valor: {valor}, Quantidade: {quantidade}")

    def importar(self, event):
        # Implemente a ação desejada aqui
        pass

    def gravar(self, event):
        # Implemente a ação desejada aqui
        pass

if __name__ == '__main__':
    app = wx.App()
    TelaCadastro(None, title='Tela de Cadastro')
    app.MainLoop()
