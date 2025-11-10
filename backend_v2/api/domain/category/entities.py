from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Category:
    """
    Category 도메인 엔터티.
    """

    id: str
    name: str
    description: Optional[str] = None


