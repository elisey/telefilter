import dataclasses
from abc import ABC, abstractmethod


class FilterServiceInterface(ABC):
    @abstractmethod
    def handle(self, content: str) -> str | None:
        pass


@dataclasses.dataclass
class Rules:
    include: list[str]
    # exclude: list[str]


class FilterServiceBasic(FilterServiceInterface):
    def __init__(self, rules: Rules):
        self.rules = rules

    def handle(self, content: str) -> str | None:
        for rule in self.rules.include:
            if rule.lower() in content.lower():
                return content
        return None
