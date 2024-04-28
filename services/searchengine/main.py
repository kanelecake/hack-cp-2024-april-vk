import os

import lib.searchengine_grpc

if __name__ == '__main__':
    lib.searchengine_grpc.serve(os.getenv("GRPC_PORT", "18881"))
