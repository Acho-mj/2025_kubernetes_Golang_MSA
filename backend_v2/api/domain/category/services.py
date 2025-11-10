from backend_v2.api.domain.category.entities import Category


class CategoryDomainService:
    """
    Category 도메인 규칙을 담는 서비스.
    """

    def validate(self, category: Category) -> None:
        """
        Category 엔터티가 규칙을 만족하는지 검증한다.
        """
        if not category.id:
            raise ValueError("Category ID는 비어 있을 수 없습니다.")
        if not category.name:
            raise ValueError("Category 이름은 비어 있을 수 없습니다.")


