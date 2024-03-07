import PyPDF2
import os
from typing import List


class UnionPdf:
    def __init__(
        self,
        diretorio: str = None,
        nome_arquivo_final: str = None,
        arquivos_pdf: List[str] = None,
    ) -> None:

        self.diretorio = diretorio
        self.nome_arquivo_final = nome_arquivo_final
        self.arquivos_pdf = arquivos_pdf

    def __repr__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f'União de PDFs: {self.diretorio}'

    def go_to_directory(self) -> None:
        """
        Changes the current working directory to the specified directory.

        Parameters:
        - self: The current instance of the class.

        Returns:
        - None
        """
        os.chdir(self.diretorio)

    def list_files(self) -> List[str]:
        """
        Returns a list of PDF files in the specified directory.

        Returns:
            A list of strings representing the names of PDF files in the directory.
        """
        arquivos = os.listdir(self.diretorio)
        return [arquivo for arquivo in arquivos if arquivo.endswith('.pdf')]

    def join_pdf(self, list_pdfs):
        """
        Joins multiple PDF files into a single PDF.

        Args:
            list_pdfs (list): A list of file paths to the PDF files to be joined.

        Returns:
            PyPDF2.PdfWriter: A PdfWriter object containing the joined PDF.

        """
        pdf_escrita = PyPDF2.PdfWriter()

        for arquivo in list_pdfs:
            pdf_leitura = PyPDF2.PdfReader(arquivo)

            for pagina in range(len(pdf_leitura.pages)):
                pdf_escrita.add_page(pdf_leitura.pages[pagina])

        return pdf_escrita

    def union_pdf(self) -> bool:
        """
        Combines multiple PDF files into a single PDF file.

        Returns:
            bool: True if the PDF files are successfully combined, False otherwise.
        """
        try:
            self.go_to_directory()
            if not self.arquivos_pdf:
                self.arquivos_pdf = self.list_files()

            pdf_escrita = self.join_pdf(self.arquivos_pdf)

            with open(self.nome_arquivo_final, 'wb') as f:
                pdf_escrita.write(f)

            print(f'PDF unido com sucesso: {self.nome_arquivo_final}')
            return True
        except Exception as e:
            print(f'Erro ao unir PDF: {e}')
            return False
