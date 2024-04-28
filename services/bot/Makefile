GRPC_FOLDER=./lib
PROTO_FILE_SEARCH=./protos/searchengine.proto
PROTO_FILE_CAT=./protos/categorizer.proto

.PHONY: build_proto
build_proto:
	python -m grpc_tools.protoc -I./protos --python_out=$(GRPC_FOLDER) --pyi_out=$(GRPC_FOLDER) --grpc_python_out=$(GRPC_FOLDER) $(PROTO_FILE_SEARCH)
	python -m grpc_tools.protoc -I./protos --python_out=$(GRPC_FOLDER) --pyi_out=$(GRPC_FOLDER) --grpc_python_out=$(GRPC_FOLDER) $(PROTO_FILE_CAT)

.PHONY: freeze_pip
freeze_pip:
	pip freeze > requirements.txt