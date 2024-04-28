import grpc
import pandas as pd

from lib import categorizer_pb2_grpc, searchengine_pb2_grpc, categorizer_pb2, searchengine_pb2

categorizer = grpc.insecure_channel('127.0.0.1:18888')
searchengine = grpc.insecure_channel('127.0.0.1:18881')

categorizerStub = categorizer_pb2_grpc.CategorizerStub(categorizer)
searchengineStub = searchengine_pb2_grpc.SearchEngineStub(searchengine)

questions_df = pd.read_csv('test_data.csv')

df = pd.DataFrame(columns=['hash', 'answer_class'])

for i in range(0, len(questions_df['Question'])):
    question = questions_df['Question'][i]

    result = categorizerStub.GetCategory(categorizer_pb2.GetCategoryRequest(
        question=question,
    ))

    answerResponse = searchengineStub.GetAnswer(searchengine_pb2.GetAnswerRequest(
        question=question,
        category=result.category,
    ))

    df.loc[-1] = [questions_df['hash'][i], answerResponse.answer_id]
    df.index = df.index + 1
    df = df.sort_index()

df.to_csv('result.csv', index=False)

