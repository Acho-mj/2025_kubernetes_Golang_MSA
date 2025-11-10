from typing import List

from backend_v2.api.domain.name.entities import Name
from backend_v2.api.domain.name.repository import NameRepository
from backend_v2.api.infrastructure.name.models import NameModel


class DjangoORMNameRepository(NameRepository):
    """
    Django ORM을 사용하는 이름(Name) 저장소 구현.
    """

    def save(self, name: Name) -> Name:
        obj = NameModel.objects.create(value=name.value, category_id=name.category_id)
        return Name(
            id=obj.id,
            value=obj.value,
            created_at=obj.created_at,
            category_id=obj.category_id,
        )

    def list(self) -> List[Name]:
        return [
            Name(
                id=obj.id,
                value=obj.value,
                created_at=obj.created_at,
                category_id=obj.category_id,
            )
            for obj in NameModel.objects.all()
        ]


