import pandas as pd
from search.documents import Answer


def load_documents():
    answers = []
    df = pd.read_csv("data/database.csv")

    for id in range(0, len(df['Answer'].to_list())):
        answers.append(Answer(ID=df['answer_class'][id], text=df['Answer'][id], category=df['Category'][id], keywords=df['Keywords'][id]))

    return answers