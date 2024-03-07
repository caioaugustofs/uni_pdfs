# unipdfs

O programa lê todos os arquivos pdfs de um diretório e os une em um só arquivo pdf.


## Instalação
```bash
git clone https://github.com/caioaugustofs/uni_pdfs.git

python -m venv .env

source .env/bin/activate

pip install -r requirements.txt
```

## Utilização

```python
python main.py

from unipdfs import UnionPdf

ordem = [
    'protecao_dados.pdf',
    'LGPD_L13709d.pdf',
]   # Lisa os arquivos que serão unidos e a ordem que serão unidos


diretorio = r'D:\Faculdade'  # Diretório onde estão os arquivos pdfs
arquivo_final = 'Uniao.pdf'  # Nome do arquivo final


uniao = UnionPdf(diretorio=diretorio,
                 nome_arquivo_final=arquivo_final,
                 arquivos_pdf=None
)

new = uniao.union_pdf()  # imprime o nome do arquivo final e retorna true se o arquivo foi criado
print(new)
```