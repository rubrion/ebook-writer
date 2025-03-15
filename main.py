import markdown
from jinja2 import Environment, FileSystemLoader
import pdfkit

class EbookGenerator:
    def __init__(self, template_dir="templates", css_file="styles.css"):
        # Configura o ambiente de templates (os arquivos de template ficarão na pasta "templates")
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.css_file = css_file

    def render_markdown(self, content_dict):
        """
        Renderiza o template Markdown com os dados informados.
        O template (por exemplo, "ebook_template.md") deve conter as marcações Jinja2.
        """
        template = self.env.get_template("ebook_template.md")
        markdown_content = template.render(content_dict)
        return markdown_content

    def markdown_to_html(self, markdown_content):
        """
        Converte o conteúdo Markdown para HTML.
        São utilizados os extensions 'extra' e 'toc' para recursos adicionais e sumário automático.
        """
        html_content = markdown.markdown(markdown_content, extensions=['extra', 'toc'])
        return html_content

    def html_to_pdf(self, html_content, output_file="ebook.pdf"):
        """
        Converte o HTML gerado para PDF usando pdfkit.
        Certifique-se de ter o wkhtmltopdf instalado no sistema.
        """
        options = {
            'encoding': 'utf-8',
            'page-size': 'A4',
            'margin-top': '10mm',
            'margin-right': '10mm',
            'margin-bottom': '10mm',
            'margin-left': '10mm'
        }
        pdfkit.from_string(html_content, output_file, options=options, css=self.css_file)

    def generate_ebook(self, content_dict, output_file="ebook.pdf"):
        """
        Método principal que gera o ebook a partir do dicionário de conteúdo.
        """
        md_content = self.render_markdown(content_dict)
        html_content = self.markdown_to_html(md_content)
        self.html_to_pdf(html_content, output_file)
        print(f"Ebook gerado com sucesso: {output_file}")

if __name__ == "__main__":
    # Exemplo de dados para o ebook
    content = {
        "title": "Meu Ebook Incrível",
        "author": "Autor Exemplar",
        "chapters": [
            {
                "title": "Introdução",
                "content": "Este é o conteúdo da introdução do ebook. Aqui você apresenta o tema e os objetivos.",
                "images": []  # Pode ser uma lista de caminhos para imagens específicas do capítulo
            },
            {
                "title": "Capítulo 1 - Conceitos Básicos",
                "content": "Conteúdo detalhado sobre os conceitos básicos.",
                "images": ["imagens/conceito_basico.jpg"]
            },
            {
                "title": "Capítulo 2 - Avançando no Tema",
                "content": "Discussão aprofundada e exemplos práticos.",
                "images": ["imagens/exemplo.jpg", "imagens/diagram.jpg"]
            }
        ]
    }
    
    # Instancia o gerador de ebook definindo o diretório de templates e o arquivo CSS para o design
    generator = EbookGenerator(template_dir="templates", css_file="styles.css")
    generator.generate_ebook(content, output_file="meu_ebook.pdf")
