from rest_framework import status, viewsets
from rest_framework.response import Response

from backend_v2.api.application.category.query_service import CategoryQueryService
from backend_v2.api.infrastructure.category.grpc_repository import CategoryGrpcRepository
from backend_v2.api.interfaces.rest.category.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    Category 목록 및 단건 조회를 제공하는 REST ViewSet.
    외부 gRPC Category 서비스를 호출하여 데이터를 조회한다.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        repository = CategoryGrpcRepository()
        self.query_service = CategoryQueryService(repository)

    def list(self, request):
        categories = self.query_service.list_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if pk is None:
            return Response(
                {"detail": "Category ID가 필요합니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        category = self.query_service.get_category(pk)
        if category is None:
            return Response(
                {"detail": "Category를 찾을 수 없습니다."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = CategorySerializer(category)
        return Response(serializer.data)


