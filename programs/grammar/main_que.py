# Process 'qui' and 'que'

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

lst = ['qui', 'que', 'Qui', 'Que']

def write_sent(i):
    out.write('1. ' + str(i) + ': ' + get_sent_contain(i) + '\n')

def do_rule(func):
    idx = list(filter(func, list(range(len(data)))))
    for i in idx: write_sent(i)
    out.write('\n\n')

for word in lst:
    do_rule(lambda x: data[x][0] ==  word)