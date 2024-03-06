from unipdfs import UnionPdf


diretorio = 'D:/Faculdade/pdf'
arquivo_final = 'Uniao.pdf'
uniao = UnionPdf(diretorio, arquivo_final)
uniao.union_pdf()