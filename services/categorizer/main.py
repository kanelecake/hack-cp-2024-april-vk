import os

import lib.categorizer_grpc

if __name__ == '__main__':
    lib.categorizer_grpc.serve(os.getenv("GRPC_PORT"))
