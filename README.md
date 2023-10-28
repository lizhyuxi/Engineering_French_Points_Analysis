# Analysis of high-frequency key points of the engineering French based on the Natural Language Processing (NLP)

## Tense, Mood, and Word Frequency Analysis

### Task

1. Analyze the tenses and moods in the math books "Fonctions réelles et géométrie (Mathématiques I)" and "Algèbre Linéaire."
   The analyzed tenses and moods include:
   1. Indicatif Présent (Present Indicative)
   2. Infinitif (Infinitive)
   3. Participe Passé (Past Participle)
   4. Participe Présent (Present Participle)
   5. Indicatif Futur Simple (Simple Future Indicative)
   6. Indicatif Futur Proche (Near Future Indicative)
   7. Indicatif Imparfait (Imperfect Indicative)
   8. Indicatif Passé Composé (Compound Past Indicative)
   9. Subjonctif Présent (Present Subjunctive)
   10. Conditionnel Présent (Present Conditional)
   11. Impératif Présent (Present Imperative)
   12. Indicatif Plus-que-parfait (Pluperfect Indicative)
   13. Indicatif Futur Antérieur (Future Perfect Indicative)
   14. Subjonctif Passé (Past Subjunctive)
   15. Conditionnel Passé (Past Conditional)
   
2. Perform word frequency analysis on both books.
3. Count the occurrences of direct and indirect object personal pronouns in both books.

---

### Results

#### Tense and Mood

| Tense and Mood | Higher Mathematics I | Linear Algebra | Total Occurrences |
| ---- | ---- | ---- | ---- |
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

Note:
1. The results may not be highly accurate.
2. It's not possible to determine definitively which tense a verb corresponds to, as some verbs may have multiple tenses. When counting the occurrences of each tense, the verb will be counted in all possible tenses (e.g., "produit" may be both indicative present and past participle, so both tenses will be counted for "produit").
3. For "futur proche," verbs like "aller" will not be counted in indicative present and infinitive. Similarly, in passé composé and other compound tenses, "aller" will not be counted.
4. The results may contain a small number (single digits) of manually filtered entries.

#### Word Frequency

Type: PRON

| Word | Advanced Mathematics I | Linear Algebra | Total |
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

Type: VERB

| Word | Advanced Mathematics I | Linear Algebra | Total |
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

Type: ADJ
| Word | Advanced Mathematics I | Linear Algebra | Total |
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

Type: ADV

| Word | Advanced Mathematics I | Linear Algebra | Total |
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

Type: DET

| Word | Advanced Mathematics I | Linear Algebra | Total |
|--|----|---|---|
|le|1390|1920|3310|
|un|751|1420|2171|
|ce|100|115|215|
|tout|35|106|141|
|son|61|63|124|
|plusieurs|22|2|24|
|quel|10|12|22|
|chaque|10|11|21|

Type: ADP（adposition）

| Word | Advanced Mathematics I | Linear Algebra | Total |
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

Type: CCONJ

| Word | Advanced Mathematics I | Linear Algebra | Total |
|--|----|---|---|
|et|519|933|1452|
|ou|30|96|126|
|car|24|94|118|
|mais|14|38|52|
|puis|7|11|18|
|or|1|14|15|

Type: SCONJ

| Word | Advanced Mathematics I | Linear Algebra | Total |
|--|----|---|---|
|que|410|673|1083|
|si|221|508|729|
|lorsque|45|63|108|
|puisque|4|29|33|
|comme|13|18|31|
|quand|5|8|13|
|parce|1|0|1|

#### Direct and Indirect Object Personal Pronouns

| Word | Advanced Mathematics I | Linear Algebra | Total |
| ---------- | ----- | ------- | ----- |
| Third Person COD (le, la, les) | 17 | 21 | 38 |
| First Person Plural COI (nous) | 18 | 15 | 33 |
| Third Person COI (lui) | 3 | 1 | 4 |
| First Person Plural Reflexive Pronoun (nous) | 0 | 4 | 4 |
| First Person Plural COD (nous) | 1 | 2 | 3 |
| First Person Singular COI (me, only in remerciement section) | 1 | 1 | 2 |
| First Person Singular COD (me, only in remerciement section) | 1 | 0 | 1 |

Most of the first person plural pronouns are in the form of "nous donner" (7 in "Advanced Mathematics I" and 9 in "Linear Algebra").

