# 基于自然语言处理的工程法语高频重点分析

## 时态、语式、词频分析

---

**注意：**
目前分支 `master` 已经被更新，重构了部分代码且添加了新的 `features`。原版本见分支 `ver_1` 和 `ver_2`。

### 最新版本与 `ver_2` 的区别

1. 抛弃 `NLTK` 和 `Stanford POSTagger`，使用精确度更高、支持 `lemmatization` 的 `spaCy`；
2. 添加词频分析。
3. 添加直接、间接宾语人称代词的统计。

---

### 任务

1. 对数学书 Fonctions réelles et géométrie (Mathématiques I) 和 Algèbre Linéaire 中的语式和时态进行分析。
	分析的语式、时态包括：
	1. 直陈式现在时 Indicatif Présent
	2. 不定式 Infinitif
	3. 过去分词 Participe Passé
	4. 现在分词 Participe Présent
	5. 直陈式简单将来时 Indicatif Futur Simple
	6. 直陈式最近将来时 Indicatif Futur Proche
	7. 直陈式未完成过去时 Indicatif Imparfait
	8. 直陈式复合过去时 Indicatif Passé Composé
	9. 虚拟式现在时 Subjonctif Présent
	10. 条件式现在时 Conditionnel Présent
	11. 命令式现在时 Impératif Présent
	12. 直陈式愈过去时 Indicatif Plus-que-parfait
	13. 直陈式先将来时 Indicatif Futur Antérieur
	14. 虚拟式过去时 Subjonctif Passé
	15. 条件式过去时 Conditionnel Passé
2. 对两本书进行词频分析。
3. 对两本书统计直接、间接宾语人称代词的出现次数。

---

### 结果

#### 语式时态

|  语式时态  | 高等数学 I  | 线性代数 | 总出现次数 |
|  ----  | ----  | ---- | ---- |
| Indicatif Présent | 1853 | 3091 | 4944 |
| Infinitif | 623 | 750 | 1373 |
| Participe Passé | 440 | 569 | 1009 |
| Subjonctif Présent | 260 | 596 | 856 |
| Impératif Présent | 24 | 42 | 66 |
| Participe Présent | 152 | 185 | 337 |
| Futur Simple | 95 | 26 | 121 |
| Indicatif Passé Composé | 20 | 30 | 50 |
| Conditionnel Présent | 9 | 12 | 21 |
| Futur Proche  | 7 | 6 | 13 |
| Indicatif Imparfait | 3 | 4 | 7 |
| Indicatif Plus-que-parfait | 0 | 1 | 1 |
| Indicatif Futur Antérieur | 1 | 0 | 1 |
| Subjonctif Passé | 0 | 1 | 1 |
| Conditionnel Passé | 1 | 0 | 1 |

注：
1. 统计结果不是非常精确；
2. 不能完全确认指某个动词可能对应多种语式时态。且在计数每种语式时态出现多少次时，也会将这个动词计入（比如 produit 可能是 indicatif présent 也可能是 participe passé，那么这两种语式时态都会计入 produit）；
3. 对于 futur proche，aller 和后面的动词不会被计入 indicatif présent 和 infinitif，passé composé 和其他的复合时态同理；
4. 统计结果包含极少量（个位数）的人工筛选。

#### 词频

Type: PRON（代词）

| 单词 | 高等数学 I | 线性代数 | 总数 |
|--|----|---|---|
|on|357|751|1108|
|il|112|284|396|
|se|107|101|208|
|ce|30|178|208|
|qui|49|139|188|
|où|37|125|162|
|y|55|74|129|
|nous|64|51|115|
|lui|39|49|88|

Type: VERB（动词）

| 单词 | 高等数学 I | 线性代数 | 总数 |
|--|----|---|---|
|être|962|2092|3054|
|avoir|434|516|950|
|démontrer|7|225|232|
|définir|133|97|230|
|pouvoir|86|129|215|
|dire|75|135|210|
|montrer|176|11|187|
|voir|120|64|184|
|exister|34|118|152|
|noter|53|94|147|
|appeler|58|76|134|
|finir|6|127|133|
|continuer|109|10|119|
|vérifier|57|47|104|
|supposer|36|63|99|

Type: ADJ（形容词）
| 单词 | 高等数学 I | 线性代数 | 总数 |
|--|----|---|---|
|tel|68|154|222|
|linéaire|0|204|204|
|vectoriel|27|103|130|
|propre|1|109|110|
|fini|11|97|108|
|suivant|55|45|100|
|nul|22|77|99|
|diagonalisable|0|99|99|
|tout|22|61|83|
|inversible|0|77|77|
|particulier|13|63|76|
|stable|3|67|70|
|direct|13|53|66|
|canonique|37|23|60|
|même|15|43|58|

Type: ADV（副词）

