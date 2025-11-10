from typing import List, Optional

from backend_v2.api.domain.category.entities import Category
from backend_v2.api.domain.category.repository import CategoryRepository
from backend_v2.api.infrastructure.category.grpc_client import CategoryGrpcClient


class CategoryGrpcRepository(CategoryRepository):
    """
    외부 Category gRPC 서비스를 호출하여 데이터를 조회하는 저장소 구현.
    """

    def __init__(self, client: CategoryGrpcClient | None = None) -> None:
        self.client = client or CategoryGrpcClient()

    def list(self) -> List[Category]:
        response = self.client.list_categories()
        return [
            Category(
                id=category.id,
                name=category.name,
                description=category.description or None,
            )
            for category in response.categories
        ]

    def get(self, category_id: str) -> Optional[Category]:
        try:
            response = self.client.get_category(category_id)
        except Exception:
            return None

        category = response.category
        if not category.id:
            return None

        return Category(
            id=category.id,
            name=category.name,
            description=category.description or None,
        )


