import grpc
import numpy as np

from concurrent import futures
from lib import categorizer_pb2_grpc, categorizer_pb2
from joblib import load

from lib.category_mapping import map_category_to_int


class CategorizerService(categorizer_pb2_grpc.CategorizerServicer):
    model = load('./model/model.joblib')

    def GetCategory(self, request, context):
        prediction = self.model.predict_proba([request.question])

        predicted_proba = np.array(prediction[0])
        max_prob_index = np.argmax(predicted_proba)
        max_prob_class = self.model.classes_[max_prob_index]

        max_prob = predicted_proba[max_prob_index]

        return categorizer_pb2.GetCategoryResponse(
            category=map_category_to_int(max_prob_class),
            probability=max_prob,
        )


def serve(port):
    options = [('grpc.max_send_message_length', 64 * 1024 * 1024),
               ('grpc.max_receive_message_length', 64 * 1024 * 1024)]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        options=options)
    categorizer_pb2_grpc.add_CategorizerServicer_to_server(CategorizerService(), server)
    server.add_insecure_port('0.0.0.0:' + str(port))
    server.start()
    print("[INFO] gRPC Server started at port=" + str(port))
    server.wait_for_termination()
