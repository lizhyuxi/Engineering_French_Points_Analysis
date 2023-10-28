#########################################################
# Read text from a pdf file, and output to a txt file
# Usage: python3 read_pdf.py $(input_pdf_file_name) $(output_txt_file_name)
#########################################################

# import sys
# 

import textract

def read_pdf_file(pdf_name):
    return textract.process(pdf_name, language = 'fr').decode('utf-8')

if __name__ == '__main__':
    import sys

    assert(len(sys.argv) == 3)
    pdf_name = sys.argv[1] # pdf file name
    txt_name = sys.argv[2] # txt file name

    import codecs
    out = codecs.open(txt_name, 'w', 'utf-8')
    out.write(read_pdf_file(pdf_name))
    out.close()