| 单词 | 高等数学 I | 线性代数 | 总数 |
|--|----|---|---|
|alors|135|353|488|
|donc|60|274|334|
|ne|91|151|242|
|pas|71|96|167|
|non|66|93|159|
|plus|55|96|151|
|tout|10|70|80|
|seulement|12|62|74|
|même|18|50|68|
|bien|31|33|64|

Type: DET（限定词）

| 单词 | 高等数学 I | 线性代数 | 总数 |
|--|----|---|---|
|le|1390|1920|3310|
|un|751|1420|2171|
|ce|100|115|215|
|tout|35|106|141|
|son|61|63|124|
|plusieurs|22|2|24|
|quel|10|12|22|
|chaque|10|11|21|

Type: ADP（adposition，一切介词的总称）

| 单词 | 高等数学 I | 线性代数 | 总数 |
|--|----|---|---|
|de|1481|2779|4260|
|en|256|374|630|
|par|249|358|607|
|dans|188|291|479|
|sur|252|186|438|
|pour|111|299|410|
|avec|52|116|168|
|au|49|54|103|
|comme|29|54|83|
|après|8|41|49|
|entre|33|13|46|
|sous|9|25|34|
|sans|8|5|13|

Type: CCONJ（并列连词）

| 单词 | 高等数学 I | 线性代数 | 总数 |
|--|----|---|---|
|et|519|933|1452|
|ou|30|96|126|
|car|24|94|118|
|mais|14|38|52|
|puis|7|11|18|
|or|1|14|15|

Type: SCONJ（附属连词）

| 单词 | 高等数学 I | 线性代数 | 总数 |
|--|----|---|---|
|que|410|673|1083|
|si|221|508|729|
|lorsque|45|63|108|
|puisque|4|29|33|
|comme|13|18|31|
|quand|5|8|13|
|parce|1|0|1|

#### 直接宾语人称代词和间接宾语人称代词

| 代词 | 高等数学 I | 线性代数 | 总出现次数 |
| ---------- | ----- | ------- | ----- |
| 第三人称 COD（le, la, les） | 17 | 21 | 38 |
| 第一人称复数 COI（nous）| 18 | 15 | 33 |
| 第三人称 COI（lui）| 3 | 1 | 4 |
| 第一人称复数自反代词（nous）| 0 | 4 | 4 |
| 第一人称复数 COD（nous）| 1 | 2 | 3 |
| 第一人称单数 COI（me，仅在 remerciement 部分）| 1 | 1 | 2 |
| 第一人称单数 COD（me，仅在 remerciement 部分）| 1 | 0 | 1 |

其中第一人称复数大部分是 nous donner 的形式（《高等数学 I》中有 7 个，《线性代数》中有 9 个）。

#### que

| 用途 | 高等数学 I | 线性代数 | 总出现次数 |
| --- | --------- | ------- | ------- |
| 关系代词 |  3    |    5    |     8     |
| 疑问代词 |  11    |    9    |    20     |
| 从属连词 |  418      |   678     |    1096      |

#### qui

| 用途 | 高等数学 I | 线性代数 | 总出现次数 |
| --- | --------- | ------- | ------- |
| 关系代词 |  48    |    139    |    187      |
| 疑问代词 |  1    |     0    |    1     |

#### 疑问形容词

quel, quelle, quels, quelles

| 高等数学 I | 线性代数 |
| ---------- | -------- |
|     21      |   25   |

#### 复合关系代词

lequel, laquelle, lesquels, lesquelles

| 高等数学 I | 线性代数 |
| ---------- | -------- |
|     4      |   16   |

---

### Packages

