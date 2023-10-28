#########################################################
# Read text from a pdf file, and output to a txt file
# Usage: python3 main.py $(input_pdf_file_name) $(output_txt_file_name)
#########################################################

import sys, codecs
from read_pdf import read_pdf_file
from trim_pdf import trim_text
from postagger import postagging
from elision import expand_elision

assert(len(sys.argv) == 3)
pdf_name = sys.argv[1] # pdf file name
txt_name = sys.argv[2] # txt file name

print("Read pdf file...")
if pdf_name[-4:] == '.pdf':
    txt = read_pdf_file(pdf_name)
else:
    inp = codecs.open(pdf_name, 'r', 'utf-8')
    txt = str(inp.read())
print("Trim text...")
txt = '\n'.join(trim_text(txt))
print("Expanding l'élision...")
txt = expand_elision(txt)
print("POS tagging...")
tags = postagging(txt)

out = codecs.open(txt_name, 'w', 'utf-8')
out.write('\n'.join(' '.join(tag) for tag in tags))
out.close()