#### que

| Usage | Advanced Mathematics I | Linear Algebra | Total Occurrences |
| --- | --------- | ------- | ------- |
| Relative Pronoun |  3    |    5    |     8     |
| Interrogative Pronoun |  11    |    9    |    20     |
| Subordinate Conjunction |  418      |   678     |    1096      |

#### qui

| Usage | Advanced Mathematics I | Linear Algebra | Total Occurrences |
| --- | --------- | ------- | ------- |
| Relative Pronoun |  48    |    139    |    187      |
| Interrogative Pronoun |  1    |     0    |    1     |

#### Interrogative Adjectives

*quel, quelle, quels, quelles*

| Calculus I | Linear Algebra |
| ---------- | -------------- |
|    21      |      25        |

#### Compound Relative Pronouns

*lequel, laquelle, lesquels, lesquelles*

| Calculus I | Linear Algebra |
| ---------- | -------------- |
|     4      |      16        |

---

### Packages

1. [spaCy](https://spacy.io/)
2. [spaCy fr_core_news_md](https://spacy.io/models/fr#fr_core_news_md)
3. [french-verb-conjugation](https://github.com/ianmackinnon/inflect/blob/master/french-verb-conjugation.csv)

---

### Project file structure
```
├── books
│   ├── AlgebreLineaire.pdf
│   └── M121.pdf
├── data # Required data
│   ├── french-verb-conjugation.csv
│   └── 法语语法简要大纲.docx
├── programs 
│   ├── pre_process
│   │   ├── elision.py
│   │   ├── main.py
│   │   ├── postagger.py
│   │   ├── read_pdf.py
│   │   └── trim_pdf.py
│   ├── process_verb
│   │   ├── get_tense.py
│   │   ├── main.py
│   │   └── output.py
│   ├── frequency_analysis
│   │   └── main.py
│   ├── grammar
│   │   └── main.py
├── README.md
└── result
    ├── algebre # Algebre Linéaire analysis result
	├── frequence.md
    └── m121 # M121 analysis result
```

---

### How to use

This project is entirely developed in `Python`.

Please use the latest version of Python if possible.

Install the latest versions of nltk and spaCy using `pip install nltk, spaCy`.

The development environment for this project is based on the Arch Linux distribution EndeavourOS. It has also been tested on Windows and runs correctly.

**Usage:**
1. Run `programs/pre_process/main.py`：
```bash
python3 programs/pre_process/main.py $(pdf_file_name) $(tag_file_name)
```
Where pdf_file_name represents the PDF file name **it can also be a 'txt' file with text extracted from the PDF**, and tag_file_name is the name of the tag file generated by the program.
2. Run `programs/process_verb/main.py`：
```bash
python3 programs/process_verb/main.py $(tag_file_name) $(output_directory)
```
Here, tag_file_name is the file generated in the first step, and output_directory is the name of the **folder** where the output will be stored. The output folder should be created in advance and should contain a subfolder named 'tmp'.

If there are no errors during execution, the output folder should have the following structure:
```
├── conditionnel-passe.md # Sentences in the conditionnel passé tense
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
├── new_tag.txt # Compared to the tag.txt output by pre_process, it includes all infinitives and tense phrases corresponding to verbs
├── participe-passe.md
├── participe-present.md
├── subjonctif-passe.md
├── subjonctif-present.md
└── tmp
    ├── else.md # Some words at the beginning of sentences may be in the second person singular imperative (but this type of imperative should not appear in mathematical physics books)
    └── undetermined.md # There are multiple corresponding tense phrases

```
Files with a '.md' extension are 'markdown' files. You can open them using a markdown viewer or copy the content to a markdown editor such as [水源文档](notes.sjtu.edu.cn)

3. If you need to manually filter, for example, to determine the tense and mood corresponding to a certain word, you can create a 'tmp/determined.txt' file in the **output folder** with the following format:
   The file contains several lines, each in the format $i$ 'tense' 'infinitif', where $i$ is the number of the word, 'tense' is the code for the tense, and 'infinitif' is the infinitive of the word. They are separated by **1 space**.

   Then, run the second step again, and the results will match the 'determined.txt' file.

   Example:
   ```
    1573 ind_pre dire
    6543 par_pas lier
   ```

Tense, Mood and their corresponding abbreviations:

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

---
