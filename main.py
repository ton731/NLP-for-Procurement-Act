import json
from pathlib import Path
from utils import find_question_relevant_laws

law_path = Path("data/採購法分段.json")
question_path = Path("data/train_multi_id.json")

laws = json.loads(law_path.read_text())
questions = json.loads(question_path.read_text())

questions = find_question_relevant_laws(questions, laws, 3)

for question in questions:
    print(question)