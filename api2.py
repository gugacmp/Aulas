import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class TelaCadastro(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Cadastro")
        self.setGeometry(100, 100, 400, 500)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Campo "Produto"
        produto_label = QLabel("Produto:")
        self.produto_entry = QLineEdit()
        layout.addWidget(produto_label)
        layout.addWidget(self.produto_entry)

        # Campo "Valor"
        valor_label = QLabel("Valor:")
        self.valor_entry = QLineEdit()
        layout.addWidget(valor_label)
        layout.addWidget(self.valor_entry)

        # Campo "Quantidade"
        quantidade_label = QLabel("Quantidade:")
        self.quantidade_entry = QLineEdit()
        layout.addWidget(quantidade_label)
        layout.addWidget(self.quantidade_entry)

        # Botão "Atualizar"
        atualizar_button = QPushButton("Atualizar")
        atualizar_button.clicked.connect(self.atualizar)
        layout.addWidget(atualizar_button)

        # Botão "Importar"
        importar_button = QPushButton("Importar")
        importar_button.clicked.connect(self.importar)
        layout.addWidget(importar_button)

        # Botão "Gravar"
        gravar_button = QPushButton("Gravar")
        gravar_button.clicked.connect(self.gravar)
        layout.addWidget(gravar_button)

        self.setLayout(layout)

    def atualizar(self):
        produto = self.produto_entry.text()
        valor = self.valor_entry.text()
        quantidade = self.quantidade_entry.text()
        # Faça algo com os dados inseridos, como exibir uma mensagem
    
        print(f"Produto: {produto}, Valor: {valor}, Quantidade: {quantidade}")

    def importar(self):
        # Implemente a ação desejada aqui
        pass

    def gravar(self):
        # Implemente a ação desejada aqui
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_cadastro = TelaCadastro()
    tela_cadastro.show()
    sys.exit(app.exec_())
