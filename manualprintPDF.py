import sys

from pdfrw import PdfReader, PdfWriter, PdfName, PdfDict

"""
usage: python manualprintPDF.py input.py output.py

Creates: output_odd.py and output_even.pdf
"""

class manualPdfPrint:
    """for print the pdf file by manual
    """
    def __init__(self, inp_f:str, out_f:str):
        self.inp_f = PdfReader(inp_f)
        self.gen_out_f(out_f)

        self.odd_pages = []
        self.even_pages = []

    def gen_out_f(self, out_f:str):
        out_f = out_f.split('.pdf')[0]
        self.out_odd_f = PdfWriter(out_f + '_odd.pdf')
        self.out_even_f = PdfWriter(out_f + '_even.pdf')

    def check_and_make_even_pages(self):
        def blankPage(template):
            x = PdfDict()
            x.Type = PdfName.Page
            x.Contents = PdfDict(stream="")
            x.MediaBox = template.inheritable.MediaBox
            return x
        self.pages = self.inp_f.pages
        if len(self.pages) % 2 == 1:
            self.pages.append(blankPage(self.pages[0]))

    def split_pages(self):
        for i, page in enumerate(self.pages):
            if i % 2 == 0:  # extract odd pages
                self.odd_pages.append(page)
            else:
                self.even_pages.append(page)
        # reverse the even pages for printing easier
        self.even_pages.reverse()
    
    def save_pdfFile(self):
        for i in range(len(self.odd_pages)):
            self.out_odd_f.addPage(self.odd_pages[i])
            self.out_even_f.addPage(self.even_pages[i])
        self.out_odd_f.write()
        self.out_even_f.write()

    def __call__(self, *args, **kwds):
        self.check_and_make_even_pages()
        self.split_pages()
        self.save_pdfFile()

def main():
    inp_f = sys.argv[-2]
    outp_f = sys.argv[-1]

    printPDF = manualPdfPrint(inp_f, outp_f)
    printPDF()

if __name__ == '__main__':
    main()
