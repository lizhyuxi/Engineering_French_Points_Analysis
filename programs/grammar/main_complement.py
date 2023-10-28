# Process COD and COI

import sys, codecs

### Files processing
assert(len(sys.argv) == 3)
inp_name, out_name = sys.argv[1:]

inp = codecs.open(inp_name, 'r', 'utf-8')
out = codecs.open(out_name, 'w', 'utf-8')

lines = inp.readlines()
data = []
for line in lines:
    data.append(line[:-1].split(' '))

def get_sent_contain(i):
    st = i
    while st >= 0 and data[st][0] != '.': st -= 1
    ed = i
    while ed + 1 < len(data) and data[ed][0] != '.': ed += 1
    res = ""
    while st < ed:
        st += 1
        if st == i: res += '***'
        res += data[st][0]
        if st == i: res += '***'
        res += ' ' if st < ed else '.'
    return res

lst1 = ['me', 'te', 'le', 'la', 'les']
lst2 = ['lui', 'leur']

def write_sent(i):
    out.write('1. ' + str(i) + ': ' + get_sent_contain(i) + '\n')

def do_rule(func):
    idx = list(filter(func, list(range(len(data)))))
    for i in idx: write_sent(i)
    out.write('\n\n')

for word in lst1:
    do_rule(lambda x: data[x][1] == 'PRON' and data[x][2] == word)
for word in lst2:
    do_rule(lambda x: data[x][1] == 'PRON' and data[x][0] == word)

if True:
    idx = list(range(len(data)))
    idx = list(filter(lambda x: data[x][1] == 'PRON' and data[x][2] in ['nous', 'vous'], idx))
    for i in idx:
        flag = False
        for j in range(i, i + 3):
            if data[j][1] == 'VERB':
                if data[i][2] == 'nous':
                    flag = data[j][0][-3:] != 'ons'
                else:
                    flag = data[j][0][-2:] != 'ez'
                break
        if flag: write_sent(i)
    print("\n")
    for i in idx:
        flag = False
        for j in range(i, i + 3):
            if data[j][1] == 'VERB':
                if data[i][2] == 'nous':
                    flag = data[j][0][-3:] == 'ons'
                else:
                    flag = data[j][0][-2:] == 'ez'
                break
        if flag:
            flag = False
            for j in range(i - 3, i):
                if data[j][2] in ['nous', 'vous']: flag = True
            if flag: write_sent(i)