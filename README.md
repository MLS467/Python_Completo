## 🐍 Seção 6: Módulos Python - OS, datatime, sys, json, csv, selenium, pillow e mais 🐍

---

```markdown
# 🐍 Python - Resumo do Módulo Avançado

## 📅 Datas e Horas

- `datetime.datetime`, `datetime.date`, `datetime.time`, `datetime.timedelta`
- Obter data/hora atual:  
  ```python
  from datetime import datetime
  agora = datetime.now()
  ```
- Formatar datas com `strftime`:
  ```python
  agora.strftime('%d/%m/%Y %H:%M:%S')
  ```
- `pytz` para fuso horário  
- `relativedelta` para cálculos mais complexos

## 🗂️ Arquivos e Sistema Operacional

### 🧱 Módulo `os` e `os.path`
- Navegar, criar, renomear, apagar arquivos e diretórios
- Obter tamanho de arquivos com `os.path.getsize`
- Recorrer diretórios com `os.walk`

### 🔨 Módulo `shutil`
- Copiar, mover e apagar arquivos/pastas

### 📁 `pathlib`
- Caminhos multiplataforma de forma moderna:
  ```python
  from pathlib import Path
  p = Path('meuarquivo.txt')
  ```

## 📑 JSON & CSV

### 📦 JSON
- Serializar com `json.dumps()` / `json.loads()`
- Arquivos: `json.dump()` / `json.load()`
- Uso com `TypedDict` para tipo seguro

### 📊 CSV
- Ler com `csv.reader` e `csv.DictReader`
- Escrever com `csv.writer` e `csv.DictWriter`

## 🔐 Segurança e Aleatoriedade

- `random`: `randint()`, `uniform()`, `sample()`, `choices()`
- `secrets`: números aleatórios seguros (ex: tokens)

## 📨 Variáveis de Ambiente

- `os.getenv()`, `os.environ`
- Usar `.env` com `python-dotenv`

## 📧 Envio de E-mails (SMTP)

- Configurar SMTP com Gmail
- Usar `smtplib` para enviar mensagens
- Criar senha de app no Google

## 🗜️ ZIP e Arquivos

- Compactar e descompactar com `zipfile.ZipFile`
- Exemplo:
  ```python
  with ZipFile('arquivo.zip', 'w') as zipf:
      zipf.write('arquivo.txt')
  ```

## ⚙️ Execução e Argumentos

- `sys.argv`: argumentos via terminal
- `argparse`: argumentos com descrição, tipos e ajuda
- `subprocess`: rodar comandos do sistema

## 🌐 Web e Internet

- Protocolo HTTP: `GET`, `POST`, `status code`
- Servidor com `http.server`
- Requisições com `requests`
- Web Scraping com `BeautifulSoup`
- Automatização com `Selenium`:
  - `find_element`, `By`, `WebDriverWait`, `Keys`

## 🧵 Concorrência

- Criar e gerenciar threads com `threading.Thread`

## 📚 PDF, Excel e Imagens

### 📘 PDF com PyPDF2
- Ler, escrever, mesclar PDFs

### 📗 Excel com openpyxl
- Criar e editar planilhas
- Ler e alterar dados de células

### 🖼️ Imagens com Pillow
- Redimensionar, converter e salvar imagens

## 🔁 Estrutura de Dados

- `collections.deque`: Fila (FIFO) e Pilha (LIFO)

## 🌍 Internacionalização

- `locale` para traduzir datas, moedas, etc.

## ✨ Extras

- `if __name__ == "__main__"`: ponto de entrada
- `string.Template` para substituir texto
- Dica de VS Code: ignorar tipos unknown do linter

##