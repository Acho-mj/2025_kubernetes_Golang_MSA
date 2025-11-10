import os
from contextlib import contextmanager
from typing import Iterator

import grpc

from proto.services import category_pb2, category_pb2_grpc


DEFAULT_CATEGORY_SERVICE_ADDR = os.getenv("CATEGORY_SERVICE_ADDR", "category-service:50060")


class CategoryGrpcClient:
    """
    Category gRPC 서비스 호출을 담당하는 클라이언트 래퍼.
    """

    def __init__(self, target: str | None = None) -> None:
        self.target = target or DEFAULT_CATEGORY_SERVICE_ADDR

    @contextmanager
    def _channel(self) -> Iterator[grpc.Channel]:
        channel = grpc.insecure_channel(self.target)
        try:
            yield channel
        finally:
            channel.close()

    def list_categories(self) -> category_pb2.ListCategoriesResponse:
        with self._channel() as channel:
            stub = category_pb2_grpc.CategoryServiceStub(channel)
            request = category_pb2.ListCategoriesRequest()
            return stub.ListCategories(request)

    def get_category(self, category_id: str) -> category_pb2.GetCategoryResponse:
        with self._channel() as channel:
            stub = category_pb2_grpc.CategoryServiceStub(channel)
            request = category_pb2.GetCategoryRequest(id=category_id)
            return stub.GetCategory(request)


