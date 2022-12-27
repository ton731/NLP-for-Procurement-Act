from tqdm import tqdm
from rank_bm25 import BM25Okapi


# https://zhuanlan.zhihu.com/p/79202151
# http://www.cs.otago.ac.nz/homepages/andrew/papers/2014-2.pdf
def select_relevant_contexts(query, contexts, k=1):
    """
    Select the most relevant contexts based on BM25 algorithms.

    Args:
        query (str): question
        contexts (List[str]): list of contexts
        k (int): the number of relevant contexts that return

    Returns:
        List[str]: relevant contexts, ordered by correlation
    """
    # tokenize context and create BM25 object
    tokenized_contexts = [list(doc) for doc in contexts]
    bm25 = BM25Okapi(tokenized_contexts)

    # tokenize query and get each context's score
    tokenized_query = list(query)
    context_scores = bm25.get_scores(tokenized_query)

    # return the top-k best context
    top_contexts = bm25.get_top_n(tokenized_query, contexts, n=k)
    return top_contexts, context_scores[:k]



def find_question_relevant_laws(questions, laws, k=3):
    """
    Find the k most relevant laws for each question using BM25 algorithm.

    Args:
        questions (List[str]): questions
        laws (List[Dict]): laws
        k (int): the desired number of relevant laws for each question

    Returns:
        List[List[str]]: list of list contains relevant laws for each question
    """
    # extract the law strings from the laws list
    law_contexts = ["，".join([law["Chapter"], law["Clause"], law["Content"]]) for law in laws]
    
    # get relevant laws for each question
    question_relevant_laws = []
    for i in tqdm(range(len(questions))):
        question_query = questions[i]
        relevant_laws, scores = select_relevant_contexts(question_query, law_contexts, k)

        # update list
        question_relevant_laws.append(relevant_laws)

    return question_relevant_laws



def remove_law_unimportant_segements(questions, question_relevant_laws, k=2):
    """
    Use period 。 to seperate segments in a law and find the most important segments
    in the law, then convert it back to a law paragraph.

    Args:
        questions (List[str]): questions
        question_relevant_laws (List[List[str]]): list of list contains relevant laws for each question
        k (int): the desired number most relevant segment for each law

    Returns:
        List[List[str]]: the unimportant part removed list of list contains relevant laws for each question
    """
    # the processed (remove unimportant segments) laws
    processed_question_relevant_laws = []

    for i, relevant_laws in enumerate(question_relevant_laws):
        processed_relevant_laws = []
        question_query = questions[i]

        # go through all the relevant laws
        for law in relevant_laws:
            law_segments = law.split("。")
            # find the important segment in the law
            relevant_law_segments, scores = select_relevant_contexts(question_query, law_segments, k)
            # concat the segments into a full law paragraph
            processed_relevant_law = "。".join(relevant_law_segments)
            processed_relevant_laws.append(processed_relevant_law)

            print()
            print("question:", question_query)
            print("original law:", law)
            print("processed las:", processed_relevant_law)
            print()

        processed_question_relevant_laws.append(processed_relevant_laws)

    return processed_question_relevant_laws
            





def remove_bad_questions(questions):
    """
    Remove the bad questions from the quesitom list.

    Args:
        questions (List[str]): questions

    Returns:
        List[str]: the clean question list
        List[int]: index of the clean questions
    """

    SHORT_QUESTION_LEN = 13
    BAD_QUESTION_KEYWORD = ["下列", "敘述", "何者", "錯誤"]
    MAXIMUM_BAD_KEYWORD_TOLERANCE = 1

    clean_questions = []
    clean_questions_index = []

    print("start removing bad questions:")
    for i, question in enumerate(questions):
        if len(question) < SHORT_QUESTION_LEN:
            keyword_count = 0
            for keyword in BAD_QUESTION_KEYWORD:
                if keyword in question:
                    keyword_count += 1
            if keyword_count < MAXIMUM_BAD_KEYWORD_TOLERANCE:
                clean_questions.append(question)
                clean_questions_index.append(i)
            else:
                print("remove:", question)
        else:
            clean_questions.append(question)
            clean_questions_index.append(i)
            
    
    print()
    print("original question number:", len(questions))
    print("cleaned question number:", len(clean_questions))
    print()

    return clean_questions, clean_questions_index









def get_choices_scores(pred, choices):

    # tokenize choices and create BM25 object
    tokenized_choices = [list(doc) for doc in choices]
    bm25 = BM25Okapi(tokenized_choices)

    # tokenize pred and get each choices' score
    tokenized_pred = list(pred)
    choice_scores = bm25.get_scores(tokenized_pred)

    return choice_scores





















if __name__ == "__main__":
    contexts = [
    "機關應於招標文件中規定，得不發還得標廠商所繳納之保證金及其孳息，或擔保者應履行其擔保責任之事由，並敘明該項事由所涉及之違約責任、保證金之抵充範圍及擔保者之擔保責任。 ",
    "廠商對於公告金額以上採購異議之處理結果不服，或招標機關逾前條第二項所定期限不為處理者，得於收受異議處理結果或期限屆滿之次日起十五日內，依其屬中央機關或地方機關辦理之採購，以書面分別向主管機關、直轄市或縣（市）政府所設之採購申訴審議委員會申訴。地方政府未設採購申訴審議委員會者，得委請中央主管機關處理。",
    "意圖使機關規劃、設計、承辦、監辦採購人員或受機關委託提供採購規劃、設計或專案管理或代辦採購廠商之人員，洩漏或交付關於採購應秘密之文書、圖畫、消息、物品或其他資訊，而施強暴、脅迫者，處五年以下有期徒刑，得併科新臺幣一百萬元以下罰金。犯前項之罪，因而致人於死者，處無期徒刑或七年以上有期徒刑；致重傷者，處三年以上十年以下有期徒刑，各得併科新臺幣三百萬元以下罰金。 "
    ]

    query = "招標相關的問題..."

    print(select_relevant_contexts(query, contexts, 1))