1. [spaCy](https://spacy.io/)
2. [spaCy fr_core_news_md](https://spacy.io/models/fr#fr_core_news_md)
3. [french-verb-conjugation](https://github.com/ianmackinnon/inflect/blob/master/french-verb-conjugation.csv)

Python 模块：sys, textract, codecs, re, csv

---

### 项目文件结构
```
├── books
│   ├── AlgebreLineaire.pdf
│   └── M121.pdf
├── data # 需要的数据
│   ├── french-verb-conjugation.csv
│   └── 法语语法简要大纲.docx
├── programs # 编写的程序
│   ├── pre_process # 预处理部分
│   │   ├── elision.py
│   │   ├── main.py
│   │   ├── postagger.py
│   │   ├── read_pdf.py
│   │   └── trim_pdf.py
│   ├── process_verb # 处理动词
│   │   ├── get_tense.py
│   │   ├── main.py
│   │   └── output.py
│   ├── frequency_analysis
│   │   └── main.py
│   ├── grammar
│   │   └── main.py
├── README.md
└── result
    ├── algebre # Algebre Linéaire 的分析结果
	├── frequence.md
    └── m121 # M121 的分析结果
```

---

### 使用方式

本项目全部基于 `Python` 编写。

Python 请尽量使用最新版本。

`pip install nltk, spaCy` 安装最新版本 nltk 和 spaCy。

本项目的开发环境为基于 Arch Linux 下的发行版 EndeavourOS。在 Windows 上也经过测试，可以正常运行。

使用步骤：
1. 运行 `programs/pre_process/main.py`：
```bash
python3 programs/pre_process/main.py $(pdf_file_name) $(tag_file_name)
```
其中 pdf_file_name 表示 PDF 文件名**也可以是从 PDF 中提取的文字 `txt` 文件**，tag_file_name 表示程序输出 tag 文件名。
2. 运行 `programs/process_verb/main.py`：
```bash
python3 programs/process_verb/main.py $(tag_file_name) $(output_directory)
```
其中 tag_file_name 表示第一步输出的文件名，output_directory 表示输出的**文件夹**名，输出文件夹应该预先建好，并且有一个名叫 `tmp` 的子文件夹。

如果运行中没有出现错误，输出文件夹应该为如下的结构：
```
├── conditionnel-passe.md # 时态为 conditionnel passé 的句子
├── conditionnel-present.md
├── imperatif-present.md
├── indicatif-futur-anterieur.md
├── indicatif-futur-proche.md
├── indicatif-futur-simple.md
├── indicatif-imparfait.md
├── indicatif-passe-compose.md
├── indicatif-plus-que-parfait.md
├── indicatif-present.md
├── infinitif.md
├── new_tag.txt # 相比于 pre_process 输出的 tag.txt，添加了所有动词对应的的不定式和时态语式
├── participe-passe.md
├── participe-present.md
├── subjonctif-passe.md
├── subjonctif-present.md
└── tmp
    ├── else.md # 一些句首的词可能是第二人称单数的命令式（但是数学物理书中应该不会出现这类的命令式）
    └── undetermined.md # 有多种对应的时态语式
```
以 `.md` 为后缀的文件是 `markdown` 文件，可以使用对应的文件查看器打开，或者将内容拷贝至[水源文档](notes.sjtu.edu.cn)。文件在正常渲染下动词应为粗体、斜体。

3. 如果要进行人工筛选，比如确定某个词对应的时态语式，可以在**该输出文件夹**下建立 `tmp/determined.txt` 文件，文件格式如下：
   该文件包含若干行，每一行形如 $i$ `tense` `infinitif`，其中 $i$ 为这个词的编号，`tense` 为时态对应的代号，`infinitif` 为这个词的不定式。它们之间由 **1 个空格**隔开。


   然后重新运行第 2 步，得到的结果一定与 `determined.txt` 一致。

   例：
   ```
    1573 ind_pre dire
    6543 par_pas lier
   ```

时态语式及对应的代号：

|         |          |
|---------|----------|
| Indicatif Présent | ind_pre |
| Infinitif | inf |
| Indicatif Futur Simple | fut_sim |
| Indicatif Imparfait | impar |
| Subjonctif Présent | sub_pre |
| Conditionnel Présent | con_pre |
| Participe Présent | par_pre |
| Participe Passé | par_pas |
| Impératif Présent | impar |
| Indicatif Passé Composé | pas_cop |
| Indicatif Plus-que-parfait | plu_par |
| Indicatif Futur Antérieur | fut_ant |
| Subjonctif Passé | sub_pas |
| Conditionnel Passé | con_pas |

#### 示例
假设我们当前终端的工作目录为该项目的根目录。

我们建立 `result/algebre` 文件夹，代表对线性代数一书分析的最终结果。并建立 `result/algebre/tmp` 文件夹，存放临时结果。

接下来我们运行（Windows 下可以使用 `powershell` 运行）
```bash
python3 programs/pre_process/main.py books/AlgebreLineaire.pdf result/algebre/tmp/tag.txt
```
会得到 `result/algebre/tmp/tag.txt` 文件，里面存放的是 `POS tagger` 识别出来的词性及原型。

然后运行
```bash
python3 programs/process_verb/main.py result/algebre/tmp/tag.txt result/algebre
```
在 `result/algebre` 文件夹中会产生各种时态的分析文件，动词被替换成不定式的 `new_tag` 文件，以及未确定的 `tmp/undetermined.md`。

接着我们可以建立 `result/algebre/tmp/determined.txt`，其中包含着被手动确定的时态。再以同样的方式运行 `programs/process_verb/main.py`，即可将结果更新。

4. 运行 COD, COI 的统计 `programs/grammar/main.py`：
```bash
python3 programs/grammar/main.py result/algebre/new_tag.txt result/algebre/grammaire.md
```

这个程序只是把所有的宾语人称代词标示出来，因为数学书中这些词很少，而且需要手动辨别 me, nous 是直接还是间接，所以没有做自动统计。

5. 用上述同样的方式得到 M121 的结果，再运行词频分析 `programs/frequency_analysis/main.py`：
```bash
python3 programs/frequency_analysis/main.py result/algebre/new_tag.txt result/m121/new_tag.txt result/frequence.md
```

词频分析会同时统计两本书的词频，并算出总出现次数，将所有词汇分类后按总出现次数从高到底排序。


---

### 实现方式

#### 预处理 `pre_process`

1. `read_pdf.py`：使用 `textract` 模块将 `PDF` 文件中的文字部分提取出来。
2. `trim_pdf.py`：只保留法语字母和数字，其次读取标题信息删除所有的代码 `Session` 部分，并判断每一行是不是数学公式（法语字母个数大于总字符数的一半）。
3. `elision.py`：先将 s'il 扩展成 si il，再将剩余原形为 e 结尾的省音扩展（**注意，所有 l' 会被展开为 le**）。
4. `postagger.py`：使用 Stanford POS tagger 得到每一个词的词性。可能是由于内存问题，必须将一本书划分成几段，对于每一段求 POS，最后整合起来。

`main.py` 即将上述四个程序整合起来。

#### 处理动词 `process_verb`

1. `get_tense.py`：使用 `french-verb-conjugation.csv` 整理出来的信息，求出每个动词对应的时态以及原形。
	文件包含一个 `GetTense` 类，支持以下方法：
	1. `__init__()`：即初始化。构造函数可以传一个参数，表示 csv 文件路径；也可以不传，默认为 `data/french-verb-conjugation.csv`。
		使用 `csv` 模块将 csv 文件中的所有信息读取出来。
	2. `get_tenses(word)`：返回一个列表，列表中每个元素为一个二元组，表示动词原形和对应的时态。
	3. `get_compound_verb(word)`：返回该动词（`word` 为不定式）在复合时态中的助动词列表，可能是 `['avoir'], ['être'], ['avoir', 'être']`。
2. `output.py`：定义 `Output` 类，以及 `OutputFile` 类。

	`OutputFile` 类优化对每个文件的输出，它包含一个缓冲区，支持添加和删除操作，解构的时候再将缓冲区的所有信息输出到文件。

	`Output` 类是对所有时态文件输出的整合，会自动调用 `OutputFile` 类。

	`Output` 类支持一下功能：
	1. `__init__(out_name, text)`：`out_name` 为输出的文件夹名，`text` 为 `tag` 文件中的所有信息。
	2. `sent_contain(i)`：求出包含第 $i$ 个词的句子，返回的是一个三元组，依次为这个句子的字符串，起始位置，终止位置。
	3. `write(tense, i)`：将第 $i$ 个词输出到 `tense` 对应的 `OutputFile`。
	4. `remove(tense, i)`：将第 $i$ 个词从 `tense` 对应的 `OutputFile` 删去。
	5. `pop(tense)`：将 `tense` 对应的 `OutputFile` 中最后添加的删去。
3. `main.py`：使用上述两个 Python 文件，处理“所有动词”对应的全部语式时态。
	其中“所有动词”包括：
	1. Stanford POS tagger 识别为 VERB 或者 AUX（有可能是复合时态中的助动词）的词；
	2. 开头字母为大写的词（可能是命令式）；
	3. soit 和 soient（数学证明过程中常常使用）。
	`main.py` 会首先判断 `$(output_directory)/tmp/determined.txt` 文件是否存在，如果存在就将其信息全部读取出来。
	接着依次处理每个动词可能对应的时态。句首的动词只可能是命令式或者虚拟式（Soit, Soient）。POS tagger 正常识别为 VERB 或 AUX 的动词有以下 $5$ 种情况：
	1. 该动词的形式只可能对应一种时态语式，则直接处理（参考程序中的 `dict1`）；
	2. 该动词是一个过去分词，可能与前面的助动词构成复合时态（参考程序中的 `dict2`）。如果前面的助动词是 avoir，则只可能是复合时态，此时需将 avoir 对应的时态删去；否则也有可能只作为一个过去分词；
	3. 该动词是不定式，前面是 aller 的直陈式现在时形式，构成最近将来时；
	4. 除了上述情况的直陈式现在时和不定式；
	5. 该动词可能是虚拟式，需判断前面有没有 que。

	除此之外，我们发现：一些动词可能会被识别成古法语，比如 est 会被识别成 être 和 **estre**。但是两者之间其他时态的变位不一样，所以我们认为不定式可能为 être 的动词一定比 estre 的多。于是在处理可能对应多个不定式的动词时，我们数这些不定式出现的总数，并选取出现次数最高的那个作为其真正的原形。


---

### 问题 or to-do

1. 添加对词组的频率分析（多个词的词频分析）；
2. 对不能完全确认的时态进行确认；
3. 如果需要可以尝试对更多语法点分析。
