from unipdfs import UnionPdf


diretorio = 'D:/Faculdade/pdf' # Diretório onde estão os arquivos
arquivo_final = 'Uniao.pdf' # Nome do arquivo final

ordem =['protecao_dados.pdf','LGPD_L13709.pdf',] # Lista com os arquivos que serão unidos e a ordem que serão unidos opcional 

uniao = UnionPdf(diretorio= diretorio,
                 nome_arquivo_final=arquivo_final,
                 arquivos_pdf=None)

uniao.union_pdf()