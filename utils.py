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

    tokenized_contexts = [list(doc) for doc in contexts]
    bm25 = BM25Okapi(tokenized_contexts)

    tokenized_query = list(query)
    context_scores = bm25.get_scores(tokenized_query)

    top_contexts = bm25.get_top_n(tokenized_query, contexts, n=k)
    return top_contexts





if __name__ == "__main__":
    contexts = [
    "機關應於招標文件中規定，得不發還得標廠商所繳納之保證金及其孳息，或擔保者應履行其擔保責任之事由，並敘明該項事由所涉及之違約責任、保證金之抵充範圍及擔保者之擔保責任。 ",
    "廠商對於公告金額以上採購異議之處理結果不服，或招標機關逾前條第二項所定期限不為處理者，得於收受異議處理結果或期限屆滿之次日起十五日內，依其屬中央機關或地方機關辦理之採購，以書面分別向主管機關、直轄市或縣（市）政府所設之採購申訴審議委員會申訴。地方政府未設採購申訴審議委員會者，得委請中央主管機關處理。",
    "意圖使機關規劃、設計、承辦、監辦採購人員或受機關委託提供採購規劃、設計或專案管理或代辦採購廠商之人員，洩漏或交付關於採購應秘密之文書、圖畫、消息、物品或其他資訊，而施強暴、脅迫者，處五年以下有期徒刑，得併科新臺幣一百萬元以下罰金。犯前項之罪，因而致人於死者，處無期徒刑或七年以上有期徒刑；致重傷者，處三年以上十年以下有期徒刑，各得併科新臺幣三百萬元以下罰金。 "
    ]

    query = "招標相關的問題..."

    print(select_relevant_contexts(query, contexts, 1))