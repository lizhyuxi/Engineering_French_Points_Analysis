#########################################################
# Delete extra characters in txt file for data cleaning
# Usage: python3 trim_pdf.py $(input_txt_file_name) $(output_txt_file_name)
#########################################################

import re

prefixes = ["Exemple", "Remarque", "Exercice", "Définition", "Propriété", 'Rappel'] # lists of titles

def ok_start(str): # Check whether a line does NOT start with a title in prefixes
    for pre in prefixes:
        if str[0:len(pre)] == pre: return False
    return True

def count_letters(str): # Return the number of valid numbers
    return len(re.sub('[^a-zA-Z\'éÉàÀèÈùÙâÂêÊîÎôÔûÛçÇëËïÏüÜ]', '', str))

def trim_text(text):
    text = re.sub('’', '\'', text) # Use the correct l'apostrophe '
    text = re.sub('[^a-zA-Z0-9,.\\-:!?()\'éÉàÀèÈùÙâÂêÊîÎôÔûÛçÇëËïÏüÜ \n]+', '', text) # Delete all characters except the french characters
    ret = []

    lines = text.split('\n')
    flag = True
    for str in lines:
        if len(str) < 10: continue # Pass if this line does not have a lot of characters
        if str[:4] == "Page": continue # Ignore Page ???/???
        if str[:7] == "Session": # This part is Python or Wxmaxima program
            flag = False
        if ok_start(str):
            if flag and count_letters(str) > 0.5 * len(str) and ".elementary" not in str: # If it is text not a mathematical equation
                ret.append(str)
        else: # The end of Session part, and starting another part
            flag = True

    return ret

if __name__ == '__main__':
    import sys, codecs
    assert(len(sys.argv) == 3)
    inp_name = sys.argv[1] # input txt name
    out_name = sys.argv[2] # output txt name

    inp = codecs.open(inp_name, 'r', 'utf-8')
    out = codecs.open(out_name, 'w', 'utf-8')

    out.write('\n'.join(trim_text(str(inp.read()))))
