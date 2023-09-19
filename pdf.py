from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import aula5

def criar_pdf(aula5):
    c = canvas.Canvas(aula, pagesize=letter)
    largura, altura = letter

    # Adicione texto ao PDF
    c.drawString(100, altura - 100, "Exemplo de PDF em Python")
    c.drawString(100, altura - 120, f'{aula5.valor}')

    # Adicione mais elementos, como gráficos, imagens, tabelas, etc., aqui

    c.save()
    print(f"PDF '{aula}' criado com sucesso.")

if __name__ == "__main__":
    criar_pdf("exemplo.pdf")
