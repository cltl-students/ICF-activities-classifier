# Function from https://stackoverflow.com/questions/44024697/how-to-read-pdf-file-using-pdfminer3k
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams, LTTextBox, LTTextLine



def convert_pdf_to_txt(pdffile):
    '''Convert pdf content from a file path to text

    :path the file path
    '''
    with open(pdffile,"rb") as fp:
        parser = PDFParser(fp)
        doc = PDFDocument(parser)
        parser.set_document(doc)
        # doc.set_parser(parser)
        # doc.initialize('')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        setattr(laparams, 'all_texts', True)
        
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        extracted_text = ''

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
            layout = device.get_result()
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    extracted_text += lt_obj.get_text()
        return extracted_text
