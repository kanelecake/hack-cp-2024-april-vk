import grpc

from concurrent import futures
from lib import searchengine_pb2_grpc, searchengine_pb2

from load import load_documents
from search.index import Index
from search.timing import timing


@timing
def index_documents(documents, idx):
    for i, document in enumerate(documents):
        idx.index_document(document)
        if i % 5000 == 0:
            print(f'Indexed {i} documents', end='\r')
    return idx


index = index_documents(load_documents(), Index())


def search(text, category):
    return index.search(text, category, search_type='OR', rank=True)


class SearchService(searchengine_pb2_grpc.SearchEngineServicer):
    def GetAnswer(self, request, context):
        result = search(request.question, request.category)
        data = result[0]
        return searchengine_pb2.GetAnswerResponse(
            answer_id=data[0].ID,
            answer=data[0].text,
            probability=result[0][1],
        )


def serve(port):
    options = [('grpc.max_send_message_length', 64 * 1024 * 1024),
               ('grpc.max_receive_message_length', 64 * 1024 * 1024)]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        options=options)
    searchengine_pb2_grpc.add_SearchEngineServicer_to_server(SearchService(), server)
    server.add_insecure_port('0.0.0.0:' + str(port))
    server.start()
    print("[INFO] gRPC Server started at port=" + str(port))
    server.wait_for_termination()
