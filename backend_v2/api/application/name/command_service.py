from datetime import datetime, timezone

from backend_v2.api.application.name.dto import CreateNameCommand
from backend_v2.api.domain.category.repository import CategoryRepository
from backend_v2.api.domain.name.entities import Name
from backend_v2.api.domain.name.repository import NameRepository
from backend_v2.api.domain.name.services import NameDomainService


class NameCommandService:
    """
    이름(Name) 생성 관련 애플리케이션 서비스.
    """

    def __init__(
        self,
        repository: NameRepository,
        domain_service: NameDomainService | None = None,
        category_repository: CategoryRepository | None = None,
    ) -> None:
        self.repository = repository
        self.domain_service = domain_service or NameDomainService()
        self.category_repository = category_repository

    def create_name(self, command: CreateNameCommand) -> Name:
        """
        이름 생성 커맨드를 처리한다.
        """
        if self.category_repository and command.category_id:
            category = self.category_repository.get(command.category_id)
            if category is None:
                raise ValueError(f"Category '{command.category_id}' 를 찾을 수 없습니다.")

        name = Name(
            id=None,
            value=command.value,
            created_at=datetime.now(tz=timezone.utc),
            category_id=command.category_id,
        )
        self.domain_service.validate(name)
        return self.repository.save(name)


