from typing import *
from openprompt.data_utils import InputExample
import json
import utils
from itertools import chain

def get_examples(data_dir: Optional[str] , split: Optional[str] = None) -> List[InputExample]:
    outputExamples = []
    print(f'File loaded from {data_dir} ')
    with open(data_dir, "r", encoding='UTF-8') as f:
        data = json.load(f)
    for item in data:
        outputExamples.append(InputExample(guid = item['id'], text_a = item['question'], label = int(item['answer']) ))
    return outputExamples


def get_rel_examples(data_dir: Optional[str], law_dir: Optional[str] , split: Optional[str] = None) -> List[InputExample]:
    outputExamples = []
    print(f'File loaded from {data_dir} ')
    with open(data_dir, "r", encoding='UTF-8') as f:
        data = json.load(f)
    with open (law_dir, encoding='utf-8') as f:
        laws = json.load(f)
    for item in data:
        questions = [item['question']]
        questions_relevant_laws = utils.find_question_relevant_laws(questions, laws, k=2)
        questions_relevant_laws = utils.remove_law_unimportant_segements(questions, questions_relevant_laws)
        re = list(chain(*questions_relevant_laws))    
        #outputExamples.append(InputExample(guid = item['id'], text_a = re[0]+item['question'], label = int(item['answer']) ))
        outputExamples.append(InputExample(guid = item['id'], text_a = item['question'], text_b = re[0], label = int(item['answer']) ))
    return outputExamples
    
