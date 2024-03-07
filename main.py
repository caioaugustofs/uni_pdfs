from unipdfs import UnionPdf


ordem = [
    'protecao_dados.pdf',
    'LGPD_L13709d.pdf',
]    # Lisa os arquivos que serão unidos e a ordem que serão unidos

diretorio = r'D:\Faculdade\pdf'   # Diretório onde estão os arquivos
arquivo_final = 'Uniao.pdf'   # Nome do arquivo final


uniao = UnionPdf(
    diretorio=diretorio, nome_arquivo_final=arquivo_final, arquivos_pdf=None
)

uniao.union_pdf()
