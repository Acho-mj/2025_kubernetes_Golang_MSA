from abc import ABC, abstractmethod
from typing import List, Optional

from backend_v2.api.domain.category.entities import Category


class CategoryRepository(ABC):
    """
    Category 엔터티에 대한 저장소 추상화.
    """

    @abstractmethod
    def list(self) -> List[Category]:
        """
        Category 전체 목록을 반환한다.
        """

    @abstractmethod
    def get(self, category_id: str) -> Optional[Category]:
        """
        ID에 해당하는 Category를 반환한다. 없으면 None.
        """


