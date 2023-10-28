echo PDF_PATH: $1
echo RES_DIR_PATH: $2

mkdir "$2"
mkdir "$2"/tmp

python3 programs/pre_process/main.py "$1" "$2"/tmp/tag.txt
python3 programs/process_verb/main.py "$2"/tmp/tag.txt "$2"
python3 programs/grammar/main_complement.py "$2"/new_tag.txt "$2"/grammaire_complment.md
python3 programs/grammar/main_que.py "$2"/new_tag.txt "$2"/grammaire_qui_que.md
