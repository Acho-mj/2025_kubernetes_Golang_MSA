from typing import List, Optional

from backend_v2.api.domain.category.entities import Category
from backend_v2.api.domain.category.repository import CategoryRepository


class CategoryQueryService:
    """
    Category 조회 애플리케이션 서비스.
    """

    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def list_categories(self) -> List[Category]:
        return self.repository.list()

    def get_category(self, category_id: str) -> Optional[Category]:
        return self.repository.get(category_id)


