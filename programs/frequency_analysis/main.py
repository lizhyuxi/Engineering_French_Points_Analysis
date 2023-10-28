import sys, codecs

### Files processing
book_num = len(sys.argv) - 2
inp_name = sys.argv[1:-1]
out_name = sys.argv[-1]

inp = [codecs.open(file, 'r', 'utf-8') for file in inp_name]
out = codecs.open(out_name, 'w', 'utf-8')

class Count:
    def __init__(self):
        self.dic = dict()
    def insert(self, key):
        if key not in self.dic:
            self.dic[key] = 0
        self.dic[key] += 1
    def get_top(self, num):
        idx = [(value, key) for key, value in self.dic.items()]
        idx = sorted(idx, reverse = True)
        return [(idx[i][1], idx[i][0]) for i in range(min(num, len(self.dic)))]
    def get_cnt(self, key):
        return self.dic[key] if key in self.dic else 0

data = []
words = []
cnt_tot = dict()
cnt_book = [dict() for _ in range(book_num)]

def doit(inp, cntx):
    lines = inp.readlines()
    for line in lines:
        l = line.strip('\n').split(' ')
        if len(l) < 3: continue
        typ, word = l[1], l[2]
        if len(word) < 2 and word != 'y' and word != 'à': continue
        data.append(l)
        words.append((typ, word))
        if typ not in cnt_tot: cnt_tot[typ] = Count()
        cnt_tot[typ].insert(word)
        if typ not in cntx: cntx[typ] = Count()
        cntx[typ].insert(word)

for i in range(book_num):
    doit(inp[i], cnt_book[i])

types = ['PRON', 'NOUN', 'VERB', 'ADJ', 'ADV', 'DET', 'ADP', 'CCONJ', 'SCONJ']

for typ in types:
    out.write('Type: ' + typ + '\n')
    out.write('| 单词 |')
    for file in inp_name: out.write(' ' + file + ' |')
    out.write(' 总数 |\n')
    out.write('|----|')
    for _ in inp_name: out.write('------------|')
    out.write('-----|\n')
    res = cnt_tot[typ].get_top(15)
    for i in range(len(res)):
        out_str = '| ' + res[i][0] + ' | '
        for cnt in cnt_book:
            out_str += str(cnt[typ].get_cnt(res[i][0])) + ' | '
        out_str += str(res[i][1]) + ' |\n'
        out.write(out_str)
    out.write('\n')
