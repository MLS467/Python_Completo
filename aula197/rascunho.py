from pathlib import Path
import pypdf as pdf

PASTA_RAIZ = Path(__file__).parent
PASTA_PFS_ORIGINAIS = PASTA_RAIZ / "pdfs_originais"
PASTA_NOVA = PASTA_RAIZ / "pdfs_nova"

PASTA_NOVA.mkdir(exist_ok=True)

# é uma lista de arquivos
RELATORIO_BC = PASTA_PFS_ORIGINAIS / "R20250404.pdf"

# RELATORIO_BC = PASTA_PFS_ORIGINAIS / "R20250404.pdf"
reader = pdf.PdfReader(RELATORIO_BC)

print(f"Total de páginas: {len(reader.pages)}")


# print(reader.pages[0].extract_text())
# print(len())


# BAIXAR A IMAGEM DO PDF

# # nome_img = reader.pages[0].images[0]
# faz download da imagem do pdf
# with open(PASTA_NOVA / nome_img.name, "wb") as img_file:
#     img_file.write(nome_img.data)

# ABRE O PDF E PEGA QUALQUER AS PÁGINAS
# writer = pdf.PdfWriter()
# writer.add_page(reader.pages[0])  # adiciona apenas a primeira página

# SEPARA O PDF EM VÁRIOS ARQUIVOS
# for num, page in enumerate(reader.pages):
#     # separa as páginas do pdf
#     writer = pdf.PdfWriter()
#     with open(PASTA_NOVA / f"relatorio{num}.pdf", "wb") as pdf_file:
#         writer.add_page(reader.pages[num])
#         writer.write(pdf_file)

# JUNTA O PDF EM UM ÚNICO ARQUIVO
# ao contrário
# merge = pdf.PdfWriter()

merge = pdf.PdfWriter()

for num in range(len(reader.pages) - 1, -1, -1):
    with open(PASTA_NOVA / "relatorio.pdf", "wb") as pdf_file:
        merge.add_page(reader.pages[num])
        merge.write(pdf_file)